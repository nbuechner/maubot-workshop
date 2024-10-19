from maubot import Plugin, MessageEvent
from maubot.handlers import command


class WorkshopBot(Plugin):
  @command.new(name="hello") 
  async def hello_world(self, evt: MessageEvent) -> None:
    await evt.reply("Hello, World!")