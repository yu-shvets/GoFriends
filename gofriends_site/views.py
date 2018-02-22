from django.shortcuts import render, reverse, HttpResponseRedirect
from django.views.generic import TemplateView
from .forms import CustomerForm
from django.views.generic.edit import CreateView
from django.http import JsonResponse
from .models import Services, HomeBanners, CaseStudies, Industries, About, Testimonials


class HomeView(TemplateView):
    template_name = 'gofriends_site/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['form'] = CustomerForm
        context['services'] = Services.objects.all()
        context['banners'] = HomeBanners.objects.all()
        context['cases'] = CaseStudies.objects.all()
        context['industries'] = Industries.objects.all()
        context['team'] = About.objects.all()
        context['testimonials'] = Testimonials.objects.all()
        return context


class CustomerCreate(CreateView):
    form_class = CustomerForm

    def form_valid(self, form):
        response_data = {'name': '', 'mail': '', 'success': ''}
        self.obj = form.save(commit=False)
        self.obj.save()
        response_data['success'] = 'Your e-mail was successfully submitted!'
        return JsonResponse(response_data)

