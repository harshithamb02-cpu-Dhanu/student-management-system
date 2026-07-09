from django.db import models
from django.contrib.auth.models import User


class AuditLog(models.Model):

    ACTION_CHOICES = (
        ("CREATE", "CREATE"),
        ("UPDATE", "UPDATE"),
        ("DELETE", "DELETE"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    model_name = models.CharField(max_length=100)

    object_id = models.IntegerField()

    action = models.CharField(
        max_length=20,
        choices=ACTION_CHOICES
    )

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.model_name} - {self.action}"