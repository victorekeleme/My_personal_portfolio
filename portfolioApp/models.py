from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Skill(models.Model):
    skill = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.skill}"

    class Meta:
        verbose_name_plural = 'skills'

class Project(models.Model):
    name = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    url = models.URLField(max_length=200, blank=True)
    project_img = models.ImageField(default='project.png', upload_to='project_img')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = 'projects'

