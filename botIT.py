from discord.ext.commands import Bot
from itertools import islice
import random
TOKEN = ('YOUR TOKEN')
pre = "!"
client = Bot(command_prefix=pre)

#---------------------------------------- ANSA ----------------------------------------------------#
@client.command(name="ansa",
                category="Help Command",
                description="per richiamare il bot usare: !ansa",
                brief ="per più info, digitare !help ansa",
                aliases=['ANSA','Ansa'])
async def ansa():
    import json
    import requests
    import re
    ansa = "https://www.ansa.it/sito/notizie/topnews/index.shtml"
    req = requests.get(ansa).text
    news = re.findall(r'<a href="([^"]*)"[^>]*>(.*?)</a>',req) #Espressione regolare per estrarre link del articolo e il titolo tag <a href> </a>
    iterator = islice(news, 314)
    await client.say("Ultime notizie:")
    for newss in iterator:
        if "/sito/notizie/topnews/2019/" in newss[0]:
            if "img" not in newss[1]:
                newslink = "http://www.ansa.it" + newss[0]
                short = "https://cutt.ly/api/api.php?key=['YOUR API KEY']&short="+newslink #per rendere l'output meno ingombrante con link lunghi! NO ADS OR PAY PER CLICK DIRECT REDIRECT
                reeq = requests.get(short).text
                shortres = json.loads(reeq)
                shortlink = shortres['url']
                newssay = str(" **Titolo:** " + "*"+newss[1]+"*" + " **LINK:** " + shortlink['shortLink'])
                await client.say(newssay)
                
client.run(TOKEN)                
#---------------------------------------- Coming SOON -----------------------------------------------#
#---------------------------------------- HUFFINGPOST -----------------------------------------------#
#---------------------------------------- ILFATTOQUOTIDIANO -----------------------------------------------#
