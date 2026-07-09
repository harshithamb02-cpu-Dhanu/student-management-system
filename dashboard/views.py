from datetime import date

from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from students.models import Student
from faculty.models import Faculty
from courses.models import Course
from attendance.models import Attendance


class DashboardAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        total_students = Student.objects.count()

        total_faculty = Faculty.objects.count()

        total_courses = Course.objects.count()

        today = date.today()

        today_attendance = Attendance.objects.filter(
            date=today
        )

        present = today_attendance.filter(
            status="Present"
        ).count()

        absent = today_attendance.filter(
            status="Absent"
        ).count()

        leave = today_attendance.filter(
            status="Leave"
        ).count()

        recent_students = Student.objects.order_by(
            "-created_at"
        )[:5]

        students = []

        for student in recent_students:

            students.append({
                "id": student.id,
                "student_name": student.student_name,
                "email": student.email,
            })

        data = {
            "total_students": total_students,
            "total_faculty": total_faculty,
            "total_courses": total_courses,

            "today_attendance": {
                "present": present,
                "absent": absent,
                "leave": leave,
            },

            "recent_students": students
        }

        return Response(data)