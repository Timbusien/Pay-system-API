from fastapi import FastAPI
from user.user_api import user_router
from transfers.transfers_api import transfer_router
from card.card_api import card_router
from database import Base, engine

app = FastAPI(docs_url='/')
app.include_router(user_router)
app.include_router(transfer_router)
app.include_router(card_router)

# Создаём базу данных
Base.metadata.create_all(bind=engine)


@app.get('/home')
async def home():
    return {'message': 'This is message'}

