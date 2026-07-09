# courses/serializers.py

from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    faculty_name = serializers.CharField(
        source="faculty.get_full_name",
        read_only=True
    )

    class Meta:
        model = Course
        fields = [
            "id",
            "course_name",
            "duration",
            "fees",
            "faculty",
            "faculty_name",
            "created_at",
            "updated_at",
        ]