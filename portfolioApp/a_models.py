# from django.db import models
# from django.contrib.auth.models import User
# from django.utils.text import slugify
# from .utils import get_random_code
#
# # Create your models here.
#
# class Profile(models.Model):
#     first_name = models.CharField(max_length=200, blank=True)
#     last_name = models.CharField(max_length=200, blank=True)
#     bio = models.CharField(max_length=500, blank=True)
#     profile_pic = models.ImageField(default='profiles.png', upload_to='profile_pics/')
#     # skills = models.ForeignKey('portfolioApp.Skills', on_delete=models.CASCADE, null=True)
#     # projects = models.ForeignKey('portfolioApp.Portfolio', on_delete=models.CASCADE, null=True)
#     facebook = models.URLField(max_length=50, blank=True)
#     email = models.CharField(max_length=200, blank=True)
#     github = models.URLField(max_length=50, blank=True)
#     twitter = models.URLField(max_length=50, blank=True)
#     linkedin = models.URLField(max_length=50, blank=True)
#     hacker_rank = models.URLField(max_length=50, blank=True)
#     slug = models.SlugField(unique=True, blank=True)
#
#
# class Skills(models.Model):
#     profile = models.ForeignKey(Profile, related_name='skills', on_delete=models.CASCADE)
#     skill = models.CharField(max_length=200, blank=True)
#
#     def __str__(self):
#         return f"{self.skill}"
#
#
# class Portfolio(models.Model):
#     profile = models.ForeignKey(Profile, related_name='portfolio', on_delete=models.CASCADE)
#     project = models.CharField(max_length=200, blank=True)
#     project_img = models.ImageField(default='project.png', upload_to='project_img')
#     def __str__(self):
#         return f"{self.project}"
#
