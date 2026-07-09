from django.urls import path
from .views import export_students_excel, export_students_pdf

urlpatterns = [
    path("export/excel/", export_students_excel, name="export-excel"),
    path("export/pdf/", export_students_pdf, name="export-pdf"),
]