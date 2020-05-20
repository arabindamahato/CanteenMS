from django.db import models

from django.contrib.auth.models import (
		BaseUserManager, AbstractBaseUser
	)
from django.utils.translation import gettext_lazy as _



class UserManager(BaseUserManager):
	def create_user(self, email, password=None):
		if not email:
			raise ValueError(_('Users must have an email address'))
		# if not first_name:
		# 	raise ValueError(_('Users must have a first name'))
		# if not last_name:
		# 	raise ValueError(_('Users must have a last name'))
	    
		user = self.model(
			email=self.normalize_email(email),
			# first_name=first_name,
			# last_name=last_name,
			)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password):
		"""
		Create and saves a superuser with the given email, 
		firstname, lastname, and password . 
		"""
		user = self.create_user(
			email=email,
			# first_name=first_name,
			# last_name=last_name,
			password=password,

    	)

		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class User(AbstractBaseUser):
	GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    )
	email = models.EmailField(unique=True, blank=False, null=False)
	contact_no = models.CharField(max_length=10, blank=True, null=True)
	first_name = models.CharField(_('first name'), max_length=30, blank=True)	
	last_name = models.CharField(_('last name'), max_length=150, blank=True)  
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	date_joined = models.DateTimeField(auto_now_add=True)
	gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES, blank=True, null=True)
    
	objects = UserManager()
	groups = models.ManyToManyField('auth.Group')

	USERNAME_FIELD = "email"
	# REQUIRED_FIELDS = ['first_name', 'last_name']

	def __str__(self):
		return self.first_name + " | " + self.email



	def has_perm(self, perm, obj=None):
		user_perms = []
		if self.is_staff:
			groups = self.groups.all()
			for group in groups:
				perms = [("{0}.{1}".format(x.content_type.app_label, x.codename)) for x in group.permissions.all()]
				user_perms += perms

			if perm in user_perms:
				return True
		return (self.is_admin or self.is_superuser)

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		return True