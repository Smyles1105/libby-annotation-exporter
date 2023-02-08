import mariadb
import sys

def create_db_cursor():
    print("Attempting to connect to MariaDB now!")
    try:
        con = mariadb.connect(
            user="",
            password="",
            host="localhost",
            port=3306,
            database="books"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    return con.cursor()

def create_db(): #TODO: Finish the database creation queries
    print("Creating the database")
    cursor = create_db_cursor()
    cursor.execute("""
    CREATE TABLE book(
    ISBN int PRIMARY KEY,
    title VARCHAR(80),
    # author VARCHAR(40),
    # publisher VARCHAR(50),
    url VARCHAR(100),
    color CHAR(7));
    """)
    print("Query Executed!")
    cursor.execute("""
    CREATE TABLE annotation(
    annotationID int PRIMARY KEY,
    quote,
    note,
    color
    );
    """)
    print("Query Executed!")
    cursor.execute("""
        CREATE TABLE author(
        authorID int PRIMARY KEY,
        );
        """)
    print("Query Executed!")
    cursor.execute("""
        CREATE TABLE publisher(
        publisherID int PRIMARY KEY,
        );
        """)
    print("Query Executed!")
    cursor.execute("""
        CREATE TABLE publishes(
        publisherID int,
        ISBN int,
        CONSTRAINT fkn FOREIGN KEY (publisherID) REFERENCES publisher(publisherID) ON DELETE X ON UPDATE X,
        CONSTRAINT fkn FOREIGN KEY (ISBN) REFERENCES book(ISBN) ON DELETE X ON UPDATE X,
        PRIMARY KEY(publisherID, ISBN)
        );
        """)
    print("Query Executed!")
    cursor.execute("""
        CREATE TABLE writes(
        authorID int,
        ISBN int,
        CONSTRAINT fkn FOREIGN KEY (authorID) REFERENCES author(authorID) ON DELETE X ON UPDATE X,
        CONSTRAINT fkn FOREIGN KEY (ISBN) REFERENCES book(ISBN) ON DELETE X ON UPDATE X,
        PRIMARY KEY(authorID, ISBN)
        );
        """)
    print("Query Executed!")
    cursor.execute("""
        CREATE TABLE consists_of(
        ISBN int,
        annotationID int,
        CONSTRAINT fkn FOREIGN KEY (ISBN) REFERENCES book(ISBN) ON DELETE X ON UPDATE X,
        CONSTRAINT fkn FOREIGN KEY (annotationID) REFERENCES annotation(annotationID) ON DELETE X ON UPDATE X,
        PRIMARY KEY(ISBN, annotationID)
        );
        """)
    print("Query Executed!")


def add_annotation_to_db():
    #TODO: Implement function, basically need to add python code for the following:
    #Creating a new row with the data of the annotation into the annotation table that is already created.
    pass

def remove_annotation_from_db():
    pass

def insertquerynamehere_to_db():
    pass

#cursor = create_db_cursor()
create_db()