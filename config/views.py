from django.shortcuts import redirect

def home(request):
    """Redireciona raiz para o frontend"""
    return redirect('/frontend/index.html')
