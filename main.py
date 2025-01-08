firstNumber = [8, 12, 6, 20,10]
secondNumber =[2,3,3,4,5]
numberOfProblems = len(firstNumber)

def calculate(typeOfproblem):
    numberOfCorrect =0
    correctAnswer =0
    for i in range(numberOfProblems):
        if typeOfproblem =="M":
            print(firstNumber[i], "*",secondNumber[i])
            correctAnswer = firstNumber[i]*secondNumber[i]
        else:
            print(firstNumber[i], "/",secondNumber[i])
            correctAnswer = firstNumber[i]/secondNumber[i]
        ans = int(input("Enter your answer: "))
        if ans ==correctAnswer:
            print("Correct!")
            numberOfCorrect+=1
        else:
            print("Sorry, incorrect!")
    return numberOfCorrect

def mainMenu():
    print("Welcome to my math Quiz")
    choice = input("Please select (M)ultiplication or (D)ivision:\n").upper()
    score = calculate(choice)*100/numberOfProblems
    print("Your score in the test:"+str(score) + "%")
    retake = input("Whant other oportunitie or take the other quiz,type (Y) for retake or (N) for exit:\n").lower()
    if retake =="y":
        mainMenu()
    else:
        input("thanks for using the mathquiz program, press enter to close...")
        exit()

mainMenu()