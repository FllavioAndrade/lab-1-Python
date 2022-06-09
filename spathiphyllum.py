class Planta:
    def __init__ (self, nome):
        self.nome = nome
        
    def gritar(self):
        if self.nome == "Spathiphyllum":
            print("Yes - Spathiphyllum is the best plant ever!")
            
        elif self.nome == "spathiphyllum":
            print("No, I want a big Spathiphyllum!")
        
        else:
            print("Spathiphyllum! Not [input]!")

nomePlanta = Planta(input("Digite o nome da planta: "))
nomePlanta.gritar()
            
