from rest_framework import viewsets, filters
filter_backends = [filters.SearchFilter]
search_fields = ["student_name"]
from rest_framework.permissions import IsAuthenticated

from .models import AuditLog
from .serializers import AuditLogSerializer


class AuditLogViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = AuditLog.objects.all().order_by("-created_at")

    serializer_class = AuditLogSerializer

    permission_classes = [IsAuthenticated]

    