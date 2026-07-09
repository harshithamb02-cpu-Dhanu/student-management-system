from django.db import models
from students.models import Student


class Attendance(models.Model):

    STATUS_CHOICES = (
        ("Present", "Present"),
        ("Absent", "Absent"),
        ("Leave", "Leave"),
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="attendance"
    )

    date = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):
        return self.student.student_name