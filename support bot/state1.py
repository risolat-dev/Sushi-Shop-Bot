from aiogram.fsm.state import State, StatesGroup

class Register(StatesGroup):
    waiting_for_name = State()
    waiting_for_course = State()
    waiting_for_payment = State()
