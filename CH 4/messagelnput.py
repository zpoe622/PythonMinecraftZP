from mcpi.minecraft import Minecraft
mc = Minecraft.create()
username = input("please enter username: ")
message = input("Enter your message: ")
while message != "exit":
    print(message)
    message = input("Please enter a message.")
    if message == "abort":
        break
else:
    print("User has left the chat.")
mc.postToChat(username + message)
