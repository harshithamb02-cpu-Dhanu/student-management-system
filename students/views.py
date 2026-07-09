from django.http import HttpResponse
from openpyxl import Workbook
from reportlab.pdfgen import canvas
from .models import Student

def export_students_excel(request):
    wb = Workbook()
    ws = wb.active
    ws.title = "Students"

    ws.append([
        "ID",
        "Name",
        "Email",
        "Phone",
        "DOB",
        "Gender",
        "Course"
    ])

    students = Student.objects.select_related("course").all()

    for student in students:
        ws.append([
            student.id,
            student.student_name,
            student.email,
            student.phone,
            str(student.dob),
            student.gender,
            student.course.course_name,
        ])

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="students.xlsx"'

    wb.save(response)
    return response

def export_students_pdf(request):
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="students.pdf"'

    p = canvas.Canvas(response)

    p.setFont("Helvetica-Bold", 16)
    p.drawString(180, 800, "Student List")

    y = 770

    students = Student.objects.select_related("course").all()

    p.setFont("Helvetica", 10)

    for student in students:
        text = (
            f"{student.id} | "
            f"{student.student_name} | "
            f"{student.email} | "
            f"{student.phone} | "
            f"{student.course.course_name}"
        )

        p.drawString(40, y, text)
        y -= 20

        if y < 50:
            p.showPage()
            p.setFont("Helvetica", 10)
            y = 800

    p.save()

    return response