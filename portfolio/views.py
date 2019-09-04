from django.shortcuts import render

# Create your views here.
def allcaptions(request):
	return render(request, "allcaptions/allcaptions.html")