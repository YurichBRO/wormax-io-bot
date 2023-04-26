## The principle
All this bot is taking screenshots of your screen and searching bright pixels.
If you run *wormax.io* you can see, that all the edible dots are bright enough
to be white in case the image is black and white. So, bot searches for white
pixels on the image. If it sees one or more, it takes the distance to all of
these pixels from the center, chooses the closest one and moves your mouse 
on it.

You would also see that many of player skins are bright and can cause
mistakes. And that's the problem we can not forget. To avoid it see *Usage*
## Efficiency
The process of taking screenshots multiple times a second is not very
efficient. To avoid wasting processor time you can limit the bot fps
(default is 10fps, actually the bot rarely needs more than this). If you are
wondering what does the world look like to this bot, you can add image saving,
you can also image logs for debugging (would decrease performance probably).

Processing the full image is too heavy, so the image is not taking the whole
screen by default.
## Usage
To use the program you will need an open wormax.io tab and code like this in
your script:
```python
"""An example of usage"""
from main import Bot

bot = Bot()
bot.run()
```
It's simple, intuitive, doesn't require any deep knowledge of the program.
However, the bot starts working immediately, that's why you need to open
the existing tab using your keyboard.

Before you start you must know that players sometimes can be identified as
food. For a better experience use the program in places with no players.
You also must choose a dark skin with no eyes and bright dots to be sure
you worm doesn't follow its own tail.

To finish the program quickly move your mouse to one of the corners of the
screen.

After all use can play with settings, see the in-file documentation for
details.
```python
from main import Bot, WIDTH, HEIGHT

# bot = Bot(region=[(0, 0), (WIDTH, HEIGHT)])
# bot = Bot(fps=15)
# bot.run(log=True)
# bot.run(wall=False)
```