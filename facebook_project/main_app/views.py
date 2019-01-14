from django.shortcuts import render

# Create your views here.

def home(request):
	if request.user.is_authenticated:
		return render(request, 'home.html', {'logged_in': True, 'user': request.user})
	else:
		return render(request, 'home.html', {'logged_in': False})