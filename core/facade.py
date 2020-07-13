import asyncio

import pyfirmata
from pyfirmata import util

from grow.models import Lampada, Relay

board = pyfirmata.Arduino('/dev/cu.usbmodem14301')

it = pyfirmata.util.Iterator(board)
it.start()

sensor_lm35 = board.get_pin('a:0:i')


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

    lampadas_status = []
    reles_status = []

    temperatura = sensor_lm35.read()

    # sensor_lm35 = board.analog[0].read()
    for lampada in lampadas:
        try:
            status = board.digital[lampada.pin].read()
            item = {'name': lampada.name, 'pin': lampada.pin, 'status': status}
            lampadas_status.append(item)
        except AttributeError:
            print('não existe')
            pass
        except IndexError:
            print('não existe')
            pass

    for rele in reles:
        try:
            status = board.digital[rele.pin].read()
            item = {'name': rele.name, 'pin': rele.pin, 'status': status}
            reles_status.append(item)
        except AttributeError:
            print('não existe')
            pass
        except IndexError:
            print('não existe')
            pass

    print(lampadas_status)
    print(reles_status)
    print(temperatura * 0.48828125 * 1000)

    return {'lampadas': lampadas_status,
            'reles': reles_status,
            'sensores': temperatura * 0.48828125 * 1000}
