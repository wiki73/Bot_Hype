from aiogram import F, Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from keyboards import main
from supabase_config import get_recommendations

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет', reply_markup=main)


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Это команда  help')


@router.message(F.text == "Хайповые советы")
async def h_a_y(message: types.Message):
    rec = await get_recommendations()
    for advice in rec:
        await message.answer(advice['body'])

