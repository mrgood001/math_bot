from aiogram import types


def butn_1():
    '''

    создается клавиатура для команды старт

    '''
    buttons = [
            types.InlineKeyboardButton(text='Задача на проценты, сплавы и смеси', callback_data='smesi'),
            types.InlineKeyboardButton(text='Задача на движение по прямой', callback_data='moving'),
            types.InlineKeyboardButton(text='Задачи на движение по воде', callback_data='water'),
            types.InlineKeyboardButton(text='Задачи на совместную работу', callback_data='work')
        ]
    keybord = types.InlineKeyboardMarkup(row_width=1)
    keybord.add(*buttons)
    return keybord


def butn_2():
    '''
    
    создается вложенная клавиатура для задач про смеси  

    '''
    buttons = [
        types.InlineKeyboardButton(text='Задача про фрукты',callback_data='frut'),
        types.InlineKeyboardButton(text='Задача про смеси', callback_data='smes'),
        types.InlineKeyboardButton(text='Назад',callback_data='start')
    ]
    keybord = types.InlineKeyboardMarkup(row_width=1)
    keybord.add(*buttons)
    return keybord


def back_but():
    keybord = types.InlineKeyboardMarkup()
    butn = types.InlineKeyboardButton(text='Назад',callback_data='back_3')
    keybord.add(butn)
    return keybord


help_command = '''
Список команд:
/help - вывести список комманд
/start - начать работу с ботом
'''

text_hello = '''Привет, я помогу тебе разобраться как решать задачи. 

Выберите нужный тип задач:'''

i_dont_know = 'Я тебя не понял напиши /start'

typ_ze = 'Выберите подтип задачи'