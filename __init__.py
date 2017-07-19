from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

from mycroft.util import play_wav

__author__ = 'b1'

LOGGER = getLogger(__name__)

class PlayWavSkill(MycroftSkill):
    def __init__(self):
		super(PlayWavSkill, self).__init__(name="PlayWavSkill")
		self.play_process = None
		self.file_path = self.config.get('test.wav')
				
    def initialize(self):
		play_wav_intent = IntentBuilder("PlayWavIntent").\
			require("PlayWavKeyword").build()
		self.register_intent(play_wav_intent, self.handle_play_wav_intent)

    def handle_play_wav_intent(self, message):
		self.play_process = play_wav(self.file_path)
    
    def stop(self):
		pass

def create_skill():
    return PlayWavSkill()