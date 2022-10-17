from fastapi import FastAPI
from api_helper import PrettyJSONResponse, StudentInfo
from fastapi import FastAPI
import uvicorn

app = FastAPI()

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

@app.post("/student")
def create_student(student: StudentInfo):
    return {
        "message": "Student created successfully",
        "name": student.name,
    }

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)