class Router:
    def __init__(self, driver, base_url):
        if not base_url:
            return
        self.driver = driver
        self.base_url = base_url
        if base_url[-1] == '/':
            self.base_url = self.base_url[:-1]

    # navigate using pathname
    def navigate(self, pathname):
        full_url = self.base_url + pathname
        self.driver.get(full_url)
