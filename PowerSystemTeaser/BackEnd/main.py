class ElementSelection:
    def __init__(self):
        self.fire_crystals = 10
        self.water_crystals = 10
        self.earth_crystals = 10
        self.air_crystals = 10

    def fire (self):

        print("You have chosen FIRE!!!")
        print(f"Crystals: {self.fire_crystals} PT(Phoenix Tears) ")

    def water (self):
        print("You have chosen WATER!!!")
        print(f"Crystals: {self.water_crystals} NT(Nereld Tears) ")

    def earth (self):
        print("You have chosen EARTH!!!")
        print(f"Crystals: {self.earth_crystals} CB(Celestial Breathstones) ")

    def air (self):
        print("You have chosen AIR!!!")
        print(f"Crystals: {self.air_crystals} GT(Granite Tears) ")


class ElementalRoadmap:
    def __init__ (self, chosen_element):
        self.element = chosen_element
        self.connections = {}

    def add_connection(self, secondary_element, relationship):
        if secondary_element not in self.connections:
            self.connections[secondary_element] = []
        self.connections[secondary_element].append(relationship)

    def draw_roadmap(self):
        print(f"    [{self.element}]")
        for secondary_element, relationships in self.connections.items():
            print(f"   |")
            print(f"   v")
            print(f"   [{secondary_element}] --> ({', '.join(relationships)})")


print("Welcome to Elemental Dungeon of the Glitch System!")
print("Please Choose ONE from following FOUR Fundamental Elements...")

element = None 

while True:
    print("1. FIRE")
    print("2. WATER")
    print("3. EARTH ")
    print("4. AIR")

    print("Please type the reference number of preferred element of yours....")
    user_element = int(input())

    if user_element == 1:
        element = "FIRE"
        break 

    elif user_element == 2:
        element = "WATER"
        break 

    elif user_element == 3:
        element = "EARTH"
        break 

    elif user_element == 4:
        element = "AIR"
        break  

    else:
        print("Invalid Input!!")

chosen_element = ElementSelection()

if element == "FIRE":
    chosen_element.fire()
elif element == "WATER":
    chosen_element.water()
elif element == "EARTH":
    chosen_element.earth()
elif element == "AIR":
    chosen_element.air()

roadmap = ElementalRoadmap(element)
roadmap.add_connection("STEAM", "Fused with WATER")
roadmap.add_connection("LAVA", "Fused with EARTH")
roadmap.add_connection("INFERNO", "Fused with AIR")

roadmap.draw_roadmap()