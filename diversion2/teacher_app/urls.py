from django.urls import path
from .views import teacher_dashboard, check_answer_sheet

urlpatterns = [
    path('', teacher_dashboard, name='teacher_dashboard'),
    path('check/<int:sheet_id>/', check_answer_sheet, name='check_answer_sheet'),
]
