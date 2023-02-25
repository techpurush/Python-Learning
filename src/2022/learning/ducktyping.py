class PyCharm:
    def execute(self):
        print("Compiling\nRunning")

class Eclipse:
    def execute(self):
        print("Spell Check\nCompiling\nRunning")

class Laptop:
    def code(self,ide):
        ide.execute()


ide=Eclipse()

lap1=Laptop()

lap1.code(ide)