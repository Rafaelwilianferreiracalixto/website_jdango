from django.shortcuts import render

# Create your views here.

def desing_ltda_index(request):
    return render (
        request,
        "index.html"
    )

def desing_ltda_elementos_design(request):
    return render (
        request,
        "elementos_design.html" 
        )

def desing_ltda_contatos(request):
    return render (
        request,
        "contatos.html"
        )