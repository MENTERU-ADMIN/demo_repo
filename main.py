from fastapi import FastAPI
import uvicorn


# use fastapi to create a web server
def create_app():
    app = FastAPI()
    return app


app = create_app()


@app.get("/")
async def root():
    return {"message": "Welcome to MENTERU Company Application"}


# Run the server
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8800)
