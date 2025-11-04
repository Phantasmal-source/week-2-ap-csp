# abstraction is when I hide
# the complex details for something 
# a lot more simple 

#personal information
#a function allows us to wrap data or personal information into a special box or enclosure for reuse
#define a function
# def personInformation():
#     question1 = input("How old are you?")
#     question2 = input("Where do you live")
#     question3 = input("what school do you go to")
#     print(question1 + question2 + question3)

# personInformation()
# personInformation()
# personInformation()

#make a function that guesses how old you are?

def GuessBorn():
    q1 = int(input("what year is it now"))
    q2 = int(input("what year were you born in"))
    answer = q1 - q2
    result = print(f'you are {answer} years old')

GuessBorn()