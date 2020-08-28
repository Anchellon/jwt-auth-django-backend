from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name,last_name,username,phone_number,password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
# Now in Django the constructor of a model takes, named parameters, to construct a model instance. 
        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            username=username,
            phone_number=phone_number
           
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

        
    def create_superuser(self, email,first_name,last_name,username,phone_number,password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,first_name,last_name,username,phone_number,
            password=password,
        )
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    
    email = models.EmailField(max_length = 254,unique=True)
    username =  models.CharField(max_length=50,unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    
    #django admin page specifics

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()

    REQUIRED_FIELDS = ['first_name', 'last_name',]
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    def get_full_name(self):
        full_name = self.first_name + " " + self.last_name
        return full_name
    
    def __str__(self):
        full_name = self.first_name + " " + self.last_name
        return full_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

class UserType(models.Model):
    type_of_user = models.CharField(max_length=20)
    def __str__(self):              # __unicode__ on Python 2
        return self.type_of_user