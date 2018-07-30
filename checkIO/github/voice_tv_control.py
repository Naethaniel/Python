class VoiceCommand(object):
    def __init__(self, channels):
        self.index = 0
        self.channels = channels

    def first_channel(self):
        self.index = 0
        return self.channels[self.index]

    def last_channel(self):
        self.index = len(self.channels) - 1
        return self.channels[self.index]

    def turn_channel(self, n):
        self.index = n - 1
        return self.channels[self.index]

    def next_channel(self):
        self.index = (self.index + 1) % len(self.channels)
        return self.channels[self.index]

    def previous_channel(self):
        self.index = (self.index - 1) % len(self.channels)
        return self.channels[self.index]

    def current_channel(self):
        return self.channels[self.index]

    def is_exist(self, ch):
        flag = 0 <= ch - 1 < len(self.channels) if isinstance(ch, int) else ch in self.channels
        return 'Yes' if flag else 'No'


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    CHANNELS = ["BBC", "Discovery", "TV1000"]

    controller = VoiceCommand(CHANNELS)

    assert controller.first_channel() == "BBC"
    assert controller.last_channel() == "TV1000"
    assert controller.turn_channel(1) == "BBC"
    assert controller.next_channel() == "Discovery"
    assert controller.previous_channel() == "BBC"
    assert controller.current_channel() == "BBC"
    assert controller.is_exist(4) == "No"
    assert controller.is_exist("TV1000") == "Yes"
    print("Coding complete? Let's try tests!")
