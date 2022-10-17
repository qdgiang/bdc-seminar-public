from typing import Union
import json, typing
from fastapi.responses import Response
from pydantic import BaseModel

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

class StudentInfo(BaseModel):
    name: str
    student_id: int
    major: str
    additional_info: Union[str, None] = None
