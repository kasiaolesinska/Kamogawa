from django.shortcuts import render
from django.views.generic import DetailView
from .models import Boxer, Staff


class BoxerDetailView(DetailView):
    model = Boxer
    context_object_name = 'boxer'


class StaffDetailView(DetailView):
    model = Staff
    context_object_name = 'staff'

