from django.urls import path
from .views import StaffDetailView, BoxerDetailView

urlpatterns = [
    path('Boxer/<pk>', BoxerDetailView.as_view(), name='boxer-detail'),
    path('Staff/<pk>', StaffDetailView.as_view(), name='staff-detail'),
]
