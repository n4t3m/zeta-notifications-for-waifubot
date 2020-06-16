import discord
from discord.ext import commands
import requests
import setup

description = "Type $info to see more information."
TOKEN = setup.TOK
client = commands.Bot(command_prefix='!', description=description, help_command=None)
UID = setup.UID

client.RED = False
client.YELLOW = False
client.WHITE = False
client.BLACK = False
client.BLUE = False
client.GREEN = False



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    initcount = 0
    for g in client.guilds:
        initcount = initcount + len(g.members)
    game = discord.Game("azunyan best")
    await client.change_presence(status=discord.Status.online, activity=game)
    

@client.event
async def on_guild_join(guild):
    print("Joined New Server: " + guild.name + ". Members: " + str( len(guild.members) ) + ". Owner: " + guild.owner.display_name + ".")

@client.event
async def on_guild_remove(guild):
    print("Removed From Server: " + guild.name + ". Members: " + str( len(guild.members) ) + ". Owner: " + guild.owner.display_name + ".")

    


@client.event
async def on_message(message):
    if message.author == client.user:   
        return
        
    if message.author.id == 472141928578940958 and len(message.embeds) > 0 and "J-List Box" in message.embeds[0].title and "Box Keys" not in message.embeds[0].title:
        user = client.get_user(UID)
        box_msg = message.embeds[0].description
        box_msg = box_msg[190:-150]
        box_words = box_msg.split(" ")
        if box_words[0]== "White" and client.WHITE == True:
            await user.send("Box Color " + box_words[0] + "\nLink: " + message.jump_url)
            return
        if box_words[0]== "Red" and client.RED == True:
            await user.send("Box Color " + box_words[0] + "\nLink: " + message.jump_url)
            return
        if box_words[0]== "Blue" and client.BLUE == True:
            await user.send("Box Color " + box_words[0] + "\nLink: " + message.jump_url)
            return
        if box_words[0]== "Black" and client.BLACK == True:
            await user.send("Box Color " + box_words[0] + "\nLink: " + message.jump_url)
            return
        if box_words[0]== "Yellow" and client.YELLOW == True:
            await user.send("Box Color " + box_words[0] + "\nLink: " + message.jump_url)
            return 
        if box_words[0]== "Green" and client.GREEN == True:
            await user.send("Box Color " + box_words[0] + "\nLink: " + message.jump_url)
            return               
    if message.author.id == 472141928578940958 and len(message.embeds) > 0 and "Character" in message.embeds[0].title:
        code = str(message.embeds[0].color)[1:]     
        apiurl = "https://www.thecolorapi.com/id?hex=" + code   
        r = requests.get(apiurl)    
        jsonResponse= r.json()
        color = str(jsonResponse["name"]["value"])
        if "Bean" in color:
            print("bean thrown out")
            return
        ##print("Color: " + color)
        if( "Mineral Green" == color or "Tom Thumb" == color or "Limed Spruce" == color or "Hemlock" == color or "Bright Gray" == color or "River Bed" == color or "Costa Del Sol" == color):   
            #await message.channel.send("A/B " + color)
            strppp = "nothing"
        elif( "Bush" == color or "Metallic Bronze" == color or "Woodland" == color or "Verdigris" == color or "Indian Tan" == color or "Rustic Red" == color or "Bracken" == color or "Bulgarian Rose" == color or "Temptress" == color or "Dark Ebony" == color):  
            #await message.channel.send("B/G " + color)
            strppp = "nothing"
        elif( "Palm Leaf" == color or "Irish Coffee" == color or "Punga" == color or "Bronze Olive" == color or "Turtle Green" == color or "Palm Leaf" == color or "Jambalaya" == color or "Cioccolato" == color or "Gable Green" == color or "Rebel" == color or "Mahogany" == color or "Burnt Maroon" == color or "Bean" == color or "Deep Bronze" == color or "Deep Forest Green" == color):    
            #await message.channel.send("D/G " + color)
            strppp = "nothing"
        elif( "White" == color ):   
            #print("Char Images Showed")
            strpp = "nothing"
        elif( "Seance" == color and "Lookup" in message.embeds[0].title ):  
            #print("Char Lookup Executed") 
            strppp = "nothing"
        elif( "Port Gore" == color or "Meteorite" == color or "Jacarta" == color or "Daisy Bush" == color or "Honey Flower" == color or "Mirage" == color or "Seance" == color): 
            strppp = "nothing"
            #await message.channel.send("D/E " + color)         
        elif( "Orchid" == color or "Fuchsia" == color or "Lavender" == color or "Purple Plum" == color or "Lavender Magenta" == color or "Grape" == color or "Blush Pink" == color): 
            strppp = "nothing"
            #await message.channel.send("Z/E " + color)
            print("Found potential zeta in server " + message.guild.name)
            user = client.get_user(UID)
            await user.send("Potential Zeta Found in " + message.guild.name + "\nLink: " + message.jump_url)            
        else:  
            user = client.get_user(UID)
            await user.send("Unknown color: " + color + " found in " + message.guild.name + "\nLink: " + message.jump_url)
            #await message.channel.send("Color Unknown. Color Name: " + color)   
            print("Color Unknown. Color Name: " + color)            
        
    await client.process_commands(message)
      
