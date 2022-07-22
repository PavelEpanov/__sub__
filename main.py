class Number:
    def __init__(self, start): # Для Number(start)
        self.data = start
    def __sub__(self, other): # Для экземпляр - other
        return Number(self.data - other) # Результатом будет новый экземпляр

X = Number(5) # Number.__init__(X, 5)
Y = X - 2 # Number.__sub__(X, 2)
print(Y.data) # Y является новым экземпляром