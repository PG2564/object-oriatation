class Fruits:
    def __init__(self,name,color):
        self.name = name
        self.color = color
 
Apple = Fruits("Apple","Green")
Mengo = Fruits("Mango","yellow")

print(f"Hey I'm{Apple.name}and my color is{Apple.color}")
print(f"Hey I'm{Mengo.name}and my color is{Mengo.color}")