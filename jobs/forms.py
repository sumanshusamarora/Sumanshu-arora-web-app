from django import forms
from .models import Job

class ImageUpload(forms.ModelForm):
	class Meta: 
		model = Job
		fields = ('image', 'summary',)