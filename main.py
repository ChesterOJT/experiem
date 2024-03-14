import asyncio
import serial
import websockets
import json

ser = serial.Serial('COM5', 9600)  # Update ttyACM0 to your Arduino serial port

async def send_data(websocket, path):
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            voltage = float(line.split(":")[1].strip())
            await websocket.send(json.dumps({'voltage': voltage}))
            await asyncio.sleep(1)

start_server = websockets.serve(send_data, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
