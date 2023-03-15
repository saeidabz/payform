from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100, null=True, default='')
    country = models.CharField(max_length=100, null=True, default='')
    birthday = models.DateField(null=True, default=None)
    father_name = models.CharField(max_length=100, null=True, default='')
    mother_name = models.CharField(max_length=100, null=True, default='')
    address = models.CharField(max_length=200, null=True, default='')
    upload_img = models.ImageField(upload_to='profile_pics/', null=True, blank=True, default='')

    # def __str__(self):
    #     return self.user
