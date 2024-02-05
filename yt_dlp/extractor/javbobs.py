from .common import InfoExtractor


class JavbobsIE(InfoExtractor):
    _VALID_URL = r'https?://www.javbobs.com/(?P<id>.+)/'
    _TESTS = []

    def _real_extract(self, url):
        video_id = self._match_id(url)
        print("video_id", video_id)

        webpage = self._download_webpage(url, video_id)
        # TODO more code goes here, for example ...
        title = self._html_search_regex(r"""<div class="ttl-cn dfl fa-film">
<h2>(.*?)</h2>""", webpage, 'title')
        iframe_url = self._html_search_regex(
            r'<iframe frameborder="0" scrolling="no" src="(.*?)" width="100%" allowfullscreen></iframe>', webpage,
            'iframe_url')
        print(iframe_url)
        iframe_page = self._download_webpage_handle(iframe_url, video_id, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:122.0) Gecko/20100101 Firefox/122.0',
            'Referer': 'https://www.javbobs.com/'
        })[0]
        url = self._html_search_regex(r'source: "(.*?)",', iframe_page, 'url')

        return {
            'id': video_id,
            'title': title,
            # 'description': self._og_search_description(webpage),
            # 'uploader': self._search_regex(r'<div[^>]+id="uploader"[^>]*>([^<]+)<', webpage, 'uploader', fatal=False),
            'formats': [
                {
                    'url': url,
                    'ext': 'mp4',
                    'format_id': 'm3u8',
                    'protocol': 'm3u8',
                }
            ]

        }
