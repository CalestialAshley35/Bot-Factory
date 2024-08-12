import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def add_command(ctx, command_name: str, *, response: str):
    if command_name in bot.all_commands:
        await ctx.send(f"Command `{command_name}` already exists.")
        return

    async def new_command(ctx):
        await ctx.send(response)

    new_command.__name__ = command_name
    bot.command(name=command_name)(new_command)
    await ctx.send(f"Command `{command_name}` added with response: {response}")

@bot.command()
async def remove_command(ctx, command_name: str):
    if command_name not in bot.all_commands:
        await ctx.send(f"Command `{command_name}` does not exist.")
        return

    bot.remove_command(command_name)
    await ctx.send(f"Command `{command_name}` removed.")

@bot.command()
async def list_commands(ctx):
    commands_list = ', '.join([cmd for cmd in bot.all_commands if cmd not in ["add_command", "remove_command", "list_commands"]])
    await ctx.send(f"Available commands: {commands_list if commands_list else 'No custom commands available.'}")

@bot.command()
async def set_description(ctx, *, description: str):
    if len(description) > 190:
        await ctx.send("Description is too long. Please keep it under 190 characters.")
        return
    
    user_description = description + " | Made with Bot Factory"
    await bot.change_presence(activity=discord.Game(name=user_description))
    await ctx.send(f"Bot description set to: {user_description}")

def main():
    token = input("Please enter your Discord bot token: ")
    bot.run(token)

if __name__ == "__main__":
    main()