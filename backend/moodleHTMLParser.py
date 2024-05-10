from html.parser import HTMLParser


class MoodleHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.token = ''

    def handle_starttag(self, tag, attrs):
        if tag == 'input' and ('name', 'logintoken') in attrs:
            self.token = attrs[2][1]

    def get_logintoken(self):
        return self.token