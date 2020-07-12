import asyncio

import pyfirmata
from django.shortcuts import render, redirect
from django.urls import reverse

from core.facade import smart_irrigation_v2

board = pyfirmata.Arduino('/dev/cu.usbmodem14301')


def dashboard(request):
    status = board.digital[13].read()
    if request.method == "POST":
        tempo = request.POST.get('tempo')
        key = request.POST.get('toggle')
        if key == "ON":
            asyncio.run(smart_irrigation_v2(13, int(tempo)))
            return redirect(reverse('dashboard'))

        if key == "OFF":
            board.digital[13].write(0)
            return redirect(reverse('dashboard'))

    context = {'status': status}
    return render(request, 'core/dashboard.html', context)


def liga(request, pin: int):
    board.digital[pin].write(1)
    return redirect(reverse('dashboard'))


def desliga(request, pin: int):
    board.digital[pin].write(0)
    return redirect(reverse('dashboard'))
