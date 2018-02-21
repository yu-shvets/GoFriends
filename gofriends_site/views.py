from django.shortcuts import render, reverse, HttpResponseRedirect
from django.views.generic import TemplateView
from .forms import CustomerForm
from django.views.generic.edit import CreateView
from django.http import JsonResponse


class HomeView(TemplateView):
    template_name = 'gofriends_site/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['form'] = CustomerForm
        return context


class CustomerCreate(CreateView):
    form_class = CustomerForm

    def form_valid(self, form):
        response_data = {'name': '', 'mail': '', 'success': ''}
        self.obj = form.save(commit=False)
        self.obj.save()
        response_data['success'] = 'Success!'
        return JsonResponse(response_data)

