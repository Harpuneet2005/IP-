import discord
import requests 
import json
from replit import db
db["0"]={}

for i in db.keys():
  print(db[i])


client = discord.Client()

def Quote():
  ans=requests.get('https://zenquotes.io/api/quotes/')
  js=json.loads(ans.text)
  response=js[0]['q']+"\n"+"By - "+js[0]['a']
  return response
def addTeam(t_name):
  
  if t_name not in db.keys():
    db[t_name]=[]

def addWork(tname,wlink):
  db[tname].append(wlink)


@client.event
async def on_ready():
  print("we are logged in")
  
@client.event
async def on_message(message):
  if message.content =="!hello":
    print(message.author.name)
    await message.channel.send("Hi")
  elif message.content =="!quote":
    await message.channel.send(Quote())
  elif message.content.startswith("!new team"):
    
    name=message.content[10:]
    strname2=str(name)
    strname=str(message.author.name)
    db["0"][strname]= strname2
    print(message.author.name)
    print(db["0"][strname])
    if name not in db.keys():
      addTeam(strname2)
      
      await message.channel.send("The team has been created!")
    else:
      await message.channel.send("The team already exists.")

  elif message.content.startswith("!add work:"):
    await message.channel.send("What is yout Team-Name?")
    
    msg = await client.wait_for('message')
    aname=str(msg.author.name)
    print(aname)
    if msg.content in db.keys():
      tname=msg.content
      await message.channel.send("Enter the drive-link to your work!!")
      msg2 = await client.wait_for('message')
      addWork(tname,msg2.content)
    
          
      
        




  
client.run('OTg5ODM1Nzc5NDc4MDIwMTE2.GU9NTf.o0Ss0ZyGK0xO1tt20ksMirQMMZChjHPYTrz3aw')
