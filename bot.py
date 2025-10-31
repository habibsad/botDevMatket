import discord
from discord.ext import commands
import os

# ⚡ إعداد الـ intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # مهم للترحيب بالأعضاء

# ⚡ إنشاء البوت
bot = commands.Bot(command_prefix="!", intents=intents)

# ⚡ حدث الترحيب
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="👋︱welcome")
    if channel:
        embed = discord.Embed(
            title="👋 Welcome to DevMarket!",
            description=(
                f"Welcome {member.mention} to **{member.guild.name}**! 🌟\n\n"
                f"📚 From here you can explore our community:\n"
                f"💬 Check out <#1433513950695133325> to talk with others!\n"
                f"📢 See news in <#1433515175612387499>!\n"
                f"🧩 Get your roles in <#1433513634675560498>!\n\n"
                f"Enjoy your stay! 🚀"
            ),
            color=0x3498db  # لون المستطيل (أزرق)
        )
        embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
        embed.set_image(url="https://cdn.discordapp.com/attachments/1433513634675560498/1433735631024033823/openart-8e45abdd-37b2-43fd-b923-94ffd8601dae.png")
        embed.set_footer(text="DevMarket Community | We’re glad to have you 💙")

        await channel.send(embed=embed)

# ⚡ تشغيل البوت مع توكن مخفي في Environment Variable
bot.run(os.getenv("TOKEN"))
