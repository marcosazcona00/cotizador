from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .service.User import UserService
from .utils.utils import is_empty_form

def index(request):
    return render(request, './index.html')

class RegisterView(View):
    def get(self, request):
        if (request.user.is_authenticated):
            return redirect('/')
        return render(request, 'user/register.html')

    def post(self, request):
        if is_empty_form(request.POST):
            return render(request, 'user/register.html', { 'failure_label': 'Formulario Vacio' })

        [email, password] = [request.POST.get('email'), request.POST.get('password')]
        user_service = UserService()
        user = user_service.find_user_by_email(request.POST.get('email'))
        if (user):
            return render(request, 'user/register.html', { 'failure_label': 'El usuario ya existe' })
        
        user_service.register_user(email, password)
        return redirect('/')

class LoginView(View):
    def get(self, request):
        return render(request, 'user/login.html')

    def post(self, request):
        if is_empty_form(request.POST):
            return render(request, 'user/login.html', { 'failure_label': 'Formulario Vacio' })

        [email, password] = [request.POST.get('email'), request.POST.get('password')]
        user = authenticate(request, username = email, password = password)
        print(user)
        if (user == None):
            return render(request, 'user/register.html', { 'failure_label': 'Datos incorrectos' })
        
        login(request, user)
        return redirect('/')

def logoutView(request):
    logout(request)
    return redirect('/')