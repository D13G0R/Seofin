from fastapi import FastAPI


from app.users.router import router as userRouter
from app.accounts.router import router as accountRouter

app = FastAPI()

app.include_router(userRouter)

app.include_router(accountRouter)


@app.get("/")
def home():
    return {"message": "Hello World"}








