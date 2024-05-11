import uuid
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
          email=self.normalize_email(email),
           
        )

        if password:
            user.set_password(password)
            user.save(using=self._db)
        else:
            user.set_unusable_password()

        return user

    def create_superuser(self, email, password=None):

        # extra_fields = {"is_staff": True, "is_superuser": True}

        user = self.create_user(email=self.normalize_email(email), password=password,
      )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
  id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True, primary_key=True)
  last_name = models.CharField(max_length=100)
  first_name = models.CharField(max_length=100)
  other_name = models.CharField(max_length=100, blank=True, null=True)
  department = models.CharField(max_length=50, null=True)
  email = models.EmailField(max_length=100 ,unique=True)
  # is_acccredited = models.BooleanField(default=False)
  is_voted = models.BooleanField(default=False)
  
  # required fields
  date_joined = models.DateTimeField(auto_now_add=True)
  last_login = models.DateTimeField(auto_now=True)
  is_admin = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  is_superuser = models.BooleanField(default=False)
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []
  objects = UserManager()
  
  class Meta:
    ordering = ["date_joined"]
    
  def __str__(self):
    return self.email
  
  def has_perm(self, perm, obj=None):
    return self.is_admin
  
  def has_module_perms(self, app_label):
    return True

  
  
class HallChairman(models.Model):
  name = models.CharField(max_length=30)
  display_name = models.CharField(max_length=20)
  display_image = models.ImageField(null=True, upload_to="hall_chairman")

  class Meta:
    ordering = ["name"]
  
  def __str__(self):
     return self.display_name
  
class ViceHallChairman(models.Model):
  name = models.CharField(max_length=30)
  display_name = models.CharField(max_length=20)
  display_image = models.ImageField(null=True, upload_to="vice_hall_chairman")

  class Meta:
    ordering = ["name"]

  def __str__(self):
     return self.display_name
  
class GeneralSecretary(models.Model):
  name = models.CharField(max_length=30)
  display_name = models.CharField(max_length=20)
  display_image = models.ImageField(null=True, upload_to="general_secretary")

  class Meta:
    ordering = ["name"]

  def __str__(self):
     return self.display_name
  
class FinancialSecretary(models.Model):
  name = models.CharField(max_length=30)
  display_name = models.CharField(max_length=20)
  display_image = models.ImageField(null=True, upload_to="financial_secretary")

  class Meta:
    ordering = ["name"]

  def __str__(self):
     return self.display_name
  
class InformationMinister(models.Model):
  name = models.CharField(max_length=30)
  display_name = models.CharField(max_length=20)
  display_image = models.ImageField(null=True, upload_to="information_minister")

  class Meta:
    ordering = ["name"]

  def __str__(self):
     return self.display_name
  
class InternalAffairsAndDefenseMinister(models.Model):
  name = models.CharField(max_length=30)
  display_name = models.CharField(max_length=20)
  display_image = models.ImageField(null=True, upload_to="defense_minister")

  class Meta:
    ordering = ["name"]

  def __str__(self):
     return self.display_name
  
class HealthMinister(models.Model):
  name = models.CharField(max_length=30)
  display_name = models.CharField(max_length=20)
  display_image = models.ImageField(null=True, upload_to="health_minister")

  class Meta:
    ordering = ["name"]

  def __str__(self):
     return self.display_name
  
class SportMinister(models.Model):
  name = models.CharField(max_length=30)
  display_name = models.CharField(max_length=20)
  display_image = models.ImageField(null=True, upload_to="sport_minister")
  
  class Meta:
    ordering = ["name"]

  def __str__(self):
     return self.display_name
  
class SocialAndWelfareMinister(models.Model):
  name = models.CharField(max_length=30)
  display_name = models.CharField(max_length=20)
  display_image = models.ImageField(null=True, upload_to="social_minister")

  class Meta:
    ordering = ["name"]

  def __str__(self):
     return self.display_name
  
class StudentRepresentativeCouncil(models.Model):
  name = models.CharField(max_length=30)
  display_name = models.CharField(max_length=20)
  display_image = models.ImageField(null=True, upload_to="src")

  class Meta:
    ordering = ["name"]

  def __str__(self):
     return self.display_name
  