from django.db import models
from .models import *
from django.contrib import messages



class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 6:
            errors['name'] = "Name must have more than 5 characters"
        if len(postData['description']) < 16:
            errors['desc'] = "Description must have more than 15 characters"
        return errors

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

class Description(models.Model):
    description = models.CharField(max_length=255)
    course = models.OneToOneField(Course, related_name="course")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# class Description(models.Model):
#     description = models.OneToOneField(Course, related_name="description")