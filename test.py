import subprocess
import os
from unittest import TestCase


from server import Server


class ServerUnitTest(TestCase):

    def setUp(self):
        self.server = Server()

    def test_room_description(self):

        descriptions = [self.server.room_description(i) for i in range(4)]

        self.assertCountEqual(descriptions, set(descriptions))

    def test_say(self):

        for phrase in ["OK!", "Whazzzzzup?", "African or European?"]:
            self.server.say(phrase)
            self.assertEqual("OK! " + phrase, self.server.output_buffer)

