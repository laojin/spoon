from spoon_server.proxy.provider import Provider
from spoon_server.util.html_parser import get_html_tree


class NianProvider(Provider):
    def __init__(self, url_list=None):
        super(Provider, self).__init__()
        if not url_list:
            self.url_list = self._gen_url_list()

    @staticmethod
    def _gen_url_list():
        url_list = ['http://www.nianshao.me/?stype=1&page={0}'.format(i) for i in range(1, 4)]
        url_list.extend(['http://www.nianshao.me/?stype=2&page={0}'.format(i) for i in range(1, 4)])
        return url_list

    @Provider.provider_exception
    def getter(self):
        for url in self.url_list:
            tree = get_html_tree(url)
            if tree is None:
                continue
            proxy_list = tree.xpath('//*[@id="main"]/div/div/table//tr')
            for px in proxy_list[1:]:
                yield ':'.join(px.xpath('./td/text()')[0:2])


if __name__ == "__main__":
    kd = NianProvider()
    for proxy in kd.getter():
        print(proxy)
