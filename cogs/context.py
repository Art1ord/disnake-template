import disnake
from disnake.ext import commands

class Context(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.user_command(name="Информация о пользователе")
    async def avatar(self, inter: disnake.ApplicationCommandInteraction):
        """
        Команда, которая выводит информацию о пользователе и его аватаре
        :param inter: Объект взаимодействия с командой
        """
        user = inter.user
        username = user.name  # Имя пользователя
        is_bot = user.bot  # Является ли пользователь ботом
        avatar_url = user.display_avatar.url  # URL аватара пользователя

        embed = disnake.Embed(title=f"Информация о пользователе: {username}", color=disnake.Color.blue())
        embed.add_field(name="Имя пользователя:", value=username, inline=True)
        embed.add_field(name="Бот:", value=is_bot, inline=True)
        embed.set_thumbnail(url=avatar_url)

        await inter.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Context(bot))
    print(f"{__name__} готов к работе")

