# This is a simple FastAPI server that returns a health check response.
# The code runs as python server.py and can be accessed at http://
# Example: python server.py

# There is an option to pick which version of uvicorn to run the server in production or debugging mode.
from fastapi import FastAPI

app = FastAPI()


@app.get('/health')
def health():
    return {'errors': "test"}

if __name__ == '__main__':
    import uvicorn

    # Production mode
    # uvicorn.run(app)
    
    # Debugging mode
    uvicorn.run("server:app", reload=True)