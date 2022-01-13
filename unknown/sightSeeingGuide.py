from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#add locations tp the dictionary
places = {'Living room': (76, 1, -61), 'Bedroom': (61, 9, -61)}

choice = ""
while choice != "exit":
    choice = input("Enter a location ('exit' to close): ")
    if choice in places:
        #store the dictionary item's value using its key (choice)
        location = places['Living room']
        #store the values stored in tje tuple in the x,y, and z variables
        x,y,z = location[0], location[1], location[2]
        mc.player.setTilePos(x,y,z)