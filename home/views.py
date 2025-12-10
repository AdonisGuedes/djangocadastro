from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Usuario

def cadastrar(request):
    if request.method == 'GET':
        return render(request, 'cadastrar.html')

    elif request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # Instanciando e salvando
        user = Usuario(email=email, senha=senha)
        user.save()

        return redirect('login')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = Usuario.objects.filter(email=email, senha=senha).first()

        if user:
            return HttpResponse(f'Parabéns usuario de E-mail: {user.email}, Seja Bem-vindo!!')
        else:
            return HttpResponse('Usuário ou senha incorretas!!! Volte e tente novamente')