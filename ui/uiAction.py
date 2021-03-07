from PIL import ImageFont
from ui.DisplayImage import DisplayImage
import LCD_1in44
import LCD_Config

font = ImageFont.truetype("Seven Segment.ttf", 60)

disp = LCD_1in44.LCD()
Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
disp.LCD_Init(Lcd_ScanDir)
disp.LCD_Clear()

img = DisplayImage()
img.drawBar(15, 1.0, 'yellow')
img.drawBarMark(15, 0.6, 'red')
img.drawBar(35, 0.4, 'white')
img.drawState(5, 50, 'pause')
img.writeSpeed(36, 60, '55')

disp.LCD_ShowImage(img.getImage(),0,0)

