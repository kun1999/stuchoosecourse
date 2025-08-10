from django.db import models


class Student(models.Model):
    student_no = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    major = models.CharField(max_length=100, blank=True)
    grade = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.student_no} - {self.name}"
