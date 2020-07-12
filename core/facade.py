import asyncio

import pyfirmata

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



