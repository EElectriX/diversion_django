

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from organisation_app.models import ExamSheet
from .forms import ExamSheetForm

def is_organisation(user):
    return user.groups.filter(name='Organisation').exists()

@login_required
@user_passes_test(is_organisation)
def organisation_dashboard(request):
    sheets = ExamSheet.objects.all()
    return render(request, 'organisation/dashboard.html', {'sheets': sheets})

@login_required
@user_passes_test(is_organisation)
def upload_sheet(request):
    if request.method == 'POST':
        form = ExamSheetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('organisation_dashboard')
    else:
        form = ExamSheetForm()
    return render(request, 'organisation/upload_sheet.html', {'form': form})
