from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    fees = models.DecimalField(max_digits=10, decimal_places=2)

    faculty = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="courses"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name