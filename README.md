# DexPrint 



## Table of Contents

- [About](#about)
- [Used](#used)
- [Deploy](#deploy)



## About

Bot which allows to print and scan with different parameters using the Telegram messenger.

You can send any file for printing or scanning. It is mean't for businesses and automates every process however possible.

## Used

- [AIOGram](https://github.com/aiogram/aiogram) as framework for Telegram Bot API
- [FastAPI](https://github.com/tiangolo/fastapi) as Web framework and [uvicorn](https://github.com/encode/uvicorn) for running it 
- LibreOffice:
  - [unoserver](https://github.com/unoconv/unoserver) for converting documents to PDF using LibreOffice
- [PyPDF4](https://github.com/claird/PyPDF4) for reading PDF files
- Apple CUPS (for printing):
  - [pycups](https://github.com/OpenPrinting/pycups) for interaction with CUPS
  - [pycups-notify](https://github.com/anxuae/pycups-notify) for receiving notifications about the status of a print job
  - [Docker image](https://hub.docker.com/r/ydkn/cups) for deployment
- eSCL protocol for scanning

## Deploy

### Environment


### Printer driver
 cups are used ( this is specific for printers and should be added for supported printers)
### Docker

To run use Docker:

```bash
docker-compose build
docker-compose -d up  # -d to run in background 
docker-compose ps
```

### Problems "if you run into problems with networking or hosting your printer on a server an alternative will be to run this program:
import os
import win32api
import telebot
import wget




#your token to access the HTTP API
API_TOKEN = 'Your bot token'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(content_types=['document', 'photo'])
def get_doc(message):
	try:
		if message.content_type == 'photo':
			doc_id = message.photo[-1].file_id
		else:
			doc_id = message.document.file_id
		#get info about file
		doc = bot.get_file(doc_id)
		#download it
		filename = wget.download('https://api.telegram.org/file/bot{0}/{1}'.format(API_TOKEN, doc.file_path))
		#get file path on host
		file_path = os.path.join(os.getcwd(), filename)
		#print it with default printer
		win32api.ShellExecute(0, "print", file_path, None,  ".",  0)
		#Send messsage that everything is ok
		bot.send_message(message.from_user.id, "printing!")
		bot.send_message(message.from_user.id, "🖨️")




	except Exception as error:
		#if something went wrong send error message with a reason
		bot.send_message(message.from_user.id, 'Error! \nAdditional information: {}'.format(error))


@bot.message_handler(content_types=['text'])
def send_message(message):
	bot.send_message(message.from_user.id, '😌')
	bot.send_message(message.from_user.id, f'You said {message.text}.' '\nTo print simply send a document to print')


#print(bot.message.from_user)

#start bot
bot.polling(none_stop=True, interval=0) 

### this program is quiet limited because your device needs to be ON constantly.  Another option is to host this on google cloud and interact with it through google. 
