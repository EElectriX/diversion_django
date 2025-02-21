
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from organisation_app.models import ExamSheet

def is_teacher(user):
    return user.groups.filter(name='Teacher').exists()

@login_required
@user_passes_test(is_teacher)
def teacher_dashboard(request):
    sheets = ExamSheet.objects.all()
    return render(request, 'teacher/dashboard.html', {'sheets': sheets})

@login_required
@user_passes_test(is_teacher)
def check_answer_sheet(request, sheet_id):
    sheet = ExamSheet.objects.get(id=sheet_id)
    if request.method == 'POST':
        marks = request.POST.get('marks')
        sheet.marks = marks
        sheet.save()
        return redirect('teacher_dashboard')
    return render(request, 'teacher/check_sheet.html', {'sheet': sheet})
