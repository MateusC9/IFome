from django.shortcuts import render, redirect
from .models import Lanche
from .forms import LancheForm 
from .user_forms import CustomUserCreationForm  # Importa o novo formulário
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def conta_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['senha'])  # Define a senha corretamente
            user.save()
            messages.success(request, 'Conta criada com sucesso! Faça o login.')
            return redirect('login')  # Redireciona para a página de login
        else:
            messages.error(request, 'Erro ao criar conta. Verifique as informações.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'cadas.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('ifome')  # Redireciona para a página inicial
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
        else:
            messages.error(request, 'Erro ao processar o formulário.')
    else:
        form = AuthenticationForm()

    return render(request, 'Login.html', {'form': form})


def ifome(request):
    return render(request, 'IFome.html')

def cadastrar(request):
    return render(request, 'cadastrar.html')

def home(request):
    lanches = Lanche.objects.all()
    return render(request, "IFome.html", {"lanches": lanches})

def salvar(request):
    if request.method == 'POST':
        form = LancheForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ifome')
    else:
        form = LancheForm()

    lanches = Lanche.objects.all()
    return render(request, 'IFome.html', {'form': form, 'lanches': lanches})
