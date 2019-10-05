class Channel:
    """
    チャンネルを表すクラス

    Attributes
    ----------
    id : str
        チャンネルのID
    title : str
        チャンネル名
    videos : list<str>
        フィードから取得できる動画IDのリスト
    """
    def __init__(self, id :str='',title :str='', videos :list =[]):
        self.id = id
        self.title = title
        self.videos = videos

