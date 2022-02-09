import telegram

def sendmessage(message ,**kwargs):
    #message = message
    #send_message = "텍스트는" + message.number + "더하기" + message.boot + "더하기" +  message.address
    token = '5131482190:AAEY7A07dWeqWaIjZZGDiVjoZ50kMKdcayM'
    bot = telegram.Bot(token)
    print("good luck")
    #bot.message_loop(start_telegram)
    chat_id = '1047352647'
    bot.sendMessage(chat_id=chat_id, text=message)