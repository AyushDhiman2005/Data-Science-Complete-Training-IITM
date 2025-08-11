import pymysql 

connection = pymysql.connect(host='locahost',user='root',password='ayush',autocommit=True)
mycursor=connection.cursor()

def create_Database(db_name):
    mycursor.execute(f'create database {db_name};')

def create_Table(t_name):
    mycursor.execute(f'''CREATE TABLE {t_name}(
    title VARCHAR(50) NOT NULL,
    author VARCHAR(50),
    year INT,
);'''
)
    
def view(table_name):
    mycursor.execute(f'select * from {table_name};')

def add(title,author_name,year,table_name='Book_Data'):
    mycursor.execute(f"insert into {table_name} values({title},{author_name},{year});")
    print('data inserted successfully!')

def search_books(author_name,table_name):
    mycursor.execute(f"select * from {table_name} where author={author_name};") 



def main():
    #Creating database
    create_Database('SQLite')
    create_Table('Book_Data')

    #Inserting Values
    add('To Kill a Mockingbird', 'Harper Lee', 1960),
    add('1984', 'George Orwell', 1949),
    add('The Great Gatsby', 'F. Scott Fitzgerald', 1925),
    add('Pride and Prejudice', 'Jane Austen', 1813),
    add('The Catcher in the Rye', 'J.D. Salinger', 1951)

    search_books('Jane Austen','Book_Data')

    connection.close()

main()