from fastapi import APIRouter
from datetime import datetime
from database.transferservice import cancel_transfer_my_db, create_transaction_my_db, get_card_transaction_my_db
from transfers import CreateTransferValidator, CancelTransferValidator

transfer_router = APIRouter(prefix='/transaction', tags=['Работа с платежами'])


# Создать новую транзакцию
@transfer_router.post('/create')
async def add_new_transaction(data: CreateTransferValidator):
    transfer_data = data.model_dump()
    result = create_transaction_my_db(**transfer_data)

    return {'message': result}


# Отменить транзакцию
@transfer_router.post('/cancel')
async def cancel_transaction(data: CancelTransferValidator):
    cancel_data = data.model_dump()
    result = cancel_transfer_my_db(**cancel_data)

    return {'message': result}


# Получить историю транзакций
@transfer_router.get('/monitoring')
async def get_card_monitoring(card_id: int):
    result = get_card_transaction_my_db(card_from_id=card_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Нет карты'}





