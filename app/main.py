from fastapi import FastAPI
from app.routes.rpn_router import router


app = FastAPI(
    title="RPN Calculator",
    description="A simple Reverse Polish Notation (RPN) calculator API",
    version="1.0.0")

app.include_router(router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

