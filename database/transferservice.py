from datetime import datetime
from database.models import Transfer, UserCard
from database import get_database


# Проверка банковской карты
def validate_card(card_number, my_db):
    exact_card = my_db.query(UserCard).filter_by(card_number=card_number).first()

    return exact_card


# Создание транзакций
def create_transaction_my_db(card_from, card_to, amount):
    my_db = next(get_database())
    # Проверка на наличие кард в базе данных
    check_card_from = validate_card(card_from, my_db)
    check_card_to = validate_card(card_to, my_db)

    # Есть ли карты в базе данных
    if check_card_from and check_card_to:
        # Проверка баланса
        if check_card_from.balance >= amount:
            # минусуем у отправителя
            check_card_from.balance -= amount
            # Добавляем получателю
            check_card_to.balance += amount

            # Сохраняем платёж в базе данных
            new_transaction = Transfer(card_from_id=check_card_from.card_id,
                                       card_to_id=check_card_to.card_id,
                                       amount=amount,
                                       transaction_date=datetime.now())
            my_db.add(new_transaction)
            my_db.commit()
            return 'Перевод успешно выполнен'
        else:
            return 'Недостаточно средств на карте'
    else:
        return 'Одна из карт не существует'


# Получить все переводы по карте
def get_card_transaction_my_db(card_from_id):
    my_db = next(get_database())

    card_transaction = my_db.query(Transfer).filter_by(card_from_id=card_from_id).all()
    return card_transaction


# Отменить перевод
def cancel_transfer_my_db(card_from, card_to, amount, transfer_id):
    my_db = next(get_database())
    check_card_from = validate_card(card_from, my_db)
    check_card_to = validate_card(card_to, my_db)

    # Есть ли карты в базе данных
    if check_card_from and check_card_to:
        # Проверка баланса возвратителя
        if check_card_from.balance >= amount:
            # минусуем у отправителя
            check_card_from.balance += amount
            # Отнимаем операцию тому кто получал до этого
            check_card_to.balance -= amount

            # Сохраняем платёж в базе данных
            exact_transaction = my_db.query(Transfer).filter_by(transfer_id=transfer_id).first()
            exact_transaction.status = False
            my_db.commit()
            return 'Перевод успешно отменён'
        else:
            return 'Недостаточно средств на карте'
    return 'Одна из карт не существует'




