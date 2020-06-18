from django.db import models
from django.contrib.auth.models import User

# Create your models here.
LICENCE_TYPE = (
    ('class_a',"class_a"),
    ('class_b',"class_b"),
    ('class_c',"class_c"),
)
class Institution(models.Model):

    INSTITUTION_TYPE = (
        ('hospital',"hospital"),
        ('pharmacy',"pharmacy"),
    )
    name = models.CharField(max_length=100, unique=True)
    industry = models.CharField(max_length=100, choices=INSTITUTION_TYPE)
    contact_person = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    created_by = models.ForeignKey( User, null=True,on_delete=models.SET_NULL, related_name="created_by")
    created_at = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey( User, null=True,on_delete=models.SET_NULL, related_name="approved_by")
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

class Company(models.Model):
    name = models.CharField(max_length=100)
    licence_class = models.CharField(max_length=100, choices=LICENCE_TYPE)
    licence_number = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Electrician(models.Model):
    name = models.CharField(max_length=100)
    licence_class = models.CharField(max_length=100, choices=LICENCE_TYPE)
    licence_number = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    listed = models.BooleanField(default=False)

    def __str__(self):
        return self.name