import discord
import os 
import random

intents = discord.Intents.default()
intents.message_content = True

def dice_roll(roll, keep):

    if roll.isdigit()==False or keep.isdigit()==False:
        return "Whoops, something not entered correctly"

    # if type(roll)!=int or type(keep)!=int or keep>roll or roll<0 or keep<0: #this line checks to make sure input is entered correctly
    #     return "Whoops, something not entered correctly"
    results=[]
    current_roll=0
    not_kept=roll-keep+1
    c_not_kept=1 

    
    while current_roll<roll:#this while loop is rolling the dice
        results.append(random.randint(1, 10))
        current_roll=current_roll+1

    results.sort(reverse=True) #sorts, highest to lowest

    while c_not_kept<not_kept: #this while loop gets rid of dice that are not being kept
        results.pop(-1)
        c_not_kept=c_not_kept+1 
    
    return results

def roll_total(dice): #total when added all dice results
    if type(dice)==str:
        return "try entering a format similar to this: $roll "
    total=0
    for die in dice:
        total=total+die

    return total


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
num_list=[]
@client.event
async def on_ready():
    print(f'Successfully connected! Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$roll'):
        message_r=reversed(message.content.split())

        message_r_list = list(message_r)

        print("list",message_r_list)

        keepin=int(message_r_list[0])
        rollin=int(message_r_list[2])
        print(type(rollin))
        print(type(keepin))
        winnings=dice_roll(rollin, keepin)
        total=roll_total(winnings)
        everything=(winnings, total)
        await message.channel.send(everything)
    
    # if message.content.startswith('$keep'):
        # message_r=reversed(message.content.split())

        # message_r_list = list(message_r)

        # print(message_r_list[0])

        # keepin=message_r_list[0]

        # print(keepin)

        # winnings=dice_roll(rollin,keepin)

        # results=list(winnings, roll_total(winnings))
        # results=["test", 24]
        # await message.channel.send(results)

    # if message.content.startswith('$keep'):
# winnings=dice_roll(7, 4)

# print(winnings, roll_total(winnings))

client.run(os.environ['DISCORD_TOKEN'])