from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code_melli = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    country = models.CharField(max_length=100, null=True, default='')
    city = models.CharField(max_length=100, null=True, default='')
    birthday = models.DateField(null=True, default=None)
    father_name = models.CharField(max_length=100, null=True, default='')
    mother_name = models.CharField(max_length=100, null=True, default='')
    address = models.CharField(max_length=200, null=True, default='')
    postal_code = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.user
