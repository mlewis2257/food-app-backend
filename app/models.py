from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User 


# Create your models here.
class Food(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
    
class newFood(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title


# class User(AbstractUser): 
#     email = models.EmailField(unique=True, max_length=50)
     
#     #ROLES 
#     COMPANY_ADMIN = 1 
#     RESTAURANT_ADMIN = 2 
#     COMPANY_EMPLOYEE = 3
#     DISPATCHER = 4 
#     ROLE_CHOICES = (
#         (COMPANY_ADMIN, "COMPANY_ADMIN"),
#         (RESTAURANT_ADMIN, "RESTAURANT_ADMIN"),
#         (COMPANY_EMPLOYEE, "COMPANY_EMPLOYEE"),
#         (DISPATCHER, "DISPATCHER")
#     )

#     role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=3)

#     def __str_(self): 
#         return self.email

