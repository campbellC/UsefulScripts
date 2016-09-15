import soundfile
import sounddevice
class Alarm:
    def playAlarm(self):
        data, fs = soundfile.read("/System/Library/Sounds/Glass.aiff")
        sounddevice.play(data, fs, blocking=True)
