from django.shortcuts import render
from django.shortcuts import redirect
from .models import Lanche
from .forms import LancheForm 

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

def login_view(request):
    return render(request, 'Login.html')

def conta_view(request):
    return render(request, 'cadas.html')

