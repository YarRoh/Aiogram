from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
API_TOKEN: str = '6268125626:AAFqGoX2VT60K7es_di_IVyBycrjA3PAubg'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе твое сообщение')

async def send_sticker_echo(message: Message):
    print(message)
    await message.reply_sticker(message.sticker.file_id)

async def send_video_echo(message: Message):
    print(message)
    await message.reply_video(message.video.file_id)

async def send_photo_echo(message: Message):
    print(message)
    await message.reply_photo(message.photo[0].file_id)


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
async def send_echo(message: Message):
    await message.reply(text=message.text)


# Регистрируем хэндлеры
dp.message.register(process_start_command, Command(commands=["start"]))
dp.message.register(process_help_command, Command(commands=['help']))
dp.message.register(send_photo_echo, F.content_type == ContentType.PHOTO)
dp.message.register(send_sticker_echo, F.content_type == ContentType.STICKER)
dp.message.register(send_video_echo, F.content_type == ContentType.VIDEO)
dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)
