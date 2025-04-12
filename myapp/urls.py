from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('skills/', views.skills, name='skills'),
    path('skill/<int:skill_id>/description/', views.skill_description, name='skill_description'),  
    path('certificate/', views.certificate, name='certificate'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path ('challenges/', views.challenges, name='challenges'),
    path('future_plans/', views.future_plans, name='future_plans'),
    path('resume/', views.resume, name='resume'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    