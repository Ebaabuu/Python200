class Counter:
    def __init__(self):
        self.reset()
    def getValue(self):
        return self._value
    
    def click(self):
        self._value += 1
    
    def reset(self):
        self._value = 0

click1 = Counter()

userInput = ""
while userInput != "q":
    userInput = input("")
    if userInput == "0":
        click1.reset()
    else:
        click1.click()
print(click1.getValue())