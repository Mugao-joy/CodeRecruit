from django.db import models

# Create your models here.
class jobs(models.Model):
    company = models.CharField(max_length=200)
    job_title = models.CharField(max_length=400)
    requirements = models.TextField(max_length= 150)
    location = models.TextField(max_length=200)
    Hours = models.CharField(max_length=50)
    salary = models.FloatField(max_length= 100)

    def __str__(self):
        return self.company