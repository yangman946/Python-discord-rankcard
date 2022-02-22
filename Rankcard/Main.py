# Discord rank card by clarence yang 30/12/21

import requests
import os
from PIL import Image, ImageFont, ImageOps, ImageDraw
from io import BytesIO

class RANKCARD():
    def rank_card(self, username, avatar, level, rank, current_xp, custom_background, xp_color, next_level_xp):

        # create backdrop
        img = Image.new('RGB', (934, 282), color = custom_background) 
        response = requests.get(avatar) # get avatar picture
        img_avatar = Image.open(BytesIO(response.content)).convert("RGBA")


        # create circle mask
        bigsize = (img_avatar.size[0] * 3, img_avatar.size[1] * 3)
        mask = Image.new('L', bigsize, 0)
        draw = ImageDraw.Draw(mask) 
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(img_avatar.size)
        img_avatar.putalpha(mask)


        img_avatar = img_avatar.resize((170, 170))
        

        img.paste(img_avatar, (50, 50))
        d = ImageDraw.Draw(img)
        d = self.drawProgressBar(d, 260, 180, 575, 40, current_xp/next_level_xp, bg="#484B4E", fg = xp_color) # create progress bar
        print(str(os.getcwd()))


        


        font = ImageFont.truetype(font=f"Rankcard/fonts/regular.ttf", size=50)
        font2 = ImageFont.truetype(font=f"Rankcard/fonts/regular.ttf", size=25)

        # add text
        d.text((260, 100),username,(255,255,255), font=font)
        d.text((740, 130),f"{current_xp}/{next_level_xp} XP",(255,255,255), font=font2)
        d.text((650, 50),f"LEVEL {level}",xp_color, font=font)
        d.text((260, 50),f"RANK #{rank}",(255,255,255), font=font2)


        # save image
        img.save(f"{os.getcwd()}\\Rankcard\\pics\\out.jpg")
        return f"{os.getcwd()}\\Rankcard\\pics\\out.jpg"
    
    def drawProgressBar(self, d, x, y, w, h, progress, bg="black", fg="red"):
        # draw background
        d.ellipse((x+w, y, x+h+w, y+h), fill=bg)
        d.ellipse((x, y, x+h, y+h), fill=bg)
        d.rectangle((x+(h/2), y, x+w+(h/2), y+h), fill=bg)

        # draw progress bar
        w *= progress
        d.ellipse((x+w, y, x+h+w, y+h),fill=fg)
        d.ellipse((x, y, x+h, y+h),fill=fg)
        d.rectangle((x+(h/2), y, x+w+(h/2), y+h),fill=fg)

        return d


