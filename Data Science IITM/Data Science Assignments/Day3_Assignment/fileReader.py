'''
File Reader
A program to read first 5 lines of any .py file
Handle file not found errors
Display line numbers

'''

def read_content(file_name):
    content=[]
    try:
        myFile = open(file_name,'r')
        for i in range(5):
            content.append(myFile.readline())
        myFile.close()
    except FileNotFoundError as e:
        print(f"Error: {e}")
    return content

def display(content):
    for i in range(len(content)):
        print(f"[{i+1}] : {content[i]}")

def write_File(file_name,content):
    try:
        file = open(file_name,'a')
        file.write(content)
        file.close()
    except FileNotFoundError as e:
        print(e)
        print("Creating a new File")
        myfile=open(file_name,'x')
        myfile.close()
    except Exception as e:
        print(e)


def main():
    myFile = "testing.py"
    for i in range(5):
        write_File(myFile,f"This is line {i+1}\n")
    display(read_content(myFile))

main()