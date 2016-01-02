# -*- coding: utf-8 -*-
import webapp2
from google.appengine.api import urlfetch
import json
from pprint import pprint
import urllib
import urllib2
from config import TOKEN
import be
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

testo = []

class BeBot(object):
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

	def manage_webhook(self, messaggio):
		tgmsg = json.loads(messaggio)
		chat_id = tgmsg["message"]["chat"]["id"]
		try:
			testout = tgmsg["message"]["text"]
		except:
			testout = 'vuoto'
		return {'chat_id':chat_id, 'testout':testout}

	def send_message(self, msg, chat_id, reply_id=None):
		msg = be.singola_bestemmia()
		data = {
			"chat_id": chat_id,
			"text": msg,
		}
		if reply_id is not None:
			data["reply_to_message_id"] = reply_id
		response = json.load(urllib2.urlopen(self.base_url + "sendMessage", urllib.urlencode(data)))



class MainPage(webapp2.RequestHandler):
	def get(self):
		bot = BeBot()
		urlarrivo = 'bestemmia-1177.appspot.com/klfdlnfslknglkdfngfngdl'
		form_fields = {'url': urlarrivo}
		urlWH = 'https://api.telegram.org/bot%s/setWebhook' % TOKEN
		form_data = urllib.urlencode(form_fields)
		result = urlfetch.fetch(url=urlWH,
			payload=form_data,
			method=urlfetch.POST,
			headers={'Content-Type': 'application/x-www-form-urlencoded'})
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write('Be.stemmia')

class WebHookHandler(webapp2.RequestHandler):
	def post(self):
		bot = BeBot()
		testo = bot.manage_webhook(self.request.body)
		try:
			if "bestemmia" in testo['testout']:
				bot.send_message(' ', testo['chat_id'])
		except NameError:
			print "XD "



app = webapp2.WSGIApplication([
	('/klfdlnfslknglkdfngfngdl', WebHookHandler),
	('/', MainPage),
], debug=True)
