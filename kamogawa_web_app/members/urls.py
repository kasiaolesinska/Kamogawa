from django.urls import path
from .views import StaffDetailView, BoxerDetailView

urlpatterns = [
    path('boxer/<pk>', BoxerDetailView.as_view(), name='boxer-detail'),
    path('staff/<pk>', StaffDetailView.as_view(), name='staff-detail'),
]
