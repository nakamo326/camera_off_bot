import discord
from discord.ext import commands
from bot_token import TOKEN

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)


@bot.command()
async def coff(ctx: commands.Context):
    await ctx.send(f'{ctx.author} さんは通信負荷軽減のためカメラオフでレビューされるそうﾃﾞｽ')
    message: discord.Message = ctx.message
    await message.add_reaction('✅')


@bot.event
async def on_command_error(ctx, error):
    print(error)
    return


bot.run(TOKEN)
