from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Resume, Role, AnalysisReport, Skill
from .forms import ResumeUploadForm, UserRegisterForm
from .utils import extract_text_from_pdf, analyze_resume_gap

def home(request):
    if request.user.is_authenticated:
        recent_reports = AnalysisReport.objects.filter(resume__user=request.user).order_by('-created_at')[:5]
        return render(request, 'analyzer/dashboard.html', {'recent_reports': recent_reports})
    return render(request, 'analyzer/index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'analyzer/register.html', {'form': form})

@login_required
def upload_resume(request):
    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)
        role_id = request.POST.get('role_id')
        
        if form.is_valid() and role_id:
            role = get_object_or_404(Role, pk=role_id)
            resume = form.save(commit=False)
            resume.user = request.user
            
            # Extract text
            file_obj = request.FILES['file']
            resume.extracted_text = extract_text_from_pdf(file_obj)
            resume.save()
            
            # Perform Analysis
            skills = role.skills.all()
            matched, missing, score = analyze_resume_gap(resume.extracted_text, skills)
            
            recommendations = "Good job!" if score > 80 else "Consider learning missing skills and gaining more practical experience."
            if missing:
                recommendations += " Focus on: " + ", ".join(missing[:3])
            
            report = AnalysisReport.objects.create(
                resume=resume,
                role=role,
                score=score,
                matched_skills=matched,
                missing_skills=missing,
                recommendations=recommendations
            )
            
            return redirect('report_detail', report_id=report.id)
        else:
            messages.error(request, "Please upload a valid PDF and select a role.")
    else:
        form = ResumeUploadForm()
        
    roles = Role.objects.all()
    return render(request, 'analyzer/upload.html', {'form': form, 'roles': roles})

@login_required
def report_detail(request, report_id):
    report = get_object_or_404(AnalysisReport, pk=report_id, resume__user=request.user)
    return render(request, 'analyzer/report_detail.html', {'report': report})
