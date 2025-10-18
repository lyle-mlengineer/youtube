from pydantic import BaseModel, Field
from typing import Optional


class CaptionMetadataSnippet(BaseModel):
    videoId: Optional[str] = Field(default="")
    lastUpdated: Optional[str] = Field(default="")
    trackKind: Optional[str] = Field(default="")
    language: Optional[str] = Field(default="")
    name: Optional[str] = Field(default="")
    audioTrackType: Optional[str] = Field(default="")
    isCC: Optional[bool] = Field(default=False)
    isLarge: Optional[bool] = Field(default=False)
    isEasyReader: Optional[bool] = Field(default=False)
    isDraft: Optional[bool] = Field(default=False)
    isAutoSynced: Optional[bool] = Field(default=False)
    status: Optional[str] = Field(default="")


class CaptionMetadata(BaseModel):
    kind: Optional[str] = Field(default=None)
    etag: Optional[str] = Field(default=None)
    id: Optional[str] = Field(default=None)
    snippet: Optional[CaptionMetadataSnippet] = Field(default=None)