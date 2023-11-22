from datetime import datetime
from database.models import User
from database import get_database


# Регистрация пользователей
def register_user_my_db(name, surname, email, number, password, city):
    my_db = next(get_database())
    new_user = User(name=name,
                    surname=surname,
                    email=email,
                    number=number,
                    password=password,
                    city=city,
                    reg_date=datetime.now())
    my_db.add(new_user)
    my_db.commit()

    return 'Пользователь был успешно зарегистрирован'


# Получение информации о пользователе
def get_exact_user_my_db(user_id):
    my_db = next(get_database())
    exact_user = my_db.query(User).filter_by(user_id=user_id).first()

    return exact_user


# Проверка личных данных
def check_user_email_my_db(email):
    my_db = next(get_database())
    check = my_db.query(User).filter_by(email=email).first()

    if check:
        return check
    else:
        return 'Такой почты нет!'


# Изменить данные у пользователя
def edit_user_my_db(user_id, edit_type, new_data):
    my_db = next(get_database())
    exact_user = my_db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        if edit_type == 'email':
            exact_user.email = new_data
        elif edit_type == 'password':
            exact_user.password = new_data
        elif edit_type == 'city':
            exact_user.city = new_data
        elif edit_type == 'name':
            exact_user.name = new_data
        elif edit_type == 'surname':
            exact_user.surname = new_data
        elif edit_type == 'number':
            exact_user.number = new_data

        my_db.commit()

        return 'Данные успешно изменены!'

    else:
        return 'Пользователь не найден!'


def delete_user_my_db(user_id):
    my_db = next(get_database())

    delete_user = my_db.query(User).filter_by(user_id=user_id).first()

    if delete_user:
        my_db.delete(delete_user)
        my_db.commit()

        return 'Пользователь был успешно удалён!'
    else:
        return 'Пользователь не найден!'


