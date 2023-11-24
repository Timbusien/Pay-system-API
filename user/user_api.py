from fastapi import APIRouter
from datetime import datetime
from database.userservice import register_user_my_db, delete_user_my_db, edit_user_my_db, get_exact_user_my_db, check_user_email_my_db
from user import UserRegisterValidator, EditUserValidator

user_router = APIRouter(prefix='/user', tags=['Работа с пользователями'])


# Регистрация
@user_router.post('/register')
async def register_user(data: UserRegisterValidator):
    # Преобразуем pydantic в словарь
    new_user = data.model_dump()
    # Вызов функции для проверки функции
    check = check_user_email_my_db(data.email)

    if not check:
        return {'message': 'Пользователь с такой почтой уже существует'}
    else:
        result = register_user_my_db(reg_date=datetime.now(), **new_user)
        return {'message': result}


# Получение пользователя
@user_router.get('/info')
async def get_user(user_id: int):
    result = get_exact_user_my_db(user_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Такого пользователя не существует'}


# Изменить данные о пользователе
@user_router.put('/edit-data')
async def edit_user(data: EditUserValidator):
    change_data = data.model_dump()
    result = edit_user_my_db(**change_data)

    if result:
        return {'message': change_data}
    else:
        return {'message': 'Такой пользователь не существует'}


# Удаление пользователя
@user_router.delete('/delete-user')
async def delete_user(user_id: int):
    result = delete_user_my_db(user_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Такой пользователь не существует'}




