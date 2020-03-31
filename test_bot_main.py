import COVID19Py
import telebot

covid19 = COVID19Py.COVID19()
location = covid19.getLocationByCountryCode('US')
print(location)
date = location[0]['last_updated'].split("T")
print(date)
    
# locations = covid19.getLocations()

# print(locations)
# bot = telebot.TeleBot('1016041250:AAHbCS_TlmqG2baVRkc-vnuLwr7H8OrrSUc')

# @bot.message_handler(commands=['start'])
# def start(message):
#     send_mess = f"<b>Hi {message.from_user.first_name}!</b>\n Put Country"
#     bot.send_message(message.chat.id, send_mess, parse_mode='html')
    
# bot.polling(none_stop=True)    