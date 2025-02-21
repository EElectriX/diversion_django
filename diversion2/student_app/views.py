

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from organisation_app.models import ExamSheet

def is_student(user):
    return user.groups.filter(name='Student').exists()

@login_required
@user_passes_test(is_student)
def student_dashboard(request):
    sheets = ExamSheet.objects.filter(student=request.user)
    return render(request, 'student/dashboard.html', {'sheets': sheets})
