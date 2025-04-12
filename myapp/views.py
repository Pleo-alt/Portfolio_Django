from django.shortcuts import render
from .models import Skills, Certificates, Project, Challenge, FuturePlans
from django.conf import settings

def home(request):
    return render(request, 'home.html')  

def skills(request):
    skills = Skills.objects.all()
    return render(request, 'skills.html', {'skills': skills})

def skill_description(request, skill_id):
    try:
        skill = Skills.objects.get(id=skill_id)
        data = {
            'name': skill.name,
            'description': skill.description  # Assuming you have a `description` field
        }
        return JsonResponse(data)
    except Skills.DoesNotExist:
        return JsonResponse({'error': 'Skill not found'}, status=404)

def about(request):
    return render(request, 'about.html', {'MEDIA_URL': settings.MEDIA_URL})

def certificate(request):
    # Fetch all certificates from the database
    all_certificates = Certificates.objects.all()
    
    # Pass the certificates to the template
    return render(request, 'certificates.html', {'certificates': all_certificates})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def contact(request):
    return render(request, 'contact.html')

def challenges(request):
    challenges = Challenge.objects.all()
    return render(request, 'challenges.html', {"challenges": challenges})

def future_plans(request):
    future_plans = FuturePlans.objects.all()
    return render(request, 'future_plans.html', {"future_plans": future_plans})

def resume(request):
    return render(request, 'resume.html', {'MEDIA_URL': settings.MEDIA_URL})