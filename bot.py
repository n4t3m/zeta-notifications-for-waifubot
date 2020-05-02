import discord
from discord.ext import commands
import requests
import setup

description = "Type $info to see more information."
TOKEN = setup.TOK
client = commands.Bot(command_prefix='$', description=description, help_command=None)
path = './data.txt'


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    game = discord.Game("WaifuBot! | Mention for Information!")
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
        
        
    if message.author.id == 472141928578940958 and len(message.embeds) > 0 and "Character" in message.embeds[0].title:
        serverid = message.guild.id
        file = open(path,'r')
        temp = ""
        lines = file.readlines()
        for line in lines:  
            if str(message.guild.id)in line.strip("\n"):
                temp = line
        split = temp.split(':');    
        ping = split[1]
        #print("Ping :" + ping)
        code = str(message.embeds[0].color)[1:]     
        apiurl = "https://www.thecolorapi.com/id?hex=" + code   
        r = requests.get(apiurl)    
        jsonResponse= r.json()
        color = str(jsonResponse["name"]["value"])
        ##print("Color: " + color)
        if( "Mineral Green" == color or "Tom Thumb" == color or "Limed Spruce" == color):   
            await message.channel.send("Rarity: Alpha/Beta")    
        elif( "Bush" == color or "Metallic Bronze" == color or "Woodland" == color or "TBD" == color):  
            await message.channel.send("Rarity: Beta/Gamma")
        elif( "Palm Leaf" == color or "Irish Coffee" == color or "Punga" == color or "Bronze Olive" == color or "Turtle Green" == color or "Palm Leaf" == color or "Jambalaya" == color or "Cioccolato" == color or "Gable Green" == color):    
            await message.channel.send("Rarity: Delta/Gamma")
        elif( "White" == color ):   
            #print("Char Images Showed")
            strpp = "nothing"
        elif( "Seance" == color and "Lookup" in message.embeds[0].title ):  
            #print("Char Lookup Executed") 
            strppp = "nothing"
        elif( "Port Gore" == color or "Meteorite" == color or "Jacarta" == color  or "Seance" == color):    
            await message.channel.send("Rarity: Delta/Epsilon")         
        elif( "Orchid" == color or "Fuchsia" == color or "Lavender" == color or "Purple Plum" == color or "Lavender Magenta" == color or "Grape" == color): 
            await message.channel.send("Rarity: Zeta/Epsilon. Pinging User. " + ping)
            print("Found potential zeta in server " + message.guild.name)              
        else:   
            await message.channel.send("Color Unknown. Color Name: " + color)   
            print("Color Unknown. Color Name: " + color)            
         
        
        

        
    if message.content.startswith('$setuser'):
        if( message.guild.owner_id != message.author.id ):  
            await message.channel.send("Error. You must be the server owner to use this command.")
            return
        if( "$setuser" == message.content ):    
            await message.channel.send("Usage: $setuser <ping>")
            return
        split = message.content.split(' ');
        if( len(split) > 2  ):  
            await message.channel.send("Error. Too Many Paramters.")
            return
        entry = str(message.guild.id) + ":" + split[1]
        response = ""
        file = open(path,'r')
        lines = file.readlines()        
        file.close()
        tempfile = open(path,'w')
        for line in lines:  
            if str(message.guild.id) not in line.strip("\n"):
                tempfile.write(line)
            else:
                response = response + "Updating Server's Mentioned User...\n"
        tempfile.write("\n" + entry)
        tempfile.close()
        await message.channel.send(response + "New User Set. I will now ping " + split[1] + " when potential Zetas spawn!")
        file = open(path,'r')
        ##removing black lines
        lines = file.readlines()        
        file.close()
        tempfile = open(path,'w')
        for line in lines:  
            if "" != line.strip("\n"):
                tempfile.write(line)
        tempfile.close()
        print("New Database Entry")
        
    await client.process_commands(message)
  
  
@client.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
    
@client.command()
async def help(ctx):
    embed=discord.Embed(title="Help/Information", description="This bot was created by  in order to notify users when a high-rarity waifu is spawned by WaifuBot.", color=0xd256d7)
    embed.set_thumbnail(url="https://66.media.tumblr.com/079c3723edc4d4e39bae11d4f4f77919/tumblr_peasla2ztT1xdtu9bo1_r1_250.png")
    embed.add_field(name="Want Zeta Notifications in YOUR Server?", value="Add the bot using this link: https://bit.ly/ZetaNotifs", inline=False)
    embed.add_field(name="Want to host your instance of the bot?", value="GH Repo Coming Soon", inline=False)
    embed.add_field(name="How do I work?", value="When a Zeta/pink waifu spawns, this bot will mention the user specified by the owner of the server. To set the person who will be notified when a Zeta spawns, use $setuser <ping the user>. Additionally, the bot lists rarity of each spawn.", inline=False)
    embed.set_footer(text="Made by Nathan Melwani/NateM135, a student entering Purdue University.")  
    await ctx.send(embed=embed)
    return
    
@client.command()
async def invite(ctx):
    embed=discord.Embed(color=0x88c4dd)
    embed.add_field(name="Zeta Collector Bot Invite", value="Bot Invite Link: https://bit.ly/ZetaNotifs", inline=False)
    await ctx.send(embed=embed)  
    

client.run(TOKEN)
            