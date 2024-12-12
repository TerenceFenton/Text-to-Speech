# Libraries
import elevenlabs
from elevenlabs.client import ElevenLabs
import os
talking_stick = os.getenv('TALKINGSTICK')

client = ElevenLabs(api_key=talking_stick)