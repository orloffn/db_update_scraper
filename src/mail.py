import smtplib
import email
import json


_MAIL_TEXT_ = '../conf/mail_text'


class Message:
	"""docstring for Message"""
	def __init__(self):
		self.config = self.__read_config('../conf/config.cfg')
		self.msg = email.message.EmailMessage()
		self.msg['Subject'] = self.config['subject']
		self.msg['From'] = self.config['from']
		self.msg['To'] = ', '.join(self.config['to'])
		with open(_MAIL_TEXT_) as fh:
			self.msg.set_content(fh.read())

	def __read_config(self, file):
        fh = open(file)
        return(json.load(fh)['mail'])

    def add_spreadsheet(self, file):
    	with open(file, 'rb') as fh:
    		self.msg.add_attachment(fh.read(),
    								maintype='application/xlsx',
    								subtype='xlsx',
    								filename='supplemental_bar_updates.xlsx')

    def send(self)
