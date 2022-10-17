from typing import Union
from unittest import result
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
import base64
import torch
from PIL import Image
import typing, json, io

model = torch.hub.load(repo_or_dir='ultralytics/yolov5', model='custom', path='./yolo_model.pt')

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

def get_image_from_bytes(binary_image, max_size=1024):
    input_image = Image.open(io.BytesIO(binary_image)).convert("RGB")
    width, height = input_image.size
    resize_factor = min(max_size / width, max_size / height)
    resized_image = input_image.resize(
        (
            int(input_image.width * resize_factor),
            int(input_image.height * resize_factor),
        )
    )
    return resized_image

app = FastAPI()


@app.get("/")
def root():
    return "This is the root URL of the API"

# receive a query as a base64 encoded string. return the decoded string
@app.get("/base64decoder/{query}")
def base64decoder(query: str):
    return {
        "message": base64.b64decode(query),
    }

# receive raw image data, get the result from the model, and return the result
@app.post("/image2json")
def image2json(file: UploadFile = File(...)):
    img = Image.open(file.file)
    results = model(img)
    detect_res = results.pandas().xyxy[0].to_json(orient="records")
    detect_res = json.loads(detect_res)
    return detect_res

# receive raw image data, get the result from the model, and return the renderred image
@app.post("/image2image")
def image2image(file: UploadFile = File(...)):
    img = Image.open(file.file)
    result = model(img)
    result.render()
    for img in result.ims:
        bytes_io = io.BytesIO()
        img_base64 = Image.fromarray(img)
        img_base64.save(bytes_io, format="png")
    return Response(content=bytes_io.getvalue(), media_type="image/png")

