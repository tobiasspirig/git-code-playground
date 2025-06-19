class Footballers:
    def __init__(self, age, name, team):

        self.age = age
        self.name = name
        self.team = team


    
    def market_value(self):
        if self.age <= 25:
            print(f"{self.name}'s Market Value is expected to rise.")
        else:
           print(f"{self.name}'s Market Value is expected to fall.")

messi = Footballers(36, "Lionel Messi", "Miami")

messi.market_value()
staubli = Footballers(24, "Tim Staubli", "FC Wil")

staubli.market_value()        
