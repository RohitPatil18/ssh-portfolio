from django.db import models
from departments.models import Department
from django.utils.text import slugify

def consultant_picture_path(instance, filename):
    foldername = slugify(instance.name)
    return f'{foldername}/{filename}'

class Consultant(models.Model):
    """
    Database entity for `Consultant` entity
    """
    name = models.CharField(max_length=200)
    education = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    display_picture = models.ImageField(upload_to=consultant_picture_path, null=True)
    is_active = models.BooleanField(
        default=True,
        verbose_name='Status',
        help_text="Currently working with hospital?"
    )

    class Meta:
        db_table = 'consultant'

    def __str__(self):
        return f'{self.name} ({self.department.title})'


def display_picture_path(instance, filename):
    foldername = slugify(instance.name)
    return f'{foldername}/{filename}'

class Management(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    display_picture = models.ImageField(upload_to=display_picture_path)
    linkedin = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    is_active = models.BooleanField(
        default=True,
        verbose_name='Status',
        help_text="Currently working with hospital?"
    )

    class Meta:
        db_table = 'management'