from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    create_password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    
