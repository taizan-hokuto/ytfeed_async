import ytfeed, ytfeed_flat
from channel import Channel
if __name__ == '__main__':
    channel_list = ["UCJhjE7wbdYAae1G25m0tHAA",#Cafe Music BGM channel 
                    "UCQINXHZqCU5i06HzxRkujfg",#BGM channel
                    "UCiVAGG1Ull73fR_xp0909rA",#Green Music BGM channel
                    ]
    channels = ytfeed.get_videos(channel_list)
    print('チャンネルデータ一覧')
    for channel in channels:
        print(f"---チャンネルID---\n{channel.id}")
        print(f"---チャンネル名---\n{channel.title}")
        print(f"---直近の動画IDリスト---{channel.videos}")
        print()
    print()
    print('フィード内動画ID一覧')
    videos = ytfeed_flat.get_videos(channel_list)
    print(videos)

