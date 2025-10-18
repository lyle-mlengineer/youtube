from datetime import datetime
from enum import Enum, auto
from typing import Optional

from pydantic import BaseModel, Field

from .request_filter import Filter
from .request_optional_parameters import OptionalParameters
from .request_part import Part


class CaptionPart(Part):
    part: list[str] = Field(
        default=[
            "id",
            "snippet",
        ]
    )


class CaptionFilter(Filter):
    videoId: Optional[str] = ""


class CaptionOptionalParameters(OptionalParameters):
    id: Optional[str] = ""
    onBehalfOfContentOwner: Optional[str] = ""
