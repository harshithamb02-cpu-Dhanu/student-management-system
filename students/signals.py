from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Student
from auditlog.models import AuditLog


@receiver(post_save, sender=Student)
def student_saved(sender, instance, created, **kwargs):
    AuditLog.objects.create(
        model_name="Student",
        object_id=instance.id,
        action="CREATE" if created else "UPDATE",
        description=f"Student '{instance.student_name}' {'created' if created else 'updated'}."
    )


@receiver(post_delete, sender=Student)
def student_deleted(sender, instance, **kwargs):
    AuditLog.objects.create(
        model_name="Student",
        object_id=instance.id,
        action="DELETE",
        description=f"Student '{instance.student_name}' deleted."
    )