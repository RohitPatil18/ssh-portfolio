from django.db import models

class Enquiry(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "enquiry"
        ordering = ('-created_at', )