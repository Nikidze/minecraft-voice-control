import asyncio
import websockets
from autogui import AutoGui

ag = AutoGui()

async def echo(websocket, path):
    async for message in websocket:
        ag.runCommand(message)
start_server = websockets.serve(echo, "192.168.0.13", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()