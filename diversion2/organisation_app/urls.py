from django.urls import path
from .views import organisation_dashboard, upload_sheet

urlpatterns = [
    path('', organisation_dashboard, name='organisation_dashboard'),
    path('upload/', upload_sheet, name='upload_sheet'),
]
