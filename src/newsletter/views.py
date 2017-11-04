from django.shortcuts import render
from .forms import SignUpForm

# Create your views here.
def home(request):
	if request.method == "POST":
		print(request.POST)
	title = "Welcome"
	if request.user.is_authenticated():
		title = "Welcome %s" %(request.user)
	form = SignUpForm(request.POST or None)

	context = {
		"title" : title,
		"forms" : form
	}

	if form.is_valid():
		instance = form.save(commit=False)
		if not instance.full_name:
			instance.full_name = "Amit"

		instance.save()
		print(instance.email)
		print(instance.timestamp)
		context = {
			"title": "Thank You"
		}
	
	return render(request, 'home.html', context)