import disnake 
from disnake.ext import commands

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Обычная команда
    @commands.command()
    async def hello(self, ctx):
        """
        Простая команда для приветствия
        """
        await ctx.send('Привет! Как дела?')

    #Слэш командa
    @commands.slash_command(
        name="hello",
        description="Простая команда для приветствия"#описания команды
    )
    async def hello_slash(self, inter):
        """
        Slash-команда для приветствия
        """
        await inter.response.send_message('Привет! Как дела?')

    
def setup(bot):
    bot.add_cog(Test(bot))
    print(f"{__name__} готов к работе")

