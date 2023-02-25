class Computer:
    numberOfGraphics = 1

    def __init__(self, *ram):
        self.ram = int(ram[0])
        self.cpu = ram[1]
        self.lap = self.Laptop()
        print("inside init")

    def config(self):
        print("i5, 16gb, 1TB")

    def display():
        numberOfGraphics = 5
        print("graphics: ", numberOfGraphics)

    def printInfo(self):
        print("Details: ", self.cpu, ", ", self.ram)

    def doSomething():
        print("I am a static method")

    def show(self):
        print("I am computer with ram: ", self.ram)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = "dell"

        def show(self):
            print("Laptop brand: ", self.brand)


com1 = Computer('8', 'i7')
com1.show()

lap=Computer.Laptop()
lap.show()

# Computer.display()
#
# com1=Computer('24','i7')
# # com2=Computer(16)
#
# Computer.doSomething()
#
# com1.printInfo()
#
# com1.numberOfGraphics=2
#
# Computer.numberOfGraphics=2
#
# print(com1.numberOfGraphics)
# # print(com2.numberOfGraphics)
#
# print(Computer.numberOfGraphics)


# Computer.config(com1)

# com1.config()
