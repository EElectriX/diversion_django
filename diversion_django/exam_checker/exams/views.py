

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import AnswerSheet
from .forms import AnswerSheetForm

@login_required
def upload_sheet(request):
    if request.method == 'POST':
        form = AnswerSheetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AnswerSheetForm()
    return render(request, 'exams/upload.html', {'form': form})

@login_required
def evaluate_sheets(request):
    sheets = AnswerSheet.objects.filter(assigned_teacher=request.user)
    return render(request, 'exams/evaluate.html', {'sheets': sheets})

@login_required
def mark_sheet(request, sheet_id):
    sheet = AnswerSheet.objects.get(id=sheet_id)
    if request.method == 'POST':
        sheet.marks = request.POST.get('marks')
        sheet.save()
        return redirect('evaluate_sheets')
    return render(request, 'exams/mark.html', {'sheet': sheet})


def home(request):
    return render(request, 'exams/home.html')


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home after registration
    else:
        form = UserCreationForm()
    return render(request, 'exams/register.html', {'form': form})

#mon@1234567
#sap

