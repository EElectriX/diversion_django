# from django.urls import path
# from . import views

# urlpatterns = [
#     path('upload/', views.upload_sheet, name='upload_sheet'),
#     path('evaluate/', views.evaluate_sheets, name='evaluate_sheets'),
#     path('mark/<int:sheet_id>/', views.mark_sheet, name='mark_sheet'),
# ]



from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_sheet, name='upload_sheet'),
    path('evaluate/', views.evaluate_sheets, name='evaluate_sheets'),
    path('mark/<int:sheet_id>/', views.mark_sheet, name='mark_sheet'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='exams/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
