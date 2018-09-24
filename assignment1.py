class Person:
    def __init__(self, name, email, phone, friends, greetings):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = friends
        self.greetings = greetings
        
        

    def num_friends(self):
        print(len(self.friends))

    def pretty_print(self):
        print("{2}'s Email: = {0}, {2}'s Phone = {1}".format(self.email,self.phone,self.name))

    def greet(self, other_person):
        self.greetings += 1
        print('Hello %s, I am %s!' % (other_person.name, self.name))

    def greeting_count(self):
        print(self.greetings)

    def __repr__(self):
        return '' % (self.name, self.email, self.phone)

   
    
sonny = Person("Sonny","sonny@hotmail.com","483-485-4948",[],0)
jordan = Person("Jordan","jordan@aol.com","495-586-3456",[],0)

sonny.greet(jordan)
jordan.greet(sonny)

sonny.pretty_print()
jordan.pretty_print()

jordan.friends.append(sonny)
sonny.friends.append(jordan)

jordan.num_friends()
sonny.num_friends()

sonny.greeting_count()
jordan.greeting_count()