@client.command()
async def invite(ctx):
    embed=discord.Embed(color=0x88c4dd)
    embed.add_field(name="Spawned", value="[Want to invite the bot to your server? Use this link!](https://discord.com/oauth2/authorize?client_id=438877051508883456&permissions=8&scope=bot)", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def botinfo(ctx):
    guildnum = str(len(ctx.bot.guilds))
    usernum = str(len(ctx.bot.users))
    count = 0
    for g in ctx.bot.guilds:
        count = count + len(g.members)
    game = discord.Game("z!help | z!invite | Spotting zetas in " + str(len(client.guilds)) + " servers for " + str(count) + " otaku!")
    await client.change_presence(status=discord.Status.online, activity=game)
    await ctx.send("Updated Status.\nGuilds: " + guildnum + "\nUsers: " + str(count))
    return 

@client.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(client.latency, 1)))
    
@client.command()
async def blue(ctx):
    client.BLUE = not client.BLUE
    await ctx.send("Blue is now " + str(client.BLUE))

@client.command()
async def black(ctx):
    client.BLACK = not client.BLACK
    await ctx.send("Black is now " + str(client.BLACK))

@client.command()
async def white(ctx):
    client.WHITE = not client.WHITE
    await ctx.send("White is now " + str(client.WHITE))

@client.command()
async def red(ctx):
    client.RED = not client.RED
    await ctx.send("Red is now " + str(client.RED))
    
@client.command()
async def yellow(ctx):
    client.YELLOW = not client.YELLOW
    await ctx.send("Yellow is now " + str(client.YELLOW))
    
@client.command()
async def green(ctx):
    client.GREEN = not client.GREEN
    await ctx.send("Green is now " + str(client.GREEN))
    
@client.command()
async def debug(ctx, chid, mid):
    c = ctx.guild.get_channel(int(chid))
    m = await c.fetch_message(int(mid))
    code = str(m.embeds[0].color)[1:]     
    requrl = "https://www.thecolorapi.com/id?hex=" + code   
    r = requests.get(requrl)    
    jsonResponse= r.json()
    color = str(jsonResponse["name"]["value"])
    await ctx.send(color)
    

@client.command()
async def boxstatus(ctx):
    await ctx.send("Yellow: " + str(client.YELLOW) + "\nBlue: " + str(client.BLUE) + "\nBlack: " + str(client.BLACK) + "\nWhite: " + str(client.WHITE) + "\nRed: " + str(client.RED) + "\nGreen: " + str(client.GREEN) )

    

      
    

client.run(TOKEN)
            
