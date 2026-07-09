from django.db import models
from courses.models import Course


class Student(models.Model):

    student_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    gender = models.CharField(max_length=10)

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        null=False
    )

    def __str__(self):
        return self.student_name