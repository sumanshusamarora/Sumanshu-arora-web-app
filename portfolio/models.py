from django.db import models

class Portfolio(models.Model):
	title = models.CharField(max_length=150)
	pub_date = models.DateField(auto_now=False, auto_now_add=False)
	body = models.CharField(max_length=1500)
	portfolio_image = models.ImageField(upload_to = 'PortfolioImages/')
