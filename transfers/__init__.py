from pydantic import BaseModel


# Класс для создания переводов
class CreateTransferValidator(BaseModel):
    card_from: int
    card_tp: int
    amount: float


# Класс для валидации отмены
class CancelTransferValidator(BaseModel):
    card_from: int
    card_to: int
    amount: float
    transfers_id: int
