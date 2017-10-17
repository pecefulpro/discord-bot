
from discord.ext.commands import Bot

import secrets

titan_bot = Bot(command_prefix="!")

@titan_bot.event
async def on_read():
	print("Client logged in")

@titan_bot.command()
async def hello(*args):
	return await titan_bot.say("It's your boy")

@titan_bot.command()
async def rules(*args):
	return await titan_bot.say("""  __***	1.No spamming or flooding the chat with messages. 
		2.Do not type in ALL CAPS. No text walls or a large paragraphs of text. 
		3.No bashing or heated arguments to other people in the chat.
		4. No adult (18+), explicit, or controversal messages.
		5. No racist or degrading content (racial terms are not allowed).
		6. No excessively cursing.
		7. No advertising other sites/discord servers (Permission must be requested from Staff).
		8. No referral links.
		9. No begging or repeatedly asking for help in the chat, Repeatingly asking basic questions
		10. No offensive names.***__""")

titan_bot.run("Mjg4NzY1NzI2NjM3MDMxNDI0.C6CupA.6EtXIs3F7uUiEPU9BBpR6EyNm_s")


Good change , nice bot and keep trying :)

