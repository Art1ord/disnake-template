# disnake Module
import asyncio
import disnake                      # Модуль дискорда 
from disnake.ext import commands,tasks    # Основные какие то модули

intents = disnake.Intents.all()
intents.members = True
# Installed modules
import os # Очистка кончоли

# Cliear console [Linux]
os.system("cls") # Очитска консоли от мосура

# Token
from dotenv import load_dotenv
load_dotenv()
# Cosg list
cogs = [        # Коги из нашей папки
    "commands",
    "Modal",
    "context"
    ]

# Class Main 
class Main(commands.Bot):                   # Обозночаем что наш основной файл является основным 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# Даём понять что дальше мы будем оброщятся к client
bot = Main(
    help_command = None,                # Убираем help
    command_prefix = "!",               # Префикс бота
    intents=intents,
    reload=True,
    activity=disnake.Activity(type=disnake.ActivityType.watching, name=f"за тобой"),
    status=disnake.Status.idle)    # Intenst или коротко разришения для бота Побробнее здесь "https://discord.com/developers/applications"

# Очередная проверка на обозночения файла родительским а тоесть основным
if __name__ == "__main__":
    # НАчала загрузки когов
    for extension in cogs:
        cog = f"cogs.{extension}"

        # Загружаем файл когов
        try:
            bot.load_extension(cog)
        
        # Если проезошла ошибка принтанёт в консоль
        except Exception as e:
            print(e)

@bot.event
async def on_ready() -> None:
    print("Бот подключен")
    print()
    print(" - Информация о боте - ")
    print("Имя бота: {0.user}".format(bot))
    print(f"ID бота: {bot.user.id}")
    status_task.start()
    
#статус бота кд 60 секунд 
@tasks.loop()
async def status_task() -> None:
    await bot.change_presence(status=disnake.Status.dnd, activity=disnake.Game("DOTA 3"))
    await asyncio.sleep(60)
    await bot.change_presence(status=disnake.Status.online, activity=disnake.Activity(type=disnake.ActivityType.listening, name="Трава у дома"))
    await asyncio.sleep(60)
    await bot.change_presence(status=disnake.Status.idle, activity=disnake.Activity(type=disnake.ActivityType.watching, name="Хентай"))
    await asyncio.sleep(60)

#презагруска кога
@bot.command()
async def reload(self, ctx, cog_name):
    """
    Команда для перезагрузки указанного кога.
    :param ctx: Контекст выполнения команды.
    :param cog_name: Название кога для перезагрузки.
    """
    developers = os.getenv("DEVELOPERS")  # Получаем список разработчиков из переменной окружения dotenv(.env файл).

    if ctx.author.id not in developers:
        return await ctx.send("У вас нет доступа к этой команде.")  # Проверяем разрешение пользователя.

    try:
        cog_path = f"cogs.{cog_name}"
        self.bot.unload_extension(cog_path)  # Выгружаем ког.
        self.bot.load_extension(cog_path)  # Загружаем ког заново.
        print(f"Перезагружен ког: {cog_name}")
        await ctx.send(f"Ког {cog_name} успешно перезагружен!")
    except Exception as e:
        print(f"Ошибка при перезагрузке кога: {cog_name}\n{type(e).__name__}: {e}")
        await ctx.send(f"Произошла ошибка при перезагрузке кога {cog_name}.")

bot.run(os.getenv("TOKEN"))# Получаем токен бота из переменной окружения dotenv(.env файл).