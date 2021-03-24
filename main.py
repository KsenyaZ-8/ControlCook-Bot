import ptbot
import os
from pytimeparse import parse

TG_token = os.getenv('MY_TOKEN')
CHAT_ID = os.getenv('MY_ID')

#def reply(text):
    secs = parse(text) 
    bot.create_countdown(secs, notify_progress)
    bot.create_timer(secs, notify)

#def notify_progress (secs, secs_left, total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    text_message = 'Осталось {} секунд\n'.format(secs_left)
    print(render_progressbar (secs, secs_left))
    sum_message =  text_message +  progressbar
    message_id = bot.send_message(CHAT_ID, sum_message)
    bot.update_message(CHAT_ID,message_id, sum_message)

    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)

#def notify():
     bot.send_message(CHAT_ID, 'Время вышло')

def notify_progress (secs, secs_left, total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)

print(render_progressbar (10, 5))

#if __name__ == '__main__':
    bot = ptbot.Bot(TG_token)
    bot.send_message(CHAT_ID,'На сколько запустить таймер?')
    bot.reply_on_message(reply)
    bot.run_bot()
