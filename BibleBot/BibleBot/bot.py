import discord
import time

def read_token():
    with open ("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()
client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity = discord.Game("på Temerold.se"))
    print("Bot setup is done.")
    print('Logged in as:')
    print(client.user.name)
    time.sleep(1)
    print(client.user.id)
    print('------------------------------------------------------------')

@client.event
async def on_message(message):
    channel = client.get_channel(728333105718362132)
    if message.content.find(".bible") != -1:
        while True:
            f_ = open("1 mosebok.txt", 'r')
            l = 1
            x = 1
            for word in f_:
                if word == "\n":
                    pass
                else:
                    await channel.send(word)
                    print("M1 Line " + str(l) + ": " + word + "\n")
                    l += 1
                    time.sleep(x)

            f_ = open("2 mosebok.txt", 'r')
            l = 1
            for word in f_:
                if word == "\n":
                    pass
                else:
                    await channel.send(word)
                    print("M2 Line " + str(l) + ": "+ word + "\n")
                    l += 1
                    time.sleep(x)

            f_ = open("3 mosebok.txt", 'r')
            l = 1
            for word in f_:
                if word == "\n":
                    pass
                else:
                    await channel.send(word)
                    print("M3 Line " + str(l) + ": "+ word + "\n")
                    l += 1
                    time.sleep(x)

            f_ = open("4 mosebok.txt", 'r')
            l = 1
            for word in f_:
                if word == "\n":
                    pass
                else:
                    await channel.send(word)
                    print("M4 Line " + str(l) + ": "+ word + "\n")
                    l += 1
                    time.sleep(x)

            f_ = open("5 mosebok.txt", 'r')
            l = 1
            for word in f_:
                if word == "\n":
                    pass
                else:
                    await channel.send(word)
                    print("M5 Line " + str(l) + ": "+ word + "\n")
                    l += 1
                    time.sleep(x)



client.run(token)