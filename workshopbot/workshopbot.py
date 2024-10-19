from maubot import Plugin, MessageEvent
from maubot.handlers import command


class WorkshopBot(Plugin):
  @command.new(name="welcome") 
  async def hello_world(self, evt: MessageEvent) -> None:
    await evt.reply("Welcome to the Matrix Workshop!")

  @command.new(name="hello")
  @command.argument(name="name", pass_raw=True, required=False)  # Optional argument
  async def hello_world(self, evt: MessageEvent, name: str = "World") -> None:
      # If no name is provided, use the default "World"
      greeting = f"Hello, {name or 'World'}!"
      await evt.reply(greeting)