# CREATE CLASS AND OBJECT
class myclass:
    x =5

d1 = myclass()
print(d1.x)



class myclass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunction(self):
        print("my name is " + self.name)

p1 = myclass("Dio", 23)
# Delete object
# del p1
print(p1.name, p1.age)


# The __init__() Method
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = MyClass("Dio", 23)

print(p1.name, + p1.age)


class myclass:
    def __init__(self, name, age = 23):
        self.name = name
        self.age = age

p1 = myclass("dio")
p2 = myclass("Deko", 21)
print(p1.name, p1.age)
print(p2.name, p2.age)


class myclass:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

p1 = myclass("Deko", 21, 'mogadishu', 'Somalia')
print(p1.name, p1.age, p1.city, p1.country)

class myclass:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunction(dio):
        print("waa", dio.name)

    def dada(da):
        print("da'deydu waa", da.age)
p1 = myclass("Dio", 23)
p1.myfunction()
p1.dada()





class myclass:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        print(f"The info of the car is {self.brand} {self.model} {self.year}")
brand_input = input("enter the brand: " )
model_input = input("enter the  model: ")
year_input = input("enter the  year: ")
p1 = myclass(brand_input, model_input, year_input)
p1.info()

class myclass:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return "Hello," + self.name

    def myfucntion(self):
        message = self.greet()
        print(message + "! Welcome to our website.")
p1 = myclass("Dio")
p1.myfucntion()



class myclass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = myclass("Dio", 23)
print(p1.age)
p1.age = 24
print(p1.age)
        


class myclass:
    status = "SINGLE"
    def __init__(self, name):
        self.name = name

p1 = myclass("Dio")
print(p1.name)
print(p1.status)


class myclass:
    status = "SINGLE"
    def __init__(self, name):
        self.name = name
    def myfunction(self):
        d = self.name
        print(d + " waxaa thy " + self.status)
    
p1 = myclass("Dio")

p1.status = "SINGLE"
dd = p1.myfunction()
print(p1.name, p1.status, )
print(p1.myfunction())




class calculator:
    def add(self, a,b):
        return a + b 
    def multply(self,a,b):
        return a * b 
cal = calculator()
print(cal.add(5, 2))
print(cal.multply(3,4))


class playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def addsong(self, song):
        self.songs.append(song)
        print(f"Added {song}")

    def remove(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removes {song}")

    def showsongs(self):
        print(f"playlist: {self.name}")
        for song in self.songs:
           print(f"{song}")



my_playlist = playlist("songs")
my_playlist.addsong("Hamdi quuen")
my_playlist.addsong("Hayart quuen")
my_playlist.addsong("Hayart quuen")
my_playlist.addsong("Hayart quuen")
my_playlist.addsong("Hayart quuen")
my_playlist.addsong("Hayart quuen")
my_playlist.addsong("Hayart quuen")
my_playlist.remove("Hayart quuen")

my_playlist.showsongs()

my_playlist.remove("Hamdi quuen")
print(my_playlist.songs)


class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()



class myclass:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(f"{self.fname} {self.lname}")
x = myclass("Abdikani", "Hassan")
x.printname()


class info(myclass):
    pass

x2 = info("Hawo", "Mohamoud")
x2.printname()