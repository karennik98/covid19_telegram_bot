import telebot
from telebot import types
import COVID19Py

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('1046256990:AAFVXCzIohlO4eplq84rwAqaVg3Mzx_2twc')

@bot.message_handler(commands=['start'])
def start(message):
	send_message = f"<b>Hi {message.from_user.first_name}!</b> <b> For information about COVID19 type" \
		f"name of country: US, Russia, Armenia </b>"
	bot.send_message(message.chat.id, send_message, parse_mode='html')

@bot.message_handler(content_types=['text'])
def mess(message):
	final_message = ""
	get_message_bot = message.text.strip().lower()
	if get_message_bot == "us":
		location = covid19.getLocationByCountryCode("US")
	elif get_message_bot == "ukraine":
		location = covid19.getLocationByCountryCode("UA")
	elif get_message_bot == "russia":
		location = covid19.getLocationByCountryCode("RU")
	elif get_message_bot == "italy":
		location = covid19.getLocationByCountryCode("IT")
	elif get_message_bot == "france":
		location = covid19.getLocationByCountryCode("FR")
	elif get_message_bot == "germany": 
		location = covid19.getLocationByCountryCode("DE")
	elif get_message_bot == "japan":
		location = covid19.getLocationByCountryCode("JP")
	elif get_message_bot == "armenia":
		location = covid19.getLocationByCountryCode("AM")
	else:
		location = covid19.getLatest()
		final_message = f"<u>Worldwide Data:</u>\n<b>Sick: </b>{location['confirmed']:,}\n<b>Died: </b>{location['deaths']:,}"
  
	print(location, '\n', final_message)
        
	if final_message == "":
		date = location[0]['last_updated'].split("T")
		time = date[1].split(".")
		final_message = f"<u>Country Data:</u>\nPopulation: {location[0]['country_population']:,}\n" \
				f"Last updated: {date[0]} {time[0]}\nLatest data:\n<b>" \
				f"Sick: </b>{location[0]['latest']['confirmed']:,}\n<b>Died: </b>" \
				f"{location[0]['latest']['deaths']:,}"

	bot.send_message(message.chat.id, final_message, parse_mode='html')

bot.polling(none_stop=True)
