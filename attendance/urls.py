from django.urls import path
from .views import (
    AttendanceListCreateView,
    AttendanceDetailView,
    DashboardView,
)

urlpatterns = [
    path("attendance/", AttendanceListCreateView.as_view(), name="attendance-list"),
    path("attendance/<int:pk>/", AttendanceDetailView.as_view(), name="attendance-detail"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
]