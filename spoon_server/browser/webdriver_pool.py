from queue import Queue, Empty
from selenium import webdriver


class WebdriverPool(object):
    def __init__(self, phantomjs_path):
        self.phantomjs_path = phantomjs_path
        self.all = Queue()
        self.available = Queue()
        self.stopped = False

    def acquire(self):
        if not self.stopped:
            try:
                return self.available.get_nowait()
            except Empty:
                driver = webdriver.PhantomJS(self.phantomjs_path)
                self.all.put(driver)
                return driver

    def release(self, driver):
        self.available.put(driver)

    def stop(self):
        self.stopped = True
        while True:
            try:
                driver = self.all.get(block=False)
                driver.quit()
            except Empty:
                break


if __name__ == "__main__":
    wd = WebdriverPool("D:/program/phantomjs-2.1.1-windows/bin/phantomjs.exe")
    driver = wd.acquire()
    driver.get("www.baidu.com")
    wd.release(driver)
    wd.stop()
    print(wd.acquire() is None)
