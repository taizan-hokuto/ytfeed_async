import aiohttp
import asyncio
import async_timeout
import xml.parsers.expat
import xmltodict

#通信エラー等でフィードが取得できない場合の最大リトライ回数
MAX_RETRY = 5

def get_videos(channel_list):
    loop = asyncio.get_event_loop()
    ret=[]
    result = loop.run_until_complete(_getvids(channel_list))
    [ret.extend(vid) for vid in result]
    return ret

async def _getvids(channel_list):
    async with aiohttp.ClientSession() as session:
        futures = [_fetch(session, channel_id) for channel_id in channel_list]
        return await asyncio.gather(*futures)
        
  
async def _fetch(session, channel_id):
    url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    result = []
    retry_count = 0
    for retry_count in range(MAX_RETRY):
        try:
            async with session.get(url) as resp:
                text = await resp.text()
                try:
                    doc = xmltodict.parse(text)
                    for m in doc['feed']['entry']:
                        result.append(m.get('yt:videoId'))
                except KeyError:
                    #チャンネル内動画がゼロ
                    pass
                except AttributeError:
                    #チャンネル内動画が一つだけ（feedの構造が変わっている）
                    m = doc['feed']['entry']
                    result.append(m.get('yt:videoId'))
                except xml.parsers.expat.ExpatError:
                    #チャンネルURLが削除されている
                    print(f'チャンネルが見つかりません:{channel_id}')
            return result
        except (aiohttp.client_exceptions.ClientConnectorError,
            aiohttp.client_exceptions.ServerDisconnectedError) as e:
            print(f'[{channel_id}]通信エラー：リトライ {retry_count+1}回目/{MAX_RETRY}回中')
            await asyncio.sleep(3)  

