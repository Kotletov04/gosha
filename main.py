import asyncio
import logging
from aiogram import Bot, Dispatcher, types, filters
from aiogram.filters.command import Command
from aiogram.filters import CommandStart
from aiogram import F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from alive import keep_alive


TOKEN = '6417113837:AAHyPs-QCWdwrI84VmI-Wpkfh0Zk-8jQBmg'



    


DP = Dispatcher()





@DP.message(CommandStart())
async def start_command(message: types.Message):  
    
    buttons = [
        [
            types.KeyboardButton(text='Вопросы'),
            types.KeyboardButton(text='чето другое хз че')
        ],

    ]
    
    markup = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    await message.answer(text='Привет, ебать', reply_markup=markup)



@DP.message(F.text == "Вопросы")
async def question(message: types.Message):
    
    
    inline_buttons = [
        [
            types.InlineKeyboardButton(text="Не понимаю, как принять вагон", callback_data="quest_one"),
        ],
        
        [
            types.InlineKeyboardButton(text="Не понимаю, как принять вагон", callback_data="quest_two"),
        ],

        [
            types.InlineKeyboardButton(text="Не понимаю, как принять вагон", callback_data="quest_three"),
        ],

        [
            types.InlineKeyboardButton(text="Проводник ебется с пассажиркой", callback_data="quest_for"),
        ],

        [
            types.InlineKeyboardButton(text="Я умный", callback_data="quest_five")
        ]
        
    ]
    
    
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=inline_buttons)
    
    await message.answer(text='huy', reply_markup=keyboard)


@DP.callback_query(F.data.startswith("quest_"))
async def callbacks_num(callback: types.CallbackQuery):

    action = callback.data.split("_")[1]

    if action == "one":
        
        await callback.message.edit_text(f"Итого: да хуй его знает")

    elif action == "two":

        await callback.message.edit_text(f"Итого: ваще хз ебать")
    elif action == "three":

        await callback.message.edit_text(f"Итого: пиздец вопрос чел")
    
    elif action == "for":

        await callback.message.edit_text(f"Итого: оооооо бля ну ему пизда черная звезда")

    elif action == "five":

        await callback.message.edit_text(f"Итого: ооооо бля ну тогда олегу поставь физру")

    await callback.answer()





async def main():
    BOT = Bot(TOKEN)
    await DP.start_polling(BOT)




if __name__ == '__main__':
    keep_alive()
    asyncio.run(main())
  