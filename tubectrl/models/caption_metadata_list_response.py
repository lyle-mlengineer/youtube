from pydantic import BaseModel, Field
from typing import Optional
from .caption_metadata import CaptionMetadata


class CaptionMetadataListResponse(BaseModel):
    kind: Optional[str] = Field(default=None)
    etag: Optional[str] = Field(default=None)
    id: Optional[str] = Field(default=None)
    items: Optional[list[CaptionMetadata]] = Field(default=[])