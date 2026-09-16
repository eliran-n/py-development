
# 1472. Design Browser History

class BrowserHistory(object):

    def __init__(self, homepage):

        self.browser_history = []
        self.url_metadata = {"current": "", "index": 0}

        self.browser_history.append(homepage)
        self.url_metadata["current"] = self.browser_history[0]

    def visit(self, url):
        if self.url_metadata["index"] == len(self.browser_history) - 1:
            self.browser_history.append(url)
        else:
            self.browser_history = self.browser_history[0:self.url_metadata["index"] + 1]
            self.browser_history.append(url)

        self.url_metadata["current"] = url
        self.url_metadata["index"] = self.url_metadata["index"] + 1

    def back(self, steps):
        if self.url_metadata["index"] - steps >= 0:
            current_index = self.url_metadata["index"]
            self.url_metadata["current"] = self.browser_history[current_index - steps]
            self.url_metadata["index"] = current_index - steps
        else:
            self.url_metadata["index"] = 0
            self.url_metadata["current"] = self.browser_history[0]

        return self.url_metadata["current"]

    def forward(self, steps):
        current_index = self.url_metadata["index"]
        if (current_index + steps) <= len(self.browser_history) - 1:
            self.url_metadata["current"] = self.browser_history[current_index + steps]
            self.url_metadata["index"] = current_index + steps
        else:
            self.url_metadata["index"] = len(self.browser_history) - 1
            self.url_metadata["current"] = self.browser_history[self.url_metadata["index"]]

        return self.url_metadata["current"]

    def print_current_browser_history(self):
        print(self.browser_history)
        print(f"current url: {self.url_metadata["current"]}, current index: {self.url_metadata["index"]}\n")


if __name__ == "__main__":
    browser_obj = BrowserHistory("google.com")
    browser_obj.visit("one.co.il")
    browser_obj.visit("leetcode")
    browser_obj.print_current_browser_history()
    browser_obj.back(1)
    browser_obj.print_current_browser_history()
    browser_obj.visit("facebook.com")
    browser_obj.visit("youtube.com")
    browser_obj.print_current_browser_history()
    browser_obj.back(2)
    browser_obj.print_current_browser_history()
    browser_obj.forward(2)
    browser_obj.print_current_browser_history()