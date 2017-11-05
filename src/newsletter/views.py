from django.conf import settings
from django.shortcuts import render
from .forms import ContactForm, SignUpForm
from django.core.mail import send_mail

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



def contact(request):

	form = ContactForm(request.POST or None)
	if form.is_valid():
		form_full_name, form_email, form_message  = form.cleaned_data.values()
		print(form_email, form_message, form_full_name)
		subject = 'Site Contact Form'
		from_email = settings.EMAIL_HOST_USER
		contact_message = "%s: \n%s \nvia: %s"%(
				form_full_name,
				form_message,
				form_email
				)
		to_email_list = [form_email]


		send_mail(subject, 
				contact_message, 
				from_email, 
				to_email_list, 
				fail_silently=False)

	context = {
		"forms" : form
	}

	return render(request, "contact.html", context)