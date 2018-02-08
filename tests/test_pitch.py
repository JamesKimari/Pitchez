import unittest
from app.models import Pitch

class PitchModelTest(unittest.TestCase):

    def setUp(self):
        self.new_pitch = Pitch(id = 1, title = 'hilarious', pitch_content = 'I saw you in my dreams and i dint wanna wake up', category = 'Pickup Line', upvote = 1, downvote = 1, author = 'james')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))
