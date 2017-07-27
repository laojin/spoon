from spoon_server.proxy.fetcher import Fetcher
from spoon_server.main.proxy_pipe import ProxyPipe
from spoon_server.proxy.us_provider import UsProvider
from spoon_server.database.redis_config import RedisConfig


def main_run():
    redis = RedisConfig("127.0.0.1", 21009)
    p1 = ProxyPipe(url_prefix="https://www.google.com",
                   fetcher=Fetcher(use_default=False), database=redis).set_fetcher([UsProvider()])
    p1.start()


if __name__ == '__main__':
    main_run()
