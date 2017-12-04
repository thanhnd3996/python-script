"""
Python supports OO technology.
And it is a duck-typed OO language.
It is the same with Ruby and has some different from other class-typed OO languages suck as Java and C#.
Moreover, python features a dynamic data-type system.
To understand clearly, you can see the example below :
1. This example shows us about four pillars of OOP:
    1.1_Encapsulation: If we talk about an animal, we'll recognize that it has name, chirp, eyes, heart, sex habits,...
        It's very complex. So, now,  treat it as a human, we'll just see this animal is a complete subject.
        He know exactly all about himself: his name, how to say hello, his sex habits,...
        We don't know about his information, so we'll use method() to ask him and get the info from him.
    1.2_Abstraction: we create class Animal to represent for all the animals: Dog, Cat,...
    1.3_Inheritance: Cat, Dog and all the animals'll be subclass of Animal, they extend Animal's attributes and methods.
    1.4_Polymorphism: We create a class named Zoo, it will hold other animals.
        In this class, we have method say_hello_all() to call to method say_hello() of each animals.
        Which operations these method'll execute depend on each animal.
2. In class Zoo, when a object is created, it'll create a list named as animals first.
    This list don't know what type of object or data it holds.
    When the object uses method add() to hold Cat, Dog,..., the list knows that it was born to hold Animal objects.
    So, as you can see, the dynamic data-type system works at runtime.
3. Duck class doesn't extend Animal class. But when we add a duck object to the list of animals, don't have any error.
    And when we use method say_hello_all() to animals, the duck object's method is also executed.
    Because Python is a duck-typed OO language, so in this case, Zoo doesn't have to know Duck is a animal.
    Just has method say_hello(), Duck'll be recognized by Zoo as an animal.
    We can say that: " Ducks don't have to know they are black or white. Just have chirp like a duck, they will be duck.
    And you can see, i don't have to write method say_hello() in Animal class.
    In Python, we also don't have 'interface'-keyword like Java, C# ( Ruby doesn't even have @Override )
"""


class Animal:
    def __init__(self, name):
        self.name = name


class Cat(Animal):
    def say_hello(self):
        print "Meow, my name is ", self.name


class Dog(Animal):
    def say_hello(self):
        print "Woof woof, my name is ", self.name


class Duck:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print "Trump, my name is ", self.name


class Zoo:
    def __init__(self):
        self.animals = []

    def add(self, animal):
        self.animals.append(animal)

    def say_hello_all(self):
        for animal in self.animals:
            animal.say_hello()


z = Zoo()
z.add(Cat("Kitty"))
z.add(Dog("Pluto"))
z.add(Duck("Donald"))
z.say_hello_all()     """
Python supports OO technology.
And it is a duck-typed OO language.
It is the same with Ruby and has some different from other class-typed OO languages suck as Java and C#.
Moreover, python features a dynamic data-type system.
To understand clearly, you can see the example below :
1. This example shows us about four pillars of OOP:
    1.1_Encapsulation: If we talk about an animal, we'll recognize that it has name, chirp, eyes, heart, sex habits,...
        It's very complex. So, now,  treat it as a human, we'll just see this animal is a complete subject.
        He know exactly all about himself: his name, how to say hello, his sex habits,...
        We don't know about his information, so we'll use method() to ask him and get the info from him.
    1.2_Abstraction: we create class Animal to represent for all the animals: Dog, Cat,...
    1.3_Inheritance: Cat, Dog and all the animals'll be subclass of Animal, they extend Animal's attributes and methods.
    1.4_Polymorphism: We create a class named Zoo, it will hold other animals.
        In this class, we have method say_hello_all() to call to method say_hello() of each animals.
        Which operations these method'll execute depend on each animal.
2. In class Zoo, when a object is created, it'll create a list named as animals first.
    This list don't know what type of object or data it holds.
    When the object uses method add() to hold Cat, Dog,..., the list knows that it was born to hold Animal objects.
    So, as you can see, the dynamic data-type system works at runtime.
3. Duck class doesn't extend Animal class. But when we add a duck object to the list of animals, don't have any error.
    And when we use method say_hello_all() to animals, the duck object's method is also executed.
    Because Python is a duck-typed OO language, so in this case, Zoo doesn't have to know Duck is a animal.
    Just has method say_hello(), Duck'll be recognized by Zoo as an animal.
    We can say that: " Ducks don't have to know they are black or white. Just have chirp like a duck, they will be duck.
    And you can see, i don't have to write method say_hello() in Animal class.
    In Python, we also don't have 'interface'-keyword like Java, C# ( Ruby doesn't even have @Override )
"""


class Animal:
    def __init__(self, name):
        self.name = name


class Cat(Animal):
    def say_hello(self):
        print "Meow, my name is ", self.name


class Dog(Animal):
    def say_hello(self):
        print "Woof woof, my name is ", self.name


class Duck:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print "Trump, my name is ", self.name


class Zoo:
    def __init__(self):
        self.animals = []

    def add(self, animal):
        self.animals.append(animal)

    def say_hello_all(self):
        for animal in self.animals:
            animal.say_hello()


z = Zoo()
z.add(Cat("Kitty"))
z.add(Dog("Pluto"))
z.add(Duck("Donald"))
z.say_hello_all()
