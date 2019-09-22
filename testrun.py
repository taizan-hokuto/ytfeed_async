import ytfeed, ytfeed_flat
from channel import Channel
if __name__ == '__main__':
    channel_list = ["UCJhjE7wbdYAae1G25m0tHAA",#Cafe Music BGM channel 
                    "UCQINXHZqCU5i06HzxRkujfg",#BGM channel
                    "UCiVAGG1Ull73fR_xp0909rA",#Green Music BGM channel
                    ]

    channels = ytfeed.get_videos(channel_list)

    for channel in channels:
        print(channel.id)
        print(channel.title)
        print(channel.videos)

    print()
    
    videos = ytfeed_flat.get_videos(channel_list)
    print(videos)

