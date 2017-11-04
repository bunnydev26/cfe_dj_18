from django.contrib import admin
from .models import SignUp
from .forms import SignUpForm

# Register your models here.

class SignUpAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'full_name', 'timestamp', 'updated']
	search_fields = ['full_name',]
	form = SignUpForm
#	class Meta:
#		model=SignUp

admin.site.register(SignUp, SignUpAdmin)