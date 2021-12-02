from mcpi.minecraft import Minecraft
mc = Minecraft.create()
message = ("Last Christmas I gave you my heart, but the very next day you sold it on Ebay. This year, to save me from tears, I'll give it to someone on Craigslist!")
mc.postToChat(message)