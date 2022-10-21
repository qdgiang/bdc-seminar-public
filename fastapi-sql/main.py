from fastapi import FastAPI
from api_helper import PrettyJSONResponse, StudentInfo
from fastapi import FastAPI

import uvicorn

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float

db_url = "mysql+pymysql://root:randompass123A!@localhost:3306/seminar"
app = FastAPI()
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()

@app.get("/")
def root():
    return "This is the root URL of the API"

@app.get("/hello")
def hello_world():
    return {"message": "Hello world!"}


@app.get("/square/{number}", response_class=PrettyJSONResponse)
def square_1(number: int):
    return {
        "number": number,
        "result": number ** 2
    }

@app.get("/square")
def square_2(number: int):
    return {
        "number": number,
        "result": number ** 2
    }


Base = declarative_base()
class Student(Base):
    __tablename__ = 'student'
    student_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    major = Column(String(50))
    additional_info = Column(String(50))

@app.post("/student")
def create_student(student: StudentInfo):
    # send data to database
    new_student = Student(student_id= student.student_id ,name=student.name, major=student.major, additional_info=student.additional_info)
    session.add(new_student)
    session.commit()


    return {
        "message": "Student created successfully",
        "name": student.name,
    }

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)