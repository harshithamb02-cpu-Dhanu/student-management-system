import django_filters
from .models import Student


class StudentFilter(django_filters.FilterSet):
    course = django_filters.CharFilter(
        field_name="course__course_name",
        lookup_expr="icontains"
    )

    faculty = django_filters.CharFilter(
        field_name="faculty__faculty_name",
        lookup_expr="icontains"
    )

    gender = django_filters.CharFilter(
        field_name="gender",
        lookup_expr="iexact"
    )

    class Meta:
        model = Student
        fields = ["course", "faculty", "gender"]