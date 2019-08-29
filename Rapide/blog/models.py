from django.db import models

from django.contrib.auth.models import User 

from datetime import datetime,date 
# Create your models here.

class Fichier(models.Model):

	title = models.CharField(max_length=200)

	content = models.TextField()

	citoyen = models.ManyToManyField(User)

	picture = models.ImageField(upload_to='profile_pics')
	def __str__(self):
		return self.title
		

class Profile(models.Model):
	
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	
	image=	models.ImageField(default='default.jpg',upload_to='profile_pics') 
	
	Nom = models.CharField(max_length=200)

	Prenom = models.CharField(max_length=200)

	Date_de_naissance = models.DateField('Puchase(mm/dd/yy)',auto_now_add=False,auto_now =False,blank=True)

	lieu_Naissance = models.CharField(max_length=200)

	Adresse = models.CharField(max_length=200)

	def __str__(self):
	
		return f'{self.user.username} Profile'
	