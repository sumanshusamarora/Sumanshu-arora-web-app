from django.shortcuts import render, redirect
from .models import Job
from django.http import HttpResponseRedirect
from .forms import ImageUpload
from django.contrib import auth

def home(request):
	jobobjects = Job.objects.all().order_by('-id')

	return render(request, 'jobs/home.html', {'jobobjects':jobobjects})

def uploadpicture(request):
	return render(request, 'jobs/picture-upload-form.html')

def InputImageEntry(request):
	if request.method == 'POST':
		form=ImageUpload(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect(home)
	else:
		form = ImageUpload()
	return render(request, 'jobs/picture-upload-form.html', {'form' : form})