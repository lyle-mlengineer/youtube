from ...models import CaptionMetadata, CaptionMetadataListResponse, CaptionMetadataSnippet
from typing import Any


def parse_caption_metadata_snippet(snippet_data: dict[str, Any]) -> CaptionMetadataSnippet:
    snippet: CaptionMetadataSnippet = CaptionMetadataSnippet()
    if snippet_data.get("videoId"):
        snippet.videoId = snippet_data["videoId"]
    if snippet_data.get("lastUpdated"):
        snippet.lastUpdated = snippet_data["lastUpdated"]
    if snippet_data.get("trackKind"):
        snippet.trackKind = snippet_data["trackKind"]
    if snippet_data.get("language"):
        snippet.language = snippet_data["language"]
    if snippet_data.get("name"):
        snippet.name = snippet_data["name"]
    if snippet_data.get("audioTrackType"):
        snippet.audioTrackType = snippet_data["audioTrackType"]
    if snippet_data.get("isCC") is not None:
        snippet.isCC = snippet_data["isCC"]
    if snippet_data.get("isLarge") is not None:
        snippet.isLarge = snippet_data["isLarge"]
    if snippet_data.get("isEasyReader") is not None:
        snippet.isEasyReader = snippet_data["isEasyReader"]
    if snippet_data.get("isDraft") is not None:
        snippet.isDraft = snippet_data["isDraft"]
    if snippet_data.get("isAutoSynced") is not None:
        snippet.isAutoSynced = snippet_data["isAutoSynced"]
    if snippet_data.get("status"):
        snippet.status = snippet_data["status"]
    return snippet


class CaptionMetadataListParser:
    @staticmethod
    def parse_caption_metadata(caption_data: dict[str, Any]) -> CaptionMetadata:
        caption_metadata: CaptionMetadata = CaptionMetadata()
        if caption_data.get("kind"):
            caption_metadata.kind = caption_data["kind"]
        if caption_data.get("etag"):
            caption_metadata.etag = caption_data["etag"]
        if caption_data.get("id"):
            caption_metadata.id = caption_data["id"]
        if caption_data.get("snippet"):
            caption_metadata.snippet = parse_caption_metadata_snippet(caption_data["snippet"])
        return caption_metadata

    @staticmethod
    def parse_caption_metadata_list_response(
        response_data: dict[str, Any],
    ) -> CaptionMetadataListResponse:
        response: CaptionMetadataListResponse = CaptionMetadataListResponse()
        if response_data.get("kind"):
            response.kind = response_data["kind"]
        if response_data.get("etag"):
            response.etag = response_data["etag"]
        if response_data.get("id"):
            response.id = response_data["id"]
        if response_data.get("items"):
            response.items = [
                CaptionMetadataListParser.parse_caption_metadata(item)
                for item in response_data["items"]
            ]
        return response