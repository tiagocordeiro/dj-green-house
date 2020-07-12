import asyncio

import pyfirmata
from pyfirmata import util

from grow.models import Lampada, Relay

board = pyfirmata.Arduino('/dev/cu.usbmodem14301')


async def smart_irrigation(pin: int, tempo: int):
    board.digital[pin].write(0)
    status = 'on'
    print(F'A porta {pin} está ativa por {tempo} segundos')
    while status == 'on':
        board.digital[pin].write(1)
        await asyncio.sleep(tempo)
        board.digital[pin].write(0)
        print('off')
        status = 'off'

    print('Done')


async def smart_irrigation_v2(pin: int, tempo: int):
    print(F'A porta {pin} está ativa ... {tempo}')
    board.digital[pin].write(1)
    while tempo > 0:
        print('/' * tempo)
        await asyncio.sleep(1)
        tempo -= 1

    board.digital[pin].write(0)
    print('Done')


async def on(pin: int):
    board.digital[pin].write(1)


async def off(pin: int):
    board.digital[pin].write(0)


def get_values():
    lampadas = Lampada.objects.all()
    reles = Relay.objects.all()

    it = pyfirmata.util.Iterator(board)
    it.start()

    lampadas_status = []
    reles_status = []
    for lampada in lampadas:
        try:
            status = board.digital[lampada.pin].read()
            print(status.read())
            item = {'name': lampada.name, 'pin': lampada.pin, 'status': status}
            lampadas_status.append(item)
            print(item)
        except AttributeError:
            pass

    for rele in reles:
        try:
            status = board.digital[rele.pin].read()
            item = {'name': rele.name, 'pin': rele.pin, 'status': status}
            reles_status.append(item)
        except AttributeError:
            pass

    print(lampadas_status)
    print(reles_status)

    return [{'lampadas': lampadas_status, 'reles': reles_status}]
