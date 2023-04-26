import numpy as np
import pyautogui as gui
from pygame.time import Clock
from PIL import Image
from time import time, sleep
from itertools import count

WIDTH, HEIGHT = gui.size()


class Bot:
    url = 'https://wormax.io/'

    def __init__(self, fps=10, region=None):
        """Class constructor
        :param fps: frames per second (maximum number of screenshots bot
        can take in a second)
        :param region: area of the screen where bot takes the screenshots.
        Uses format [(x1, y1), (x2, y2)], contains only integers
        """
        self.clock = Clock()
        self.fps = fps
        self.resize = 2
        if not region:
            self.region = ((WIDTH // 4, HEIGHT // 4), (WIDTH // 4, HEIGHT // 4))
            self.region = [*self.region[0], *self.region[1]]
        else:
            self.region = region
        self.center = np.array([self.region[2] // 2, self.region[3] // 2])

    def get_data(self):
        """Returns an array of pixels which is basically a screenshot in black
        and white, squeezed in both directions.
        """
        return np.asarray(
            gui.screenshot(region=self.region).convert('1', dither=Image.NONE)
        )[::self.resize, ::self.resize]

    def to_absolute(self, coords):
        """Convert relative pixel coords to absolute"""
        return (coords[0] * self.resize + self.region[0], coords[1] * self.resize + self.region[1])

    def distance(self, coords):
        """Fast distance between two points on flat surface"""
        return np.linalg.norm(coords - self.center[::-1])

    def _basic_update(self):
        """The part of the bot with all the high-level logic"""
        self.clock.tick(self.fps)
        data = self.get_data()
        white_pixels = np.argwhere(data)
        if not len(white_pixels):
            return 1
        closest = min(white_pixels, key=self.distance)[::-1]
        # Another way to choose pixel out of all white ones
        # white_pixel = white_pixels[0][::-1]
        # gui.moveTo(self.to_absolute(white_pixel))
        gui.moveTo(self.to_absolute(closest))

    def _logged_update(self):
        """Modified update with time logging"""
        start_time = time()
        # None means found pixels and moved mouse
        # 1 means no pixels have been found, skiped mouse movement
        result = self._basic_update()
        end_time = time()
        if result:
            print("No pixels were found. ", end='')
        print(self.iteration, ': ', end_time - start_time, sep='')

    def _basic_run(self):
        """Infinite loop of bot updating"""
        for self.iteration in count():
            self.update()

    def _failsafe_run(self):
        """Runs the bot in mode when moving moude to the corner wouldn't cause
        an exception, but will finish the program correctly.
        """
        try:
            self._basic_run()
        except gui.FailSafeException:
            print("The bot has successfully finished")

    def run(self, wall=True, log=False):
        """Runs the bot with given configuration
        :param wall: if true, exxception will not be thrown when mouse reaches the corner of the screen
        :param log: if true, every iteration will be printed with the time it took. Useful for debugging
        :return: None
        """
        print("The bot has started")
        if log:
            self.update = self._logged_update
        else:
            self.update = self._basic_update
        if wall:
            self._failsafe_run()
        else:
            self._basic_run()


__all__ = ['Bot', 'WIDTH', 'HEIGHT']

if __name__ == '__main__':
    # import webbrowser
    bot = Bot()
    # webbrowser.open(bot.url)
    # sleep(3)
    # gui.hotkey('fn', 'f11')
    # click = list(bot.to_absolute(bot.center))
    # click[1] -= 35
    # gui.moveTo(click)
    # sleep(1)
    # gui.click()
    # sleep(2)
    bot.run(log=True)

