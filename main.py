from aiogram import Bot, Dispatcher, executor, types
import os
from dotenv import load_dotenv
import logging
from text_py.text_smes import text_smes,some_tx
from text_py.text_mov import text_m
from text_py.text_frut import text_fru
from text_py.text_watr import text_waters
from text_py.text_work import text_works
from buttons import butn_1,butn_2, back_but, help_command, text_hello, i_dont_know, typ_ze


load_dotenv('venv/.env')
token = os.getenv('TOKEN')
bot = Bot(token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start'])
async def com_start(message: types.Message):
    await message.answer(text=text_hello, reply_markup=butn_1())

@dp.message_handler(commands=['help'])
async def com_help(message: types.Message):
    await message.answer(text=help_command)


@dp.message_handler(content_types='text')
async def random_text(message):
    await message.answer(text=i_dont_know)

'''
три callback_hendler отвечают занажатие на первую конпу 
и генерацию следующег меню

последние два отвечают за новые две кнопки
'''
@dp.callback_query_handler(text = 'smesi')
async def procent(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=typ_ze, reply_markup=butn_2())


@dp.callback_query_handler(text = 'frut')
async def frut(call: types.CallbackQuery):
    keybord = types.InlineKeyboardMarkup()
    butn = types.InlineKeyboardButton(text='Назад', callback_data='back_2')
    keybord.add(butn)
    await call.message.delete()
    with open('text/frut.txt', 'r', encoding='utf-8') as file:
        text_frut = file.read()
    await call.message.answer(text=text_frut+text_fru, reply_markup=keybord)

@dp.callback_query_handler(text='smes')
async def smes(call: types.CallbackQuery):
    keybord = types.InlineKeyboardMarkup()
    butn = types.InlineKeyboardButton(text='Назад',callback_data='back_1')
    keybord.add(butn)
    with open('text/sm.txt', 'r', encoding='utf-8') as file:
        text_smesi = file.read()
    await call.message.delete()
    await call.message.answer(text_smesi+'\n'+some_tx+text_smes,
                              reply_markup=keybord)

'''

слудеющие три callback_hendler отвечают за кнопки назад 

'''

@dp.callback_query_handler(text='back_1')
async def back_smesi(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=typ_ze, reply_markup = butn_2())
    


@dp.callback_query_handler(text = 'start')
async def back_1(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=text_hello,reply_markup = butn_1())
    

@dp.callback_query_handler(text = 'back_2')
async def back_2(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=typ_ze, reply_markup=butn_2())


@dp.callback_query_handler()
async def mov(call: types.CallbackQuery):
    if call.data == 'moving':
        with open('text/mov.txt', 'r', encoding='utf-8') as file:
            text_mov = file.read()
        await call.message.delete()
        await call.message.answer(text=text_mov+text_m, reply_markup=back_but())
    
    
    elif call.data == 'water':
        with open('text/water.txt', 'r', encoding='utf-8') as file:
            text_water = file.read()
        await call.message.delete()
        await call.message.answer(text=text_water+text_waters, reply_markup=back_but())
    
    
    elif call.data == 'work':
        with open('text/work.txt', 'r', encoding='utf-8') as file:
            text_work = file.read()
        await call.message.delete()
        await call.message.answer(text=text_work+text_works, reply_markup=back_but())
    
    
    elif call.data == 'back_3':
        await call.message.delete()
        await call.message.answer(text=text_hello, reply_markup=butn_1())


if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True)  