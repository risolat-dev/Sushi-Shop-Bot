from aiogram import Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from state1 import Register
from service_logicbot import update_user_progress, check_course_exists, get_user_current_course
from user_keyboard import next_lesson_keyboard
from database1 import courses

def register_user_handlers(dp: Dispatcher):

    @dp.message(CommandStart())
    async def start_handler(message: Message, state: FSMContext):
        await message.answer("Salom! Ismingizni kiriting:")
        await state.set_state(Register.waiting_for_name)

    @dp.message(Register.waiting_for_name)
    async def name_handler(message: Message, state: FSMContext):
        await state.update_data(name=message.text)
        await message.answer(
            f"Rahmat, {message.text}! Qaysi kursni xohlaysiz?\n- Java\n- JavaScript\n- Python"
        )
        await state.set_state(Register.waiting_for_course)

    @dp.message(Register.waiting_for_course)
    async def course_handler(message: Message, state: FSMContext):
        user_data = await state.get_data()
        name = user_data.get("name")
        course_name = message.text
        course = check_course_exists(course_name)
        if not course:
            await message.answer("Bunday kurs mavjud emas ❌")
            return

        if course["paid"]:
            await state.update_data(course=course_name)
            await message.answer(f"{name}, {course_name} kursi pullik. Shunchaki 'tasdiqlash' deb yozing ✅")
            await state.set_state(Register.waiting_for_payment)
        else:
            lesson_text, finished = update_user_progress(message.from_user.id, course_name)
            if finished:
                await message.answer(f"{name}, siz {course_name} kursini tugatdingiz! 🎉")
                await state.clear()
            else:
                await message.answer(lesson_text, reply_markup=next_lesson_keyboard())
                await state.set_state(Register.waiting_for_course)

    @dp.message(Register.waiting_for_payment)
    async def payment_simulation(message: Message, state: FSMContext):
        if message.text.lower() == "tasdiqlash":
            user_data = await state.get_data()
            course_name = user_data.get("course")
            lesson_text, finished = update_user_progress(message.from_user.id, course_name)
            if finished:
                await message.answer(f"{course_name} kursini tugatdingiz! 🎉")
                await state.clear()
            else:
                await message.answer(lesson_text, reply_markup=next_lesson_keyboard())
                await state.set_state(Register.waiting_for_course)
        else:
            await message.answer("To‘lovni tasdiqlash uchun 'tasdiqlash' deb yozing.")

    @dp.callback_query(lambda c: c.data == "next_lesson")
    async def next_lesson_callback(callback: CallbackQuery):
        user_id = callback.from_user.id
        course_name = get_user_current_course(user_id)
        if not course_name:
            await callback.message.answer("Siz hozirda kursni tanlamadingiz ❌")
            return
        lesson_text, finished = update_user_progress(user_id, course_name)
        if finished:
            await callback.message.answer(f"{course_name} kursini tugatdingiz! 🎉")
        else:
            await callback.message.answer(lesson_text, reply_markup=next_lesson_keyboard())
