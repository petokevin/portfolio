from django.conf import settings
from django.shortcuts import render
from .data import TECHNOLOGIES, COMPETENCIES, PROJECTS, EXPERIENCE, EDUCATION


def index(request):
    return render(request, 'main/index.html', {
        'technologies': TECHNOLOGIES, 'competencies': COMPETENCIES,
        'projects': PROJECTS, 'experience': EXPERIENCE, 'education': EDUCATION,
        'contact_email': settings.CONTACT_EMAIL,
        'contact_linkedin': settings.CONTACT_LINKEDIN,
    })
