import logging  #Если в коде мы допустим ошибку, мы об этом не узнаем, так как авторы библиотеки для устойчивости бота "перехватывают" исключения, которые встречаются в нашем коде. Нам поможет стандартный модуль логирования.
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters    # Импортируем нужные компоненты. CommandHandler реагирует на команды. MessageHandler реагирует на текстовые сообщения.

import settings 

logging.basicConfig(filename="bot.log", level=logging.INFO)     #Конфигурируем logging. Имя, куда записывается. И уровни дебагов (1 - разработка - описание действий по шагам, 2 - информационные сообщения - когда что произошло, 3 - ворнинг - что планируется изменяться, 4 - неисправимые ошибки)

def greet_user(update, context): #update - то, что пришло с платформы Телеграм, context - штука, внутри которой можем отдавать команды боту.
    print("Вызван /start")  #Напиши в консоль старт
    update.message.reply_text("Здравствуй, пользователь")

def talk_to_me(update, context):    #Напишем функцию talk_to_me, которая будет "отвечать" пользователю
    text = update.message.text
    print(text)
    update.message.reply_text(text)     #Отправим пользователю его сообщение

def main():
    mybot = Updater(settings.API_KEY, use_context=True) # Создаем бота и передаем ему ключ для авторизации на серверах Telegram

    dp = mybot.dispatcher   #Просто сокращаем код (mybot.dispatcher). dispatcher - при наступлении события вызывается наша функция
    dp.add_handler(CommandHandler("start", greet_user))  #Добавляем к диспетчеру обработчик команд, который реагирует на команду "start", и вызовает функции
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))    #При использовании MessageHandler укажем, что мы хотим реагировать только на текстовые сообщения - Filters.text

    logging.info("Bot started")   #Залогируем в файл информацию о старте бота
    mybot.start_polling()   # Командуем боту начать ходить в Telegram за сообщениями
    mybot.idle()    # Запускаем бота, он будет работать, пока мы его не остановим принудительно

"""Сейчас мы просто вызываем функцию main() в самом конце файла bot.py. 
Вызов функций прямо на верхнем уровне считается плохим стилем и в дальнейшем вызовет проблемы, 
когда вам понадобится что-то импортировать из этого файла. 
В этом случае при импорте функция main() все равно будет вызвана и запустит бота, 
что приведет к тому, что ваша программа "зависнет".

В питоне есть общепринятый способ решить эту проблему. 
Если вам нужно вызвать функцию не внутри другой функции, 
она заключается в специальный блок, который исполняется только при прямом вызове файла python bot.py 
и не вызывается при импорте, например from bot import PROXY. Вот как это выглядит:"""

if __name__ == "__main__":   
    main()  # Вызываем функцию main() - именно эта строчка запускает бота