class Student:
      def __init__(self,first_name,last_name,age,country):
          self.first_name=first_name
          self.last_name=last_name
          self.age=age
          self.country=country
          

      def greet(self):
          return f" Hello {self.first_name} and you stay in {self.country} "
      def full_name(self):
          return f"your full name is {self.first_name} {self.last_name}"
      def  birth_year(self):
          year=2022-self.age
          return f" your year of birth is",year
      def initials(self):
          return f"your initials are {self.first_name[0]}{self.last_name[0]}"

    
            
