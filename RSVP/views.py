from django.shortcuts import render, redirect
from .models import RSVP
from django.http import HttpResponseRedirect
from .forms import RSVPFamily
from django.contrib import auth
import jobs.views
from django.core.mail import send_mail


def send_email_to_guest(First_name, Email):
	send_mail(First_name + ", Thanks for submitting your RSVP", "Hello " + First_name + ",\n\nThanks for registering your RSVP. We are very excited that you can make it Abeer's birthday party and so is Abeer. We look forward to seeing you on 26th October 2019 @ 12.30 PM at Parramatta Reserve", 'abeer@mail.sumanshuarora.com', [Email], fail_silently=False)


def send_email_to_host(First_name, Family_Name, Adults, Kids, Email):
	send_mail(First_name + ' ' + Family_Name + " has submitted RSVP for Abeer's 3rd birthday", First_name + ' ' + Family_Name + " shall be arriving with " + str(Adults) + "and " + str(Kids) + ". A confirmation email has been sent to them. Database entry has been registered.", 'abeer@mail.sumanshuarora.com', ['sumanshusamarora@gmail.com'], fail_silently=False)
	send_email_to_guest(First_name, Email)


# Create your views here.
def InputRSVPFamily(request):
	if request.method == 'POST':
		form_RSVP=RSVPFamily(request.POST, request.FILES)
		if form_RSVP.is_valid():
			form_RSVP.save()
			send_email_to_host(request.POST["First_Name"], request.POST["Family_Name"], request.POST["Number_Of_Adults"], request.POST["Number_Of_Kids"], request.POST["Email"])
			return redirect(jobs.views.home)
	else:
		form_RSVP = RSVPFamily()
	return render(request, 'RSVP/rsvp_family.html', {'form' : form_RSVP})