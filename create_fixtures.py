import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from analyzer.models import Role, Skill

def create_data():
    # Skills
    python, _ = Skill.objects.get_or_create(name='Python')
    django_skill, _ = Skill.objects.get_or_create(name='Django')
    sql, _ = Skill.objects.get_or_create(name='SQL')
    docker, _ = Skill.objects.get_or_create(name='Docker')
    aws, _ = Skill.objects.get_or_create(name='AWS')
    js, _ = Skill.objects.get_or_create(name='JavaScript')
    react, _ = Skill.objects.get_or_create(name='React')
    ml, _ = Skill.objects.get_or_create(name='Machine Learning')

    # Roles
    # Python Developer
    py_dev, _ = Role.objects.get_or_create(
        title='Python Developer',
        defaults={'description': 'Backend development with Python and Django.'}
    )
    py_dev.skills.add(python, django_skill, sql, docker, aws)
    
    # Frontend Developer
    fe_dev, _ = Role.objects.get_or_create(
        title='Frontend Developer',
        defaults={'description': 'Frontend development with React and JS.'}
    )
    fe_dev.skills.add(js, react)

    print("Initial data created successfully.")

if __name__ == '__main__':
    create_data()
