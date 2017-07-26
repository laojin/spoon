import time
from multiprocessing import Process

from spoon_server.proxy.fetcher import Fetcher
from spoon_server.main.refresher import refresher_run
from spoon_server.main.validater import validater_run


class ProxyPipe(object):
    def __init__(self, database=None, fetcher=None, url_prefix=None):
        if not fetcher:
            self._fetcher = Fetcher()

        self._database = database
        self._url_prefix = url_prefix

    def set_fetcher(self, provider_list):
        self._fetcher.set_provider(provider_list)
        return self

    def start(self):
        proc1 = Process(target=validater_run, args=(self._url_prefix, self._fetcher, self._database, ))
        proc2 = Process(target=refresher_run, args=(self._url_prefix, self._fetcher, self._database, ))

        proc_list = [proc1, proc2]

        for proc in proc_list:
            proc.start()
            time.sleep(1)
        for proc in proc_list:
            proc.join()


if __name__ == "__main__":
    pp = ProxyPipe()
    pp.start()
