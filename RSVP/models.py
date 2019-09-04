from django.db import models

class RSVP(models.Model):
	First_Name = models.CharField(max_length=50, blank=False)
	Family_Name = models.CharField(max_length=50, blank=True)
	Number_Of_Adults = models.PositiveIntegerField()
	Number_Of_Kids = models.PositiveIntegerField()
	Email = models.EmailField()