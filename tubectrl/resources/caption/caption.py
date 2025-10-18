from typing import Any

from ...models import Caption
from ...schemas import CaptionFilter, CaptionOptionalParameters, CaptionPart, YouTubeRequest
from ..utils import create_request_dict
# from .parsers import parse_video, parse_video_list 
from tubectrl.resources.caption.parsers import CaptionMetadataListParser


class YouTubeCaptionResource:
    def __init__(self, youtube_client: Any):
        self.youtube_client = youtube_client

    def list_captions(self, video_id: str) -> list[Caption]:
        """List captions for a given video id."""
        request_filter: CaptionFilter = CaptionFilter(videoId=video_id)
        request_part: CaptionPart = CaptionPart()
        request_optional_params: CaptionOptionalParameters = CaptionOptionalParameters()
        youtube_request: YouTubeRequest = YouTubeRequest(
            part=request_part,
            filter=request_filter,
            optional_parameters=request_optional_params,
        )
        request_dict = create_request_dict(youtube_request)
        list_captions_request: dict = self.youtube_client.captions().list(**request_dict)
        list_captions_result: dict[str, Any] = list_captions_request.execute()
        captions_metadata_list_response = CaptionMetadataListParser.parse_caption_metadata_list_response(
            list_captions_result
        )
        return captions_metadata_list_response

    def download_caption(self, caption_id: str, tfmt: str = 'srt') -> str:
        """Download caption by caption id."""
        download_caption_request = self.youtube_client.captions().download(
            id=caption_id,
            tfmt=tfmt
        )
        caption_content: str = download_caption_request.execute()
        return caption_content