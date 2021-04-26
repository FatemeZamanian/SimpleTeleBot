import telebot
import random
global c,r
c=0
bot=telebot.TeleBot('1776106722:AAESboQEm2OMFXjOe9G-z3Qbn8hKRpxTEpA')
@bot.message_handler(commands=['start'])
def wlc(message):
    global r
    bot.send_message(message.chat.id,'سلام خوش اومدي😍 يك عدد بين 1 تا 30 حدس بزن🤷‍♂️')
    r=random.randint(0,30)
@bot.message_handler(func=lambda message:True)
def guess(message):
    
    global r
    # bot.send_message(message.chat.id,str(r))
    mr=int(message.text)
    #c+=1
    if r==mr:
        bot.send_message(message.chat.id,'🎉آفرين برنده شدي ')
        bot.send_message(message.chat.id,'اول استارت بزن بعد عدد جديد رو حدس بزن✌ /start ')
        
        #bot.send_message(message.chat.id,'تعداد حدس ها::'+str(c))
    elif r>mr:
       bot.send_message(message.chat.id,'عدد بيشتري وارد كن👆')
    elif r<mr:
            bot.send_message(message.chat.id,'عدد كمتري وارد كن👇')

bot.polling()