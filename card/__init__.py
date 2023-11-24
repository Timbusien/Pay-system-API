from pydantic import BaseModel


class AddUserCard(BaseModel):
    user_id: int
    card_number: int
    balance: int
    exp_date: int
    card_name: str


class EditUserCard(BaseModel):
    card_id: int
    new_data: str
    edit_type: str

