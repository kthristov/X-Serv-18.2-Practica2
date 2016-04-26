from django.db import models

# Create your models here.

class Urls_List(models.Model) :
	url = models.CharField(max_length=500)

