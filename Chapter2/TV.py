class TV():
    def __init__(self):
        self.isOn = False
        self.isMuted = False
        self.channelList = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
        self.channelIndex = 0
        self.VOLUME_MINIUM = 0
        self.VOLUME_MAXIMUM = 10
        self.volume = self.VOLUME_MAXIMUM//2 #integer division

    def power(self):
        self.isOn = not self.isOn

    def volumeUp(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume += 1

    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False
        if self.volume > self.VOLUME_MINIUM:
            self.volume -= 1
    def channelUp(self):
        if not self.isOn:
            return
        self.channelIndex = (self.channelIndex + 1) % len(self.channelList)

    def channelDown(self):
        if not self.isOn:
            return
        self.channelIndex = (self.channelIndex -1) % len(self.channelList)

    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted

    def setChannel(self, newChannel):
        if newChannel in self.channelList:
            self.channelIndex = self.channelList.index(newChannel)

    def showInfo(self):
        print()
        print('TV Status:')
        if self.isOn:
            print('\tTv is: On')
            print('\tChannel is: ', self.channelList[self.channelIndex])
            if self.isMuted:
                print('\tVolume is: ', self.volume,' (sound is muted)')
            else:
                print('\tVolume is: ', self.volume)
        else:
            print('\tTV is: Off')
