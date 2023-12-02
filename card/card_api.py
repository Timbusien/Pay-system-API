from card import AddUserCard, EditUserCard
from fastapi import APIRouter
from database.cardservice import (edit_card_my_db, add_card_my_db, get_exact_user_cards_my_db,
                                  check_card_my_db, delete_card_my_db)

card_router = APIRouter(prefix='/card', tags=['Работа с картами'])


@card_router.post('/add-card')
async def add_card(data: AddUserCard):
    result = add_card_my_db(**data.model_dump())

    return {'message': result}


@card_router.get('/get-users-card')
async def get_exact_user_card(user_id: int):
    result = get_exact_user_cards_my_db(user_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Карта пользователя не найдена'}


@card_router.get('/check-card')
async def check_card(card_number: int):
    result = check_card_my_db(card_number)

    if result:
        return {'message': result}
    else:
        return {'message': 'Карты с таким номером не существует'}


@card_router.put('/edit-card')
async def edit_card(data: EditUserCard):
    change_card = data.model_dump()
    result = edit_card_my_db(**change_card)

    if result:
        return {'message': result}
    else:
        return {'message': 'Карты не существует'}


@card_router.delete('/delete-card')
async def delete_card(card_id: int):
    result = delete_card_my_db(card_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Карты не существует'}




