from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils.timezone import now

from .models import Attendance
from .serializers import AttendanceSerializer

from students.models import Student
from faculty.models import Faculty
from courses.models import Course


# GET + POST Attendance
class AttendanceListCreateView(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]


# GET Single Attendance
class AttendanceDetailView(generics.RetrieveAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]


# Dashboard API
class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {
            "total_students": Student.objects.count(),
            "total_faculty": Faculty.objects.count(),
            "total_courses": Course.objects.count(),
            "today_attendance": Attendance.objects.filter(
                date=now().date()
            ).count(),
            "recent_students": list(
                Student.objects.order_by("-id").values("id", "student_name")[:5]
            ),
        }
        return Response(data)