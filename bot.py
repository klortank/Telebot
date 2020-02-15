import telebot
import config
from telebot import types


@bot.message_handler(commands=['start'])

def start_message(message):
	bot.send_message(message.chat.id, "Привет, вижу ты нашёл моего бота, который ничем не отличается от других, только если списком команд, надеюсь он тебе понравится, и да он создан только для Fun-а, поэтому не воспринимай всё что тут увидишь всерьёз")
	bot.send_message(message.chat.id, "Если хочешь подкинуть идейку насчёт бота, то вот мой вк: https://vk.com/klor_tank31")

@bot.message_handler(content_types=['text'])
def send_text(message):
		if message.text.lower() == 'привет':
			bot.send_message(message.chat.id, "Привет, чем я могу тебе помочь?")
		elif message.text.lower() == 'как взломать жопу руслана?':
			bot.send_message(message.chat.id, 'Никак, там уже всё взломано')
		elif message.text.lower() == 'пока':
			bot.send_message(message.chat.id, 'Пока, с тобой было интересно общаться!')
		elif message.text.lower() == "как дела?":
			bot.send_message(message.chat.id, 'У меня всё найс')
		elif message.text.lower() == 'как житуха':
			bot.send_message(message.chat.id, 'Отлично')
		elif message.text.lower() == 'что делаешь?':
			bot.send_message(message.chat.id, 'Общаюсь с красивым и умным человеком')
		elif message.text.lower() == 'иди нахуй':
			bot.send_message(message.chat.id, 'Сам туда иди или лучше сядь')
		elif message.text.lower() == 'пошёл нахуй':
			bot.send_message(message.chat.id, 'Сам туда иди или лучше сядь')
		elif message.text.lower() == 'сам сядь':
			bot.send_message(message.chat.id, 'Только после вас')
		elif message.text.lower() == 'нет ты':
			bot.send_message(message.chat.id, 'Я настаиваю')
		elif message.text.lower() == 'да':
			bot.send_message(message.chat.id, 'Нет')
		elif message.text.lower() == 'нет':
			bot.send_message(message.chat.id, 'Да')
		elif message.text.lower() == 'кто лучше хабиб или конор?':
			bot.send_message(message.chat.id, 'Определённо Хабиб, но если ты болеешь за Конора, то я тебя не сужу, ведь это твой выбор!')
		elif message.text.lower() == 'а':
			bot.send_message(message.chat.id, 'б')
		elif message.text.lower() == 'в':
			bot.send_message(message.chat.id, 'г')
		elif message.text.lower() == 'д':
			bot.send_message(message.chat.id, 'е')
		elif message.text.lower() == 'бот':
			bot.send_message(message.chat.id, 'Я вас слушаю')
		elif message.text.lower() == 'антон':
			bot.send_message(message.chat.id, 'Он мой создатель')
		elif message.text.lower() == 'балуев':
			bot.send_message(message.chat.id, 'Это фамилия моего создателся')
		elif message.text.lower() == 'xiomi':
			bot.send_message(message.chat.id, 'Топ за свои деньги')
		elif message.text.lower() == 'samsung':
			bot.send_message(message.chat.id, 'Не топ за свои деньги')
		elif message.text.lower() == 'соня':
			bot.send_message(message.chat.id, 'Это любовь всей моей жизни (это колонка)')
		elif message.text.lower() == 'александра':
			bot.send_message(message.chat.id, 'А вот она уже точно любовь всей моей жизни')
		elif message.text.lower() == 'гдз':
			bot.send_message(message.chat.id, 'Могу посоветовать вам Гдз по матеше 5 класс веленкина')
		elif message.text.lower() == 'ё':
			bot.send_message(message.chat.id, 'ж')
		elif message.text.lower() == 'не согласен':
			bot.send_message(message.chat.id, 'А я согласен')
		elif message.text.lower() == 'код':
			bot.send_message(message.chat.id, 'Не сложный')
		elif message.text.lower() == 'молодец':
			bot.send_message(message.chat.id, 'Спасибо за комплимент, ты тоже')
		elif message.text.lower() == 'з':
			bot.send_message(message.chat.id, 'Ты выйграл, я дальше не знаю алфавит')
		elif message.text.lower() == 'и':
			bot.send_message(message.chat.id, 'Я ведь уже сказал что я не знаю алфавит и ты выйграл')
		elif message.text.lower() == 'й':
			bot.send_message(message.chat.id, 'Ты что не понимаешь что я тебе говорю?')
		elif message.text.lower() == 'к':
			bot.send_message(message.chat.id, 'Нет, ну это уже не смешно, заканчивай')
		elif message.text.lower() == 'л':
			bot.send_message(message.chat.id, 'Если ты сейчас не остановишься, то я перестану отвечать на такое')
		elif message.text.lower() == 'м':
			bot.send_message(message.chat.id, 'Я тебя предупредил')
		elif message.text.lower() == 'хуй соси':
			bot.send_message(message.chat.id, 'Сначала ты')
		elif message.text.lower() == 'артём':
			bot.send_message(message.chat.id, 'Молодец')
		elif message.text.lower() == '/help':
			bot.send_message(message.chat.id, 'Нееее, давай сам разбирайся')
		elif message.text.lower() == 'р' :
			bot.send_message(message.chat.id, 'Ладно, ты слишком умный либо упорный, теперь можешь смело идти к разрабу за подарком в вк')
		else:
			bot.send_message(message.chat.id, 'Я вас не понимаю, уточните')

name = '';
surname = '';
age = 0;
@bot.message_handler(content_types=['text'])
def send_message(message):
    if message.text == '/reg':
        bot.send_message(message.chat.id, "Как тебя зовут?");
        bot.register_next_step_handler(message, get_name);
    else:
        bot.send_message(message.chat.id, 'Напиши /reg');

def get_name(message):
    global name;
    name = message.text;
    bot.send_message(message.chat.id, 'Какая у тебя фамилия?');
    bot.register_next_step_handler(message, get_surnme);

def get_surname(message):
    global surname;
    surname = message.text;
    bot.send_message('Сколько тебе лет?');
    bot.register_next_step_handler(message, get_age);

def get_age(message):
    global age;
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    keyboard = types.InlineKeyboardMarkup();
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes');
    keyboard.add(key_yes);
    key_no= types.InlineKeyboardButton(text='Нет', callback_data='no');
    keyboard.add(key_no);
    question = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?';
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes": 
        ...
        bot.send_message(call.message.chat.id, 'Запомню : )');
    elif call.data == "no":
        ... 

bot.polling(none_stop=True, interval=0)