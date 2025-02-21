

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class ExamSheet(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    exam_name = models.CharField(max_length=255)
    answer_sheet = models.FileField(upload_to='answer_sheets/')
    marks = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.student.username} - {self.exam_name}"
