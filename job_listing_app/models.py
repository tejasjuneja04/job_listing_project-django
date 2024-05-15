from django.db import models

def user_directory_path(instance, filename):
    return 'company_logos/{0}'.format(filename)

class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    required_skills = models.CharField(max_length=255)
    employment_type = models.CharField(max_length=50)
    salary = models.CharField(max_length=50)
    job_description = models.TextField()
    company_logo = models.ImageField(upload_to=user_directory_path, null=True, verbose_name="")

class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    message = models.TextField()
