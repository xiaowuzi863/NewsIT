import discord # aggiornato alla versione 1.0.0a ---> se usate la versione =< a 1.0.0.a la funzione per mandare l'output nel canale news
from discord.ext.commands import Bot
from itertools import islice
import random
TOKEN = input('YOUR TOKEN:')
pre = "!"
client = Bot(command_prefix=pre)

def canalenews(canale, nomecan): #funzione per listare i canali e mandare l'output al canale news [il quale dovrà essere già creato dagli admin]
    for canali in client.get_all_channels():
        if canali.name == nomecan:
            return canali
    return None

#---------------------------------------- ANSA ----------------------------------------------------#
@client.command(name="ansa",
                category="Help Command",
                description="per richiamare il bot usare: !ansa",
                brief ="per più info, digitare !help ansa",
                aliases=['ANSA','Ansa'])

@client.event
async def ansa():
    import json
    import requests
    import re
    ansa = "https://www.ansa.it/sito/notizie/topnews/index.shtml"
    req = requests.get(ansa).text
    news = re.findall(r'<a href="([^"]*)"[^>]*>(.*?)</a>',req) #Espressione regolare per estrarre link del articolo $
    iterator = islice(news, 314)
    canews = canalenews(client.get_all_channels(), 'news')
    await client.send_message(canews, "Ultime notizie:")
    for newss in iterator:
        if "/sito/notizie/topnews/2019/" in newss[0]:
            if "img" not in newss[1]:
                newslink = "http://www.ansa.it" + newss[0]
                short = "https://cutt.ly/api/api.php?key=c3b22a920fe5a7b5261dd514ba9b0a0f&short="+newslink #per rendere i link meno ingombranti, NO ADS NO WAIT TO FORWARD
                reeq = requests.get(short).text
                shortres = json.loads(reeq)
                shortlink = shortres['url']
                newssay = str(" **Titolo:** " + "*"+newss[1]+"*" + " **LINK:** " + shortlink['shortLink'])
                await client.send_message(canews, newssay)

client.run(TOKEN)
#---------------------------------------- Coming SOON -----------------------------------------------#
#---------------------------------------- HUFFINGPOST -----------------------------------------------#
#---------------------------------------- ILFATTOQUOTIDIANO -----------------------------------------------#

