from maubot import Plugin, MessageEvent
from maubot.handlers import command
import requests
import urllib.parse

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

  @command.new(name="weather", aliases=["wttr"], must_consume_args=True, help="Please provide a city name. Example: !weather London")
  @command.argument(name="city", pass_raw=True, required=True)
  async def weather_command(self, evt: MessageEvent, city: str) -> None:
    city = city.strip()

    if not city:
      await evt.reply("Please provide a city name. Example: !weather London")
      return

    json_url = f"https://wttr.in/{city}?format=j1"
    response_json = requests.get(json_url)
    try:
      if response_json.status_code != 200:
        return
    except:
      return
    
    weather_data = response_json.json()
    # Fetching the output from the second URL (text-based weather info with icons)
    text_url = f"https://wttr.in/{city}?format=2"
    response_text = requests.get(text_url)
    weather_summary = response_text.text

    # Extracting city and weather information from JSON
    city_info = {
        "city": weather_data.get("nearest_area", [{}])[0].get("areaName", [{}])[0].get("value", "N/A"),
        "region": weather_data.get("nearest_area", [{}])[0].get("region", [{}])[0].get("value", "N/A"),
        "country": weather_data.get("nearest_area", [{}])[0].get("country", [{}])[0].get("value", "N/A"),
        "current_temp_c": weather_data.get("current_condition", [{}])[0].get("temp_C", "N/A"),
        "feels_like_c": weather_data.get("current_condition", [{}])[0].get("FeelsLikeC", "N/A"),
        "weather_desc": weather_data.get("current_condition", [{}])[0].get("weatherDesc", [{}])[0].get("value", "N/A"),
    }
    city_url = urllib.parse.quote(city_info['city'])
    output = f"The [weather](https://wttr.in/{city_url}) in {city_info['city']}, {city_info['region']}, {city_info['country']} is {weather_summary}"
    await evt.reply(output.strip())
    