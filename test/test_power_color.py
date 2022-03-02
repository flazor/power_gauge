import unittest
from power_color import color, fade, rgb_fader, color_fader, ORANGE, RED 

class TestPowerColor(unittest.TestCase):

    def test_blue_color(self):
        self.assertEqual(color(0), '#0000ff')
        self.assertEqual(color(89), '#0000ff')

    def test_green_color(self):
        self.assertEqual(color(100), '#00ff00')
        self.assertEqual(color(149), '#00ff00')

    def test_yellow_color(self):
        self.assertEqual(color(200), '#ffff00')
        self.assertEqual(color(299), '#ffff00')

    def test_orange_color(self):
        self.assertEqual(color(500), '#ff7f00')
        self.assertEqual(color(699), '#ff7f00')

    def test_red_color(self):
        self.assertEqual(color(1000), '#ff0000')
        self.assertEqual(color(99099), '#ff0000')

    def test_fade(self):
        self.assertEqual(fade(0), 0)
        self.assertEqual(fade(1), 255)
        self.assertEqual(fade(0.25), 63.75)
        self.assertEqual(fade(0.5), 127.5)
        self.assertEqual(fade(0.75), 191.25)
        
    def test_fade_end(self):
        self.assertEqual(fade(0.5, color_end=127), 63.5)
    
    def test_fade_start(self):
        self.assertEqual(fade(0.5, color_start=128), 191.5)
    
    def test_fade_descending(self):
        self.assertEqual(fade(0.25, color_start=255, color_end=0), 191.25)
        self.assertEqual(fade(0.5, color_start=255, color_end=0), 127.5)
        self.assertEqual(fade(0.75, color_start=255, color_end=0), 63.75)
        # range less than 255
        self.assertEqual(fade(0.25, color_start=255, color_end=128), 223.25)
        self.assertEqual(fade(0.25, color_start=127, color_end=0), 95.25)

    def test_rgb_fader(self):
        self.assertEqual(rgb_fader(1, 0, 1), '#ffffff')
        self.assertEqual(rgb_fader(0, 0, 1), '#000000')
        self.assertEqual(rgb_fader(95, 90, 100), '#7f7f7f')
        self.assertEqual(rgb_fader(50, 0, 100), '#7f7f7f')

    def test_rgb_fader_blue_to_green(self):
        self.assertEqual(rgb_fader(0, 0, 1, r_max=0, b_min=255, b_max=0), '#0000ff')
        self.assertEqual(rgb_fader(1, 0, 1, r_max=0, b_min=255, b_max=0), '#00ff00')
        self.assertEqual(rgb_fader(0.5, 0, 1, r_max=0, b_min=255, b_max=0), '#007f7f')

    def test_rgb_fader_orange_to_red(self):
        self.assertEqual(rgb_fader(0, 0, 1, r_min=255, g_min=127, g_max=0, b_max=0), '#ff7f00')
        self.assertEqual(rgb_fader(1, 0, 1, r_min=255, g_min=127, g_max=0, b_max=0), '#ff0000')
        self.assertEqual(rgb_fader(0.5, 0, 1, r_min=255, g_min=127, g_max=0, b_max=0), '#ff3f00')

    def test_color_fader_blue_to_green(self):
        self.assertEqual(color_fader(0, 0, 1, '#0000ff', '#00ff00'), '#0000ff')
        self.assertEqual(color_fader(1, 0, 1, '#0000ff', '#00ff00'), '#00ff00')
        self.assertEqual(color_fader(0.5, 0, 1, '#0000ff', '#00ff00'), '#007f7f')

    def test_color_fader_orange_to_red(self):
        self.assertEqual(color_fader(0, 0, 1, ORANGE, RED), '#ff7f00')
        self.assertEqual(color_fader(1, 0, 1, ORANGE, RED), '#ff0000')
        self.assertEqual(color_fader(0.5, 0, 1, ORANGE, RED), '#ff3f00')



if __name__ == '__main__':
    unittest.main()
