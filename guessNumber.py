import telebot
import random
global c,r
c=5
bot=telebot.TeleBot('1776106722:AAESboQEm2OMFXjOe9G-z3Qbn8hKRpxTEpA')
btns=telebot.types.ReplyKeyboardMarkup(row_width=1)
btn1=telebot.types.KeyboardButton('شروع بازي جديد😁')
btns.add(btn1)
def new_game():
    global r,c
    c=5
    r=random.randint(0,30)

@bot.message_handler(commands=['start'])
def wlc(message):
    bot.send_message(message.chat.id,'سلام خوش اومدي شروع كنيم؟😍',reply_markup=btns)
@bot.message_handler(func=lambda message:True)
def guess(message):
    global r,c
    if message.text=='شروع بازي جديد😁':
        bot.send_message(message.chat.id,'عدد جديد رو حدس بزن(بين 1 تا 30)')
        new_game()
    else:
        mr=int(message.text)
        c-=1
        if c>0:
            if r==mr:
                bot.send_message(message.chat.id,'🎉آفرين برنده شدي ')
                bot.send_message(message.chat.id,'عدد جديد رو حدس بزن')
                new_game()
            elif r>mr:
                bot.send_message(message.chat.id,'عدد بيشتري وارد كن👆')
                bot.send_message(message.chat.id,'تعداد حدس هاي باقي مونده:'+str(c*'💙'))
            elif r<mr:
                bot.send_message(message.chat.id,'عدد كمتري وارد كن👇')

                bot.send_message(message.chat.id,'تعداد حدس هاي باقي مونده:'+str(c*'💙'))
        else:
            bot.send_message(message.chat.id,'باختي كه😒يه بازي ديگه شروع كن')
            bot.send_message(message.chat.id,'عدد جديد رو حدس بزن')
            new_game()

bot.polling()