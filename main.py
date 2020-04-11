from bot import *
from keyboards import * 

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет, <b>{0.first_name}</b>! Я помогу тебе с Kali Linux!'.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markupinline)

@bot.message_handler(commands=['developer'])
def send_welcome(message):
    bot.reply_to(message, 't.me/Mrfire7')

@bot.message_handler(content_types=['text'])
def text_help (message):
    bot.send_message(message.chat.id,  "Шо?") 

def main():
	bot.polling(none_stop=True)


if __name__ == '__main__':
    main()
