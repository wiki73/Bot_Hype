from aiogram import F, Router,types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from Lesson_1.app.keyboards import main
from dotenv import load_dotenv
import os
from supabase import create_client, Client
load_dotenv()
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)
router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет', reply_markup=main)


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Это команда  help')


@router.message(F.text == "Хайповые советы")
async def h_a_y(message: types.Message):
    response = supabase.table('recommendations').select("*").execute()
    text = response.data
    await message.answer(str(text))

