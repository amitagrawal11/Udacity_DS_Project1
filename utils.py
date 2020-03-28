class Text:
    def __init__(self, text):
        incoming, answering, time = text
        self.incoming = incoming
        self.answering = answering
        self.time = time


class Call:
    def __init__(self, call):
        incoming, answering, time, during = call
        self.incoming = incoming
        self.answering = answering
        self.time = time
        self.during = during
