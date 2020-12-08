from faker import Faker
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Q
from django.shortcuts import render
from django.views.generic.base import View

from OII_LR.forms import RequestForm, CreatePersonForm, TraficLightForm
from OII_LR.models import Candidates
from OII_LR.utils import get_experience_affiliations, get_age_affiliations


def index(request):
    return render(request, 'index.html')


class RequestView_LR_1(View):
    def get(self, request: WSGIRequest):
        return render(request, 'lr_1/request_page.html', context={'form': RequestForm()})

    def post(self, request: WSGIRequest):
        bound_form = RequestForm(request.POST)
        if bound_form.is_valid():
            experience = {
                'small': Q(experience_small__gt=0),
                'middle': Q(experience_middle__gt=0),
                'big': Q(experience_big__gt=0),
            }.get(bound_form.data.get('experience'))
            age = {
                'small': Q(age_small__gt=0),
                'middle': Q(age_middle__gt=0),
                'big': Q(age_big__gt=0),
            }.get(bound_form.data.get('age'))
            candidates = Candidates.objects.filter(age & experience)
            return render(request, 'lr_1/request_page.html', context={
                'form': RequestForm(request.POST),
                'candidates': candidates
            })


class CreateCandidateForm_LR_1(View):
    def get(self, request: WSGIRequest):
        candidates = Candidates.objects.all()
        return render(request, 'lr_1/create_page.html', context={
            'form': CreatePersonForm(),
            'candidates': candidates
        })

    def post(self, request: WSGIRequest):
        bound_form = CreatePersonForm(request.POST)
        if bound_form.is_valid():
            data = bound_form.data
            affiliations_age = get_age_affiliations(data.get('age'))
            affiliations_experience = get_experience_affiliations(data.get('experience'))
            faker = Faker()
            candidate = Candidates(first_name=faker.first_name(), last_name=faker.last_name(), age=data.get('age'),
                                   experience=data.get('experience')) \
                .set_affiliations(affiliations_age, affiliations_experience)
            candidate.save()
            candidates = Candidates.objects.all()
            return render(request, 'lr_1/create_page.html', context={
                'form': CreatePersonForm(),
                'candidates': candidates
            })


class LR2View(View):
    def get(self, request: WSGIRequest):
        return render(request, 'lr_2/main_page.html', context={'form': TraficLightForm()})

    def post(self, request: WSGIRequest):
        return render(request, 'lr_2/main_page.html', context={'form': TraficLightForm()})

