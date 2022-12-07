from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .service.User import UserService
from .utils.utils import is_empty_form, fill_form_values

def index(request):
    return render(request, 'index.html')

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

class CotizarView(View):
    def __init__(self):
        # Ejemplo de como podriamos enviar al template los datos que queremos mandar para cotizar
        self._fields = {
            'fields': [
                { 'name': 'Nombre', 'required': True },
                { 'name': 'Apellido', 'required': True },
            ]
        }

    def get(self, request):
        return render(request, 'cotizacion/index.html', self._fields)
    
    def post(self, request):
        # Este metodo deberia llamarse cuando el form no esta bien completado 
        # y dejarlo con los valores que puso el cliente
        filled_form = fill_form_values(self._fields, request.POST) 
        return render(request, 'cotizacion/index.html', filled_form)

def logoutView(request):
    logout(request)
    return redirect('/')