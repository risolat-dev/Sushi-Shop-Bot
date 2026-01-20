from aiogram import Router, types
from config1 import ADMIN_ID
from admin_keyboard import admin_keyboard
from database1 import user_progress, courses, courses_lessons

router = Router()

def register_admin_handlers(dp):
    dp.include_router(router)

@router.message(lambda m: m.text == "/admin")
async def admin_menu(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        await message.answer("Siz admin emassiz ❌")
        return
    await message.answer("Admin panel", reply_markup=admin_keyboard())

@router.message(lambda m: m.text == "Kurslar ro‘yxati")
async def show_courses(message: types.Message):
    text = "Kurslar:\n"
    for c in courses:
        status = "Pullik" if c.get("paid") else "Bepul"
        text += f"{c['name']} — {status}\n"
    await message.answer(text)

@router.message(lambda m: m.text == "User progress")
async def show_progress(message: types.Message):
    if not user_progress:
        await message.answer("Hozircha user progress yo‘q ❌")
        return
    text = "User progress:\n"
    for uid, data in user_progress.items():
        text += f"\nUser {uid}:\n"
        for course_name, idx in data.items():
            total = len(courses_lessons.get(course_name, []))
            text += f"{course_name}: {idx}/{total} darslar\n"
    await message.answer(text)
