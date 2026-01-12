

class Student:
    @property
    def password(self):
        print("getter is called")
        return self._password
    
    @password.setter
    def password(self, newPass):
        print("setter is called")
        if len(newPass) < 10:
            print("password too small")
            return
        self._password = newPass

    def __init__(self, name, age, location, password):  
        self.name = name
        self.age = age
        self.location = location
        self._password = password


student1 = Student("Adarsh", 20, "India", "9793")
print(student1.name, student1.age, student1.location ,student1.password)

