from django.shortcuts import render
from django.views.generic import DetailView
from .models import Boxer, Staff


class BoxerDetailView(DetailView):
    model = Boxer


class StaffDetailView(DetailView):
    model = Staff

