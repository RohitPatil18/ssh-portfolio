from django.db import models

class Department(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)
    is_active = models.BooleanField(
        default=True,
        help_text="Active Status."
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'department'

    def __str__(self):
        return self.title