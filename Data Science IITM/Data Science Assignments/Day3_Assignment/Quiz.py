def createFile(file_name):
    try:
        f=open(file_name,'x')
        f.close()
        #print("File created successfully!")
    except Exception as e:
        print(e)

def deleteFile(file_name):
    import os
    os.remove(file_name)
    #print("File deleted successfully!")

def add_Question(question,answer,file1="questions.txt",file2="answers.txt"):
    try:
        file1=open(file1,'a')
        file1.write(f"{question}")
        file1.write("\n")
        file1.close()

        file2=open(file2,'a')
        file2.write(f"{answer}")
        file2.write("\n")
        file2.close()
        print("Question added successfully!")
    except Exception as e:
        print(e)

def get_Question(question_number,file="questions.txt"):
    file=open(file,'r')
    question = file.readlines()
    file.close()
    return question[question_number-1]

def get_Answer(question_number,file="answers.txt"):
    file=open(file,'r')
    question = file.readlines()
    file.close()
    return question[question_number-1]

def updateScore(score,file="score.txt"):
    try:
        file3=open(file,'r')
        previous_score=int(file3.read())
        score = score+previous_score
        file3.close()

        file3 = open(file,'w')
        file3.write(str(score))
        file3.close()
    except Exception as e:
        print(e)

def get_Score(file="score.txt"):
    try:
        f=open(file,'r')
        content = f.read()
        print(content)
        return int(content)
        f.close()
    except Exception as e:
        print(e)

def endQuiz():
    deleteFile("questions.txt")
    deleteFile("answers.txt")
    deleteFile("score.txt")

def number_of_Questions():
    try:
        file=open("questions.txt",'r')
        queList = file.readlines()
        return len(queList)
    except Exception as e:
        print(e)

def setQuestions():
    createFile("questions.txt")
    createFile("answers.txt")
    add_Question("Who is the Prime Minister of India?", "Narendra Modi")
    add_Question("Who is the current President of India?", "Droupadi Murmu")
    add_Question("Who was the first Prime Minister of India?", "Jawaharlal Nehru")
    add_Question("Who is the current Home Minister of India?", "Amit Shah")
    add_Question("Who was the first woman Prime Minister of India?", "Indira Gandhi")
    # add_Question("Who is the current Chief Minister of Delhi?", "Arvind Kejriwal")
    # add_Question("Who is the current Defence Minister of India?", "Rajnath Singh")
    # add_Question("Who is the Governor of the Reserve Bank of India?", "Shaktikanta Das")
    # add_Question("Who is the current External Affairs Minister of India?", "S. Jaishankar")
    # add_Question("Who was the architect of the Indian Constitution?", "B. R. Ambedkar")

def startQuiz():
    name=input("Enter your name:")
    createFile("score.txt")
    f=open("score.txt",'w')
    f.write('0')
    f.close()
    marks_per_question = 5
    for i in range(number_of_Questions()):
        print("_"*50)
        print(f"Question{i+1} : {get_Question(i+1)}".strip())
        import random as r
        import random_names as rn
        options=[]
        person_list = rn.random_person_list()
        while len(options)<3:
            random_person = person_list[r.randint(0,rn.number_of_persons())]
            if random_person not in options:
                options.append(random_person)

        actual_answer = get_Answer(i+1).strip()
        options.insert(r.randint(0,3),actual_answer)
        for i in range(4):
            print(f"option {i+1}: {options[i]}")
        user_input = int(input("Enter the option:"))
        if options[user_input-1] == actual_answer:
            print("Correct Option!")
            updateScore(marks_per_question)
        else:
            print("Incorrect Option!")
    print(f"{name} , You Scored: {get_Score()} out of {number_of_Questions()*5}")



def display(size):
    for i in range(size):
        print(f"Q{i+1} : {get_Question(i+1)}\n Ans{i+1}: {get_Answer(i+1)}\n{"_"*30}\n")



def main():
    setQuestions()
    startQuiz()
    endQuiz()

main()