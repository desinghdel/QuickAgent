import asyncio
import websockets
import pyaudio
import certifi
import ssl

# Replace with your actual Deepgram API key
api_key = 'YOUR_ACTUAL_API_KEY'

# Function to handle received data
async def handle_data(data):
    print(data)

# Function to connect to Deepgram WebSocket
async def connect():
    ssl_context = ssl.create_default_context(cafile=certifi.where())

    async with websockets.connect(
        'wss://api.deepgram.com/v1/listen',
        extra_headers={
            'Authorization': f'Token {api_key}',
            'Upgrade': 'websocket',
            'Connection': 'Upgrade'
        },
        ssl=ssl_context
    ) as websocket:
        await websocket.send('{"type": "start"}')
        while True:
            data = await websocket.recv()
            await handle_data(data)

# Initialize PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)

# Function to send audio data
async def send_audio():
    ssl_context = ssl.create_default_context(cafile=certifi.where())

    async with websockets.connect(
        'wss://api.deepgram.com/v1/listen',
        extra_headers={
            'Authorization': f'Token {api_key}',
            'Upgrade': 'websocket',
            'Connection': 'Upgrade'
        },
        ssl=ssl_context
    ) as websocket:
        await websocket.send('{"type": "start"}')
        while True:
            data = stream.read(1024)
            await websocket.send(data)

# Run the connection and audio sending concurrently
async def main():
    await asyncio.gather(connect(), send_audio())

# Execute the main function
asyncio.run(main())
