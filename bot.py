import string
import time

import main
import json

from main import SUPERUSER_IDS
from filter import IsAdminFilter

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher, filters

bot = Bot(token=main.TOKEN)
dp = Dispatcher(bot)

dp.filters_factory.bind(IsAdminFilter)


# greetings a new user
@dp.message_handler(content_types=["new_chat_members"])
async def new_member(message: types.Message):
    for new_member in message.new_chat_members:
        me = await bot.get_me()
    await message.answer(f'Приветствуем нового пользователя - {new_member.first_name}! \nЯ @{me.first_name}, и я '
                         f'здесь главный, после @JokermanMM.'
                         f'\nПеред началом общения в этом чате, я советую тебе прочитать правила чата. Список правил ты'
                         f' можешь получить используя команду: /rules\nДля начала взаимодействия со мной ты можешь '
                         f'воспользоваться командой: /start \nGood luck, have fun')


# /start reply
"""@dp.message_handler(filters.CommandStart())
async def command_start_handler(msg: types.Message):
    await msg.answer(f"Привет. Я @{me.first_name}, и я могу тебе что-нибудь подсказать. Что тебя интересует ?")"""


@dp.message_handler(commands='start')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    text_and_data = (
        ('База от админа (ﾉ◕ヮ◕)ﾉ', 'yes'),
        ('Сам справлюсь ᕦ(ò_óˇ)ᕤ', 'no'),
    )

    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)

    keyboard_markup.row(*row_btns)
    keyboard_markup.add(
        types.InlineKeyboardButton('Dotabuff админа', url='https://ru.dotabuff.com/players/299539763'),
    )

    me = await bot.get_me()
    await message.reply(f"Привет. Я @{me.first_name}, и я могу тебе что-нибудь подсказать. Что тебя интересует ?",
                        reply_markup=keyboard_markup)


@dp.callback_query_handler(text='no')
@dp.callback_query_handler(text='yes')
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    answer_data = query.data

    await query.answer(f'You answered with {answer_data!r}')

    if answer_data == 'yes':
        text = 'Одноразовая ссылка!\nhttps://disk.yandex.ru/i/BkLZ8Nuy3iwhlg'

    elif answer_data == 'no':
        text = 'А, ннну давай'
    else:
        text = f'Unexpected callback data {answer_data!r}!'

    await bot.send_message(query.message.chat.id, text)


# echo function
"""@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)"""


# get rules list
@dp.message_handler(commands=["rules"], commands_prefix="/")
async def rules(message: types.Message):
    await message.reply(f'Правила чата:\n1. Запрещен мат.\n2. Это просто тестирование функционала, поэтому правила чата'
                        f' будут постепенно дополняться с дополнением функционала бота. \nEnjoy!')


# ban function
@dp.message_handler(is_admin=True, commands=["ban"], commands_prefix="!/")
async def ban(message: types.Message):
    if not message.reply_to_message:
        await message.reply('Эта команда должна применяться ответом на сообщение')
        return

    await bot.kick_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
    await message.delete()

    await message.reply_to_message.reply('VAC!')


@dp.message_handler(text='!ban')
async def re_ban(message: types.Message):
    await message.reply('Ты кто такой, чтоб это делать ?')

    time.sleep(2)
    await message.answer('3')
    time.sleep(1)
    await message.answer('2')
    time.sleep(1)
    await message.answer('1')
    time.sleep(1)
    await message.answer('HAHAHAHA')
    time.sleep(0.2)
    await bot.kick_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)


# bad words list
@dp.message_handler()
async def ban_words(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
            .intersection(set(json.load(open('banwords.json')))) != set():
        await message.answer('Сообщение было автоматически удалено.\nПричина: использование нецензурной лексики '
                             'в чате запрещено!')
        await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
