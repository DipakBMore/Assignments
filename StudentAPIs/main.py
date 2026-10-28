
#from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
#app = FastAPI()
import csv
import os


from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# For this local classroom demo.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)


CSV_Folder_Path = os.path.dirname(os.path.abspath(__file__))


"""@app.get("/")
def home():
    return {"message": "Student API is running"}"""

"""
students = {
    1: {"name": "Anu", "course": "Python"},
    2: {"name": "Rahul", "course": "Java"},    
}

@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    return students[student_id]

@app.get("/students")
def get_students():
    return students
    
class Student(BaseModel):
    id: int
    name: str
    course: str

@app.post("/students")
def add_student(student: Student):
    #students.append(student.model_dump())
    students[student.id] = student.model_dump()
    return student


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    removed = students.pop(student_id)
    return {"deleted": removed}

@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    students[student_id] = student.model_dump()
    return student

"""
"""
Books = {
    1: {"Bookname": "Chumpak", "Author": "VSB"},
    2: {"Bookname": "Aayudh", "Author": "JVB"}
}

@app.get("/books/{book_id}")
def get_book(book_id: int):
    if book_id not in Books:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )


@app.get("/books")
def get_books():
    return Books

class Book(BaseModel):
    id: int
    Bookname: str
    Author: str

@app.post("/books")
def add_book(book: Book):
    Books[book.id] = book.model_dump()
    return book
  

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if book_id not in Books:
        raise HTTPException(status_code=404, detail="Book not found")
    removed = Books.pop(book_id)
    return {"deleted": removed}

@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    if book_id not in Books:
        raise HTTPException(status_code=404, detail="Book not found")
    Books[book_id] = book.model_dump()
    return book
"""


Libraries = {
    1: {"LibraryName": "Central", "Place": "Delhi"},
    2: {"LibraryName": "Asia", "Place": "Mumbai"}
}

def write_libraries_to_csv():
    filename = os.path.join(CSV_Folder_Path, "libraries.csv")

    try:
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "LibraryName", "Place"])   

            for lib_id, info in Libraries.items():
                writer.writerow([lib_id, info["LibraryName"], info["Place"]])                     
    except FileExistsError as e:
                    print(e)


write_libraries_to_csv()



@app.get("/libraries/{library_id}")
def get_library(library_id: int):
    if library_id not in Libraries:
        raise HTTPException(
            status_code=404,
            detail="Library not found"
        )


@app.get("/libraries")
def get_libraries():
    return Libraries

class Library(BaseModel):
    id: int
    LibraryName: str
    Place: str

@app.post("/libraries")
def add_library(library: Library):
    Libraries[library.id] = library.model_dump()
    print("******* I am here *******")
    return {"message":"Library added successfully","Library":library}

@app.delete("/libraries/{library_id}")
def delete_library(library_id: int):
    if library_id not in Libraries:
        raise HTTPException(status_code=404, detail="Library not found")
    removed = Libraries.pop(library_id)
    return {"deleted": removed}

@app.put("/libraries/{library_id}")
def update_library(library_id: int, library: Library):
    if library_id not in Libraries:
        raise HTTPException(status_code=404, detail="Library not found")
    Libraries[library_id] = library.model_dump()    
    return library
    


