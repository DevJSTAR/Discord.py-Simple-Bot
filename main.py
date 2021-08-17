import discord
import os
import keep_alive
from discord.ext import commands

client = commands.Bot(command_prefix=">>")
token = os.environ.get("DISCORD_BOT_SECRET")


f = open("rules.txt", "r")
rules = f.readlines()

@client.event
async def on_ready():
    print("Bot is ready")

@client.command(aliases=['rules'])
async def rule(ctx,*,number):
    await ctx.send(rules[int(number)-1])

@client.command(aliases=['c', 'purge', 'p'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=3):
    await ctx.channel.purge(limit = amount)

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason= "No Reason Provided"):
    await member.send("You have been kicked from **𝔽𝕌ℕ 𝔾𝕌𝕐𝕊** server for "+reason)
    await member.kick(reason=reason)

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason= "No Reason Provided"):
    await ctx.send(member.name + " has been from banned **𝔽𝕌ℕ 𝔾𝕌𝕐𝕊** server for "+reason)
    await member.ban(reason=reason)

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('>>')

    for banned_entry in banned_users:
        user = banned_entry.user

        if(user.name, user.discriminator)==(member.name,member_disc):

            await ctx.uild.unban(user)
            await ctx.send(member.name +" has been unbanned!")
            return

    await ctx.send(member+"was not found!")

keep_alive.keep_alive()
client.run(token)
