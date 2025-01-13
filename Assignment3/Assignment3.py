class Element: 
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

hydrogen = Element('Hydrogen', 'H', 1)
hydrogen.name
hydrogen.symbol
hydrogen.number

print(hydrogen.name, hydrogen.symbol, hydrogen.number)
