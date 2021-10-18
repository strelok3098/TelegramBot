#импортируем файл для логгирования, задания логики
import logging
import settings
#импортируем нужные компоненты

from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
#прописываем логгирования, выдача сообщений , задача уровня: debug-самый нижний уровень, необходим при отладки
#info-более высокий уровень
#warning- оповещение от авторов
#eror серьезные неустранимые ошибки
logging.basicConfig(filename='bot.log',level=logging.INFO)
#настройка прокси
PROXY={'proxy_url':settings.PROXY_URL,'urllib3_proxy_kwargs':{'username':settings.PROXY_USERNAME,'password':settings.PROXY_PASSWORD}}
def great_user(update,context):
    print('Повелитель, кто то только что зашел в бота и написал ему')

    
def talk_me(update,context):
    text=update.message.text
    print(text)
    update.message.reply_text('''Любимая моя, я тебя безумно люблю
    ты самое прекрасное что случалось мной
    ты просто чудо
    свет в моец жизни
    поправляйся пупсик, я тебя безумно люблю
    твой суслик''')





#функция которая соединяется с платформой Telegram, 'тело ' бота
def main():
    #создаем бота и предаем ключ для авторизации на серверах телеграм
    mybot=Updater(settings.API_KEY,use_context=True,request_kwargs=PROXY)
   #обьявляем для удобства и постоянного н епрописыванмя
    dp=mybot.dispatcher   
   #рассказывваем боту, что через диспетчера обратиться к заголовку и вызвать функцию
    dp.add_handler(CommandHandler('start',great_user))
    #при использовании Messagehendler указываем что мы хотим реагироватт только на текст
    dp.add_handler(MessageHandler(Filters.text, talk_me))
    logging.info('Bot started')
    #командуем боту начать ходить в телеграм за сообщение
    mybot.start_polling()
     #запускаем бота , он будет работать пока мы его не остановим
    mybot.idle()

if __name__=='__main__':
    main()