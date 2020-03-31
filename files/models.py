import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class File(models.Model):
    file = models.FileField(upload_to='provisional_files')
    file_type = models.CharField(max_length=200)
    belongs_to_student = models.ForeignKey('Student', on_delete=models.DO_NOTHING)
    timestamp = models.DateTimeField('date published')

    def __str__(self):
        return self.file_type

    def was_uploaded_recently(self):
        return self.timestamp >= timezone.now() - datetime.timedelta(days=1)

class Student(models.Model):
    name = models.CharField(max_length=300)
    age = models.IntegerField()
    country_of_citizenship = models.CharField(max_length=300)
    morningside_ID = models.IntegerField()
    sevis_ID = models.IntegerField()
    profile_picture = models.ImageField(upload_to="imgs")
    email = models.EmailField()
    major = models.CharField(max_length=300)
    status = models.CharField(max_length=300)
    graduation_year = models.IntegerField
    student_class = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name
    
    