from django.db import models
import uuid

class Url(models.Model):
    url = models.CharField(max_length=1000)

    def __str__(self):
        return self.url
    

class Profile(models.Model):
    url = models.ForeignKey(Url, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    headline = models.CharField(max_length=10000)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    company = models.CharField(max_length=1000)
    location = models.CharField(max_length=1000)
    start_date = models.CharField(max_length=1000)
    end_date = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return f"{self.title} at {self.company}"
    
class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    school = models.CharField(max_length=1000)
    degree = models.CharField(max_length=1000)
    field_of_study = models.CharField(max_length=1000)
    start_date = models.CharField(max_length=1000)
    end_date = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return f"{self.degree} in {self.field_of_study} at {self.school}"
    
class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)

    def __str__(self):
        return self.skill_name
