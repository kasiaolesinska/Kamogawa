from django.urls import path
from .views import StaffDetailView, BoxerDetailView

urlpatterns = [
    path('Boxer/<pk>', BoxerDetailView, name='boxer-detail'),
    path('Staff/<pk>', StaffDetailView, name='staff-detail'),
]
