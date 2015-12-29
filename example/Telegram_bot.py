# encoding: utf-8
import json
from pprint import pprint
import urllib
import urllib2
from config import TOKEN
import be


class DanieleBot(object):
    def __init__(self):
        self.base_url = "https://api.telegram.org/bot" + TOKEN + "/"
        self.offset = 0

    def get_me(self):
        response = json.load(urllib2.urlopen(self.base_url + "getMe"))
        return response['ok']

    def get_updates(self):
        data = {
            "offset": self.offset
        }
        response = json.load(urllib2.urlopen(self.base_url + "getUpdates", urllib.urlencode(data)))
        if len(response['result']) > 0:
            self.offset = response['result'][-1]['update_id'] + 1
        return response['result']

    def send_message(self, msg, chat_id, reply_id=None):
        msg = be.singola_bestemmia()
        data = {
            "chat_id": chat_id,
            "text": msg,
        }
        if reply_id is not None:
            data["reply_to_message_id"] = reply_id
        response = json.load(urllib2.urlopen(self.base_url + "sendMessage", urllib.urlencode(data)))
        #pprint(response)


def polling():
    bot = DanieleBot()
    print bot.get_me()

    while True:
        testo = bot.get_updates()
        for in_messaggio in testo:
            messaggio = in_messaggio['message']
            try:
                if messaggio.get('text'):
                    if "bestemmia" in messaggio['text']:
                        bot.send_message(messaggio['text'], messaggio['chat']['id'], messaggio['message_id'])
            except NameError:
                print "XD "


if __name__ == "__main__":
    polling()
