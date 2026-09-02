class mynumbers:
    def __iter__(self):
        self.a =1
        return self
    def __next__(self):
        if self.a <=20:
            x =self.a
            self.a +=1
            return x
        else:
            raise StopIteration



def dio(x):
    return 5* x

def pw(x,y):
    return x**y

info = {
    "name" : "Ahmed",
    "age" : 32,
    "status" : "single"
}