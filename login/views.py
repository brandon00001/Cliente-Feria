from django.shortcuts import render
from .models import *
from .forms import UCFCompleted
import requests
from django.http import HttpResponseRedirect


from django.contrib.auth import login as do_login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def CrearUsuario(request):
	form = UCFCompleted()

	if request.method == "POST":
		form = UCFCompleted(request.POST)
		nombre = form.data['first_name']
		apellido = form.data['last_name']
		usern = form.data['username']
		correo = form.data['email']
		passwd = form.data['password1']
		payload = {"first_name": nombre,
				   "last_name": apellido,
				   "username": usern,
				   "email": correo,
				   "password": passwd
				   }
		r = requests.post('http://letalisumbra.pythonanywhere.com/api/1.0/create_user/', json=payload)
		return HttpResponseRedirect('login.html')

	return render(request, 'register.html', {"form": form})

def login(request):
	# codigo para el formulario del login con autenticación
	login_form = AuthenticationForm()
	if request.method == "POST":
		login_form = AuthenticationForm(data=request.POST)
		if login_form.is_valid():
			username = login_form.cleaned_data['username']
			password = login_form.cleaned_data['password']
			user = authenticate(username=username, password=password)

			if user is not None:
				do_login(request, user)
				return HttpResponseRedirect('http://letalisumbra.pythonanywhere.com')

	return render(request, 'login.html', {'form': login_form})