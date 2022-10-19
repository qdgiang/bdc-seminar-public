from typing import Union
from fastapi import FastAPI, UploadFile
from fastapi.responses import Response
from api_helper import PrettyJSONResponse, StudentInfo
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import uvicorn
import base64
import typing, json, io

app = FastAPI()


@app.get("/")
def root():
    return "This is the root URL of the API"

@app.get("/api/hello/")
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

class PrettyJSONResponse(Response):
    media_type = "application/json"

    def render(self, content: typing.Any) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=4,
            separators=(", ", ": "),
        ).encode("utf-8")

@app.get("/")
def root():
    return "This is the root URL of the API."

## receive a query as a base64 encoded string. return the decoded string
@app.get("/api/base64decoder/{query}")
def base64decoder(query: str):
    return {
        "message": base64.b64decode(query),
    }

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)