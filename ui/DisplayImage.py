from PIL import Image, ImageDraw, ImageFont


class DisplayImage:
    def __init__(self, font):
        self.image = Image.new('RGB', (128, 128), color='black')
        self.draw = ImageDraw.Draw(self.image)
        self.font = font


    def drawBar(self, y, percentage, color):
        self.draw.rectangle((3, y, 120 * percentage + 3, y+3), outline=color, fill=color)

    def drawBarMark(self, y, percentage, color):
        x = 120 * percentage + 3
        self.draw.line((x, y-4, x, y+7), fill=color, width=3)

    def drawState(self, x, y, state):
        if state == 'recording':
            self.draw.ellipse((x, y, x+15, y+15), outline='red', fill='red')
        else:
            self.draw.rectangle((x, y, x+5, y+15), outline='lightgrey', fill='lightgrey')
            self.draw.rectangle((x+10, y, x + 15, y + 15), outline='lightgrey', fill='lightgrey')

    def writeSpeed(self, x, y, speed):
        self.draw.text((x, y), speed, fill='white', font=self.font)

    def debugShow(self):
        self.image.show()

    def getImage(self):
        return self.image
