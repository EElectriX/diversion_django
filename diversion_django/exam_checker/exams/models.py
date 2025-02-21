from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class AnswerSheet(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answer_sheets')
    file = models.FileField(upload_to='answer_sheets/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    assigned_teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assigned_sheets')
    marks = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.student.username} - {self.file.name}"
