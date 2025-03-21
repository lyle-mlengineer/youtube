from tubectrl import YouTube
from pathlib import Path
import json
from gverify import InvalidSecretsFileException
from typing import Any, Iterator, Optional


def save_resource(resource: dict, resource_name: str) -> None:
    resource_name = f'{resource_name}.json'
    with open(resource_name, 'w') as f:
        json.dump(resource, fp=f, indent=4)


def load_resource(resource_path: str) -> dict:
    with open(resource_path, 'r') as f:
        return json.load(f)


# client_secret_file: str = '/home/lyle/Downloads/youtube_secrets.json'
# youtube = YouTube()
# youtube.authenticate(client_secret_file)
credentials_path: str = '/home/lyle/.youtube/credentials.json'
youtube = YouTube()
youtube.authenticate_from_credentials(credentials_path)
video_id: str = 'l93N4XaQJok'
# response = youtube.find_video_by_id(video_id=video_id)
# response = youtube.find_videos_by_ids(video_ids=[video_id, video_id])
# print(response)
# save_resource(response, video_id)
# iterator: Iterator = youtube.get_channel_playlists_iterator(
#     channel_id="UCt6Lag-vv25fTX3e11mVY1Q"
# )
# count = 0
# for playlist in iterator:
#     save_resource(playlist, f"playlists-{count}.json")
#     print(playlist)
#     count += 1
# iterator: Iterator = youtube.get_channel_playlists_iterator(
#     channel_id="UCkfx67Y3VeQwsCpKaguGs3g"
# )
# for playlist in iterator:
#     print(playlist)

iterator: Iterator = youtube.get_playlist_items_iterator(
    playlist_id="PLK0b4e05LnzZh7g9-60nS0H_FxPlib7PV"
)
count = 0
for videos in iterator:
    # save_resource(videos, f"videos-{count}.json")
    print(videos)
    count += 1
# results = load_resource('videos-0.json.json')
# from tubectrl.resources.playlist_item.parsers import parse_playlist_items_list
# results = parse_playlist_items_list(results['items'])
# print(results)