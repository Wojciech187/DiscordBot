from nextcord.ext import commands,tasks
from nextcord.ext.commands import has_permissions,has_role,has_any_role,has_guild_permissions
import os
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv("token")
    bot = commands.Bot(command_prefix='#')
    bot.run(token)