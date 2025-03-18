from tubectrl import YouTube
from pathlib import Path
import json
from gverify import InvalidSecretsFileException


# def save_resource(resource: dict, resource_name: str) -> None:
#     resource_name = f'{resource_name}.json'
#     with open(resource_name, 'w') as f:
#         json.dump(resource, fp=f, indent=4)


# client_secret_file: str = '/home/lyle/Downloads/youtube_secrets.json'
# youtube = YouTube()
# youtube.authenticate(client_secret_file)
# video_id: str = 'l93N4XaQJok'
# response = youtube.find_video_by_id(video_id=video_id)
# # response = youtube.find_videos_by_ids(video_ids=[video_id, video_id])
# print(response)
# # save_resource(response, video_id)