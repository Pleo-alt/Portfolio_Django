from django.contrib import admin
from .models import Skills, Certificates, Project, Challenge, FuturePlans

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('name','description','percentage')
    search_fields = ('name',)
    list_filter = ('percentage',)

@admin.register(Certificates)
class CertificatesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')
    search_fields = ('name',)
    list_filter = ('description',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'github_link')
    search_fields = ('title',)
    list_filter = ('description',)

@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)
    list_filter = ('description',)

@admin.register(FuturePlans) 
class FuturePlansAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)
    list_filter = ('description',)