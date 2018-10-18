class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def __str__(self):
        return "{} {}".format(self.firstname, self.lastname)



if __name__ == "__main__":
      ralph = Person("ralph", "Fernandez")
      print (ralph)

#inheritance
class Student (Person):
    def __init__(self,firstname,lastname,school = ""):
        super().__init__(firstname, lastname)
        self.school = school

        