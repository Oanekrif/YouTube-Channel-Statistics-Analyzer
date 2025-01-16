# YouTube Channel Statistics Analyzer
# Install required libraries
# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
# pip install pandas seaborn matplotlib pyyaml

from googleapiclient.discovery import build
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import sys
import yaml

# Load YouTube API token from a YAML file
parameters_file = open(os.path.join(sys.path[0], "youtube_api_token.yaml"), "r")
parameters_file_parsed = yaml.load(parameters_file, Loader=yaml.FullLoader)
TOKEN = parameters_file_parsed["parameters_dictionary"].get('TOKEN')

# List of channel IDs
# Exemple
#channel_ids = ['UCbbQt4SQp26xjc55bCs-uGA','UCSNkfKl4cU-55Nm-ovsvOHQ','UCbQh1yxBPVhyjB-G_blFFEQ','UCMPBiSwYY4fS1LYw4KkDZuw','UCAahySnMsXP77kGb0Gfcq-w']
channel_ids = ['']

# Initialize YouTube API client
youtube = build('youtube', 'v3', developerKey=TOKEN)

# Function to fetch channel details
def get_channel_stats(youtube, channel_ids):
    all_channels_data = []
    request = youtube.channels().list(
        part='snippet,contentDetails,statistics',
        id=','.join(channel_ids)
    )
    response = request.execute()
    for i in range(len(response['items'])):
        data = dict(channel_name = response['items'][i]['snippet']['title'],
                    Subscribers = response['items'][i]['statistics']['subscriberCount'],
                    Views = response['items'][i]['statistics']['viewCount'],
                    Total_videos = response['items'][i]['statistics']['videoCount']
                )
        all_channels_data.append(data)
    return all_channels_data
golden_data = get_channel_stats(youtube, channel_ids)
view_data = pd.DataFrame(golden_data)
# print the data on the terminal
print(view_data)

view_data['Subscribers'] = pd.to_numeric(view_data['Subscribers'])
view_data['Views'] = pd.to_numeric(view_data['Views'])
view_data['Total_videos'] = pd.to_numeric(view_data['Total_videos'])

ax = sns.barplot(x='channel_name', y='Subscribers', data=view_data)
# show the data as a plot for good view..
plt.show()