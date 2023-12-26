from django.shortcuts import render
from random import choice

acao = {
    "Beijo", "Cheiro", "Linguada",
    "Linguada lenta", "Tapa",
    "Assoprar", "Arranhar"
    }

local = {
    "Boca", "Pepeca", "Pênis",
    "Atrás da orelha", "Pescoço", "Coxa",
    "Braço", "Nariz", "Orelha",
    "Bunda", "Ânus"
    }

 
def sorteio(request):
    c = choice(seq=acao)
    render(request, )
    
