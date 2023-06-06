import disnake
from disnake.ext import commands
import datetime
from disnake import TextInputStyle

class Embed1(disnake.ui.Modal):
    def __init__(self):
        # Детали модального окна и его компоненты

        # Создание компонентов ввода текста
        components = [
            disnake.ui.TextInput(
                label="Автор",
                placeholder="Укажите текст",
                custom_id="author",
                style=TextInputStyle.short,
                min_length=1,
                max_length=30,
                required=False
            ),
            disnake.ui.TextInput(
                label="Заголовок",
                placeholder="Укажите текст",
                custom_id="title",
                style=TextInputStyle.short,
                min_length=1,
                max_length=50,
                required=False
            ),
            disnake.ui.TextInput(
                label="Описание",
                placeholder="Укажите текст",
                custom_id="des",
                style=TextInputStyle.paragraph,
                min_length=1,
                max_length=1000,
                required=True,
            ),
            disnake.ui.TextInput(
                label="Футер(подвал)",
                placeholder="Если хотите указать дату -> {timestamp}",
                custom_id="footer",
                style=TextInputStyle.paragraph,
                min_length=1,
                max_length=30,
                required=False
            ),
        ]

        # Инициализация модального окна
        super().__init__(
            title="Отправить эмбед",
            custom_id="create_tag",
            components=components,
        )

    async def callback(self, inter: disnake.ModalInteraction):
        # Получение введенных значений
        input = inter.text_values

        # Замена "{author}" на имя автора и "{author.mention}" на упоминание автора
        input['author'] = input['author'].replace('{author}', f'{inter.author}')
        input['des'] = input['des'].replace('{author.mention}', f'{inter.author.mention}')

        # Замена "{timestamp}" на текущую дату и время
        footer = input['footer'].replace("{timestamp}", str(datetime.datetime.now()))

        # Создание объекта Embed
        embed = disnake.Embed(
            title=input.get('title'),  # Заголовок эмбеда
            description=input.get('des'),  # Описание эмбеда
            colour=disnake.Colour.random()  # Случайный цвет эмбеда
        )
        embed.set_author(name=input.get('author'))  # Установка автора эмбеда
        embed.set_footer(text=footer)  # Установка подвала эмбеда

        # Отправка сообщения с эмбедом
        await inter.channel.send(embed=embed)
        await inter.response.send_message("Успешно", ephemeral=True)


class Embed(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    #Декоратор @commands.has_permissions(administrator=True) требует, чтобы только пользователи с административными правами могли использовать эту команду.
    @commands.cooldown(rate=1, per=25, type=commands.BucketType.user)#кд 25 секунд
    #Декоратор @commands.cooldown(rate=1, per=25, type=commands.BucketType.user) добавляет задержку между использованиями команды.
    @commands.slash_command(description="Create embed | Создать эмбед")
    async def embed(self, inter: disnake.AppCmdInter):
        # Отправка модального окна Embed1 при вызове команды /embed
        await inter.response.send_modal(modal=Embed1())

def setup(bot: commands.Bot):
    bot.add_cog(Embed(bot))
    print(f"{__name__} готов к работе")
