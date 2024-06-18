# Bot Factory

Bot Factory is a simple Discord bot maker that allows you to easily add and remove custom commands. This bot provides a straightforward way to extend functionality dynamically within a Discord server.

## Features

- Add custom commands with custom responses.
- Remove existing custom commands.
- List all available custom commands.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- `discord.py` library

### Installation

1. Clone the repository or download the source code.

   ```bash
   git clone <repository-url>
   cd bot-factory
   ```

2. Install the required Python packages.

   ```bash
   pip install discord.py
   ```

### Usage

1. Run the bot script.

   ```bash
   python bot_factory.py
   ```

2. When prompted, enter your Discord bot token.

### Commands

- `!add_command <command_name> <response>`: Adds a new command with the specified response. For example:
  ```
  !add_command hello Hello, world!
  ```
  This will create a new command `!hello` that responds with "Hello, world!".

- `!remove_command <command_name>`: Removes an existing command. For example:
  ```
  !remove_command hello
  ```
  This will remove the `!hello` command.

- `!list_commands`: Lists all custom commands that are currently available.

### Example

```python
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
```

## Running on Replit

To use this bot on Replit, visit the following link: [Bot Factory on Replit](https://replit.com/@calestialashley/Bot-Factory-3?s=app)

Simply fork the project, add your Discord bot token in the appropriate field, and run the bot.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- The `discord.py` library for providing the core functionality.
- The Discord community for inspiration and support.
