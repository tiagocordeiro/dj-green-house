import asyncio

from django.shortcuts import render, redirect
from django.urls import reverse

from core.facade import smart_irrigation_v2, on, off, get_values
from grow.models import Lampada, Relay


def dashboard(request):
    data = get_values()
    status = 0
    lampadas = Lampada.objects.all()
    reles = Relay.objects.all()

    context = {'status': status,
               'lampadas': lampadas,
               'reles': reles,
               'data': data, }
    return render(request, 'core/dashboard.html', context)


def temporizador(request):
    reles = Relay.objects.all()
    if request.method == "POST":
        tempo = request.POST.get('tempo')
        key = request.POST.get('toggle')
        pin = request.POST.get('pin')
        if key == "ON":
            asyncio.run(smart_irrigation_v2(int(pin), int(tempo)))
            return redirect(reverse('temporizador'))

    context = {'reles': reles}
    return render(request, 'core/temporizador.html', context)


def liga(request, pin: int):
    asyncio.run(on(pin))
    return redirect(reverse('dashboard'))


def desliga(request, pin: int):
    asyncio.run(off(pin))
    return redirect(reverse('dashboard'))
