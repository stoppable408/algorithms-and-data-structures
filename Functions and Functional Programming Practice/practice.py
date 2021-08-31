

#Practice in writing callable classes with also lambda expressions
class Robot():

    def __init__(self, name):
        self.name = name
    

    def __call__(self):
        string = "My name is " + self.name
        print(string)
    
    def sorted_speech(self, sentence):
        sorting = lambda sentence: "".join(sorted(sentence)).strip()
        print(sorting(sentence))





if __name__ == '__main__':
    robot = Robot("Jerry Smith")
    robot()
    robot.sorted_speech("time is just a construct")

