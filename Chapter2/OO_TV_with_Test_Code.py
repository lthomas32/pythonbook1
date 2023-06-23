#Testing file
from TV import TV
#New tv object
oTV = TV()

#Turn the tv on and show the status
oTV.power()
oTV.showInfo()

oTV.channelUp()
oTV.channelUp()
oTV.volumeUp()
oTV.volumeUp()
oTV.showInfo()

oTV.power()
oTV.showInfo()
oTV.power()
oTV.showInfo()

oTV.volumeDown()
oTV.mute()
oTV.showInfo()

oTV.setChannel(11)
oTV.mute()
oTV.showInfo()





