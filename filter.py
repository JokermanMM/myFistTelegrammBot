from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsAdminFilter(BoundFilter):
    key = "is_admin"

    def __init__(self, is_admin):
        self.is_admin = is_admin

    async def check(self, message: types.Message):
        member = await message.bot.get_chat_member(message.chat.id, message.from_user.id)
        return member.is_chat_admin()


class IsDictFilter(BoundFilter):
    key = "dict"

    def __init__(self, dict):
        self.dict = dict

    async def check(self, message: types.Message):
        member = await message.bot.get_chat_member(message.chat.id, message.from_user.id)
        return member.is_chat_admin()

    FORBIDDEN_PHRASE = [
        "Апездал",
        "Апездошенная",
        "Блядь",
        "Блядство",
        "Выебон",
        "Выебать",
        "Вхуюжить",
        "Гомосек",
        "Долбоёб",
        "Ебло",
        "Еблище",
        "Ебать",
        "Ебическая сила",
        "Ебунок",
        "Еблан",
        "Ёбнуть",
        "Ёболызнуть",
        "Ебош",
        "Заебал",
        "Заебатый",
        "Злаебучий",
        "Заёб",
        "Иди нахуй",
        "Колдоебина",
        "Манда",
        "Мандовошка",
        "Мокрощелка",
        "Наебка",
        "Наебал",
        "Наебаловка",
        "Напиздеть",
        "Отъебись",
        "Охуеть",
        "Отхуевертить",
        "Опизденеть",
        "Охуевший",
        "Отебукать",
        "Пизда",
        "Пидарас",
        "Пиздатый",
        "Пиздец",
        "Пизданутый",
        "Поебать",
        "Поебустика",
        "Проебать",
        "Подзалупный",
        "Пизденыш",
        "Припиздак",
        "Разъебать",
        "Распиздяй",
        "Разъебанный",
        "Сука",
        "Сучка",
        "Трахать",
        "Уебок",
        "Уебать",
        "Угондошит",
        "Уебан",
        "Хитровыебанный",
        "Хуй",
        "Хуйня",
        "Хуета",
        "Хуево",
        "Хуесос",
        "Хуеть",
        "Хуевертить",
        "Хуеглот",
        "Хуистика",
        "Членосос",
        "Членоплет",
        "Шлюха"
     ]
