from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# class UserManager(BaseUserManager):
#     def create_user(self, name, email, password=None, register_as=None):
#         if not email:
#             raise ValueError('Users must have an email address')
#         user = self.model(
#             email=self.normalize_email(email),
#             name=name,
#             register_as=register_as,  # Include the register_as field
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, name, email, password):
#         user = self.create_user(
#             email=self.normalize_email(email),
#             name=name,
#             password=password,
#             register_as='contractor',  # Set register_as to 'contractor' for superuser
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.save(using=self._db)
#         return user


# class User(AbstractBaseUser):
#     CUSTOMER = 1
#     CONTRACTOR = 2
#     REGISTER_CHOICES = (
#         ('customer', 'Customer'),
#         ('contractor', 'Contractor')
#     )
#     id=models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100, unique=True)
#     register_as = models.CharField(max_length=20, choices=REGISTER_CHOICES, blank=False)

#     # Required fields
#     date_joined = models.DateTimeField(auto_now_add=True)
#     last_login = models.DateTimeField(auto_now=True)
#     is_admin = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)  # Default to True for simplicity

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']

#     def __str__(self):
#         return self.email

class extendeduser(models.Model):
     CUSTOMER = 1
     CONTRACTOR = 2
     REGISTER_CHOICES = (
        ('customer', 'Customer'),
        ('contractor', 'Contractor')
     )
     register_as = models.CharField(max_length=20, choices=REGISTER_CHOICES, blank=False)
     company_name = models.CharField(max_length=100)
     contractor_name = models.CharField(max_length=100)
     gstin = models.CharField(max_length=15)
     location = models.CharField(max_length=100)
     city = models.CharField(max_length=100)
     projects_completed = models.IntegerField()
     experience_years = models.IntegerField()
     contractor_occupation=models.CharField(max_length=30)
    
class User(models.Model)
    userid=models.ForeignKey(extendeduser, on_delete=models.CASCADE)

    

class contractor(models.Model):
    
    company_name = models.CharField(max_length=100)
    contractor_name = models.CharField(max_length=100)
    gstin = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    projects_completed = models.IntegerField()
    experience_years = models.IntegerField()
    contractor_occupation=models.CharField(max_length=30)



class ConnectedUsersToContractor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contractor = models.ForeignKey(contractor, on_delete=models.CASCADE)
    
    
   
   