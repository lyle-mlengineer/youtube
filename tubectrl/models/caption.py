from pydantic import BaseModel, Field
from typing import Optional


class Caption(BaseModel):
    kind: Optional[str] = Field(default=None)
    etag: Optional[str] = Field(default=None)
    id: Optional[str] = Field(default=None)