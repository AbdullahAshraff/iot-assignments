import asyncio
import websockets

async def client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = input("Enter a message: ")
        await websocket.send(message)
        response = await websocket.recv()
        print(f"Server response: {response}")

asyncio.run(client())
