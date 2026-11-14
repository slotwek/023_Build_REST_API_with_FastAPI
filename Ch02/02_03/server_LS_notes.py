import asyncio
from time import sleep

from fastapi import FastAPI

app = FastAPI()

# /sleep/sys - synchronous sleep. It blocks the event loop, preventing other requests from being processed during the sleep duration.
@app.get('/sleep/sys')
def nsys_sleep():
    sleep(1)
    return {'error': None}

# /sleep/async-sys - asynchronous function with synchronous sleep. It still blocks the event loop, similar to the synchronous sleep.
@app.get('/sleep/async-sys')
async def sys_sleep():
    sleep(1)
    return {'error': None}

# /sleep/async-aio - asynchronous function with asynchronous sleep. It allows other requests to be processed during the sleep duration.
@app.get('/sleep/async-aio')
async def aio_sleep():
    await asyncio.sleep(1)
    return {'error': None}

