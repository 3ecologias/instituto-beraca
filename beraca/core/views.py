from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.template.loader import get_template
from django.contrib import messages
from django.views import generic
from django.views.generic.base import TemplateView

# Create your views here.
# def fullsite(request):
# 	context_general = {}
# 	return render(request, 'core/index.html', context_general)

class Index(TemplateView):
	template_name = "core/index.html"

class AboutView(TemplateView):
    template_name = "core/about.html"
