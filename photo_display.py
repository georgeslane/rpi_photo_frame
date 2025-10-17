import os
import time
from PIL import Image
from st7789 import ST7789
class Display:
    """Controls the display of photos on the screen.
    """
    def __init__(self):
        self.display = ST7789(
            port=0,
            cs=1,
            dc=9,
            backlight=13,
            spi_speed_hz=80 * 1000 * 1000,
            width=320,
            height=240,
            rotation=0,
            invert=True
        )

    def get_photos(self, path:str):
        files = []
        for filename in os.listdir(path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                files.append(filename)

        return files
    
    def display_slideshow(self, images:list, path:str):
        """Displays all images specified in a rotating slideshow.
        """
        self.display.set_backlight(1.0)
        try:
            while True:
                for index, image in enumerate(images):
                    try:
                        image = Image.open(f'{path}{image}')
                    except FileNotFoundError:
                        image = Image.open(f'{path}{images[index - 1]}')

                    image = image.resize((self.display.width, self.display.height))
                    self.display.display(image)
                    time.sleep(1)
        
        except KeyboardInterrupt:
            self.display.set_backlight(0.0)












