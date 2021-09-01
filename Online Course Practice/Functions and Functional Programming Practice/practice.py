

#Practice in writing callable classes with also lambda expressions
class Robot():

    def __init__(self, name):
        self.name = name
    
    #Callable class implementation 
    def __call__(self):
        string = "My name is " + self.name
        print(string)
    
    #function containing a lambda expression
    def sorted_speech(self, sentence):
        sorting = lambda sentence: "".join(sorted(sentence)).strip()
        print(sorting(sentence))

    #fuction utilizing non-keyword arguments
    def multiply_nums(self, *args):
        total = 1
        for item in args:
            total *= item
        print(total)

    #function utilizing keyword arguments
    def speech_protocal(self, **kwargs):
        for kwarg, value in kwargs.items():
            print("Key: "+ str(kwarg) + ", Value: " + str(value))

    #function utilizing position only operator
    def print_length(self,length, /):
       print(length)
    #function utilizing extended call syntax
    def color(self, red, green, blue, **kwargs):
        print("r = ", red)
        print("g = ", green)
        print("b = ", blue)
        print(kwargs)

    #Example of a function returning a local function
    def choose(self, param):
        def print_name():
            print(self.name)
        def print_age():
            print(self.age)
        if param != self.name:
            return print_age
        return print_name


    #Closure example
    def raise_to(self, exp):
        def raise_to_exp(x):
            return pow(x, exp)
        return raise_to_exp
if __name__ == '__main__':
    robot = Robot("Jerry Smith")
    robot()
    robot.sorted_speech("time is just a construct") 
    robot.multiply_nums(4,5,6,7)
    robot.speech_protocal(time=2184, name="Lennon", speed="412mph", height="890ft")
    robot.print_length(284)

    color_dict = {"red": 248, "green":123, "blue":998, "purple": 78923}
    robot.color(**color_dict)
    robot.choose("Jerry Smith")()

    square = robot.raise_to(2)
    print(square.__closure__)
    print(square(5))

