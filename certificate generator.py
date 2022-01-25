#import the modules
from PIL import Image,ImageDraw,ImageFont
import pandas as pd
import os
to_read=pd.read_csv("name_details.csv")#provide the names to be in certificate using csv format
font=ImageFont.truetype('arial.ttf',30)
for index,j in to_read.iterrows():
    img=Image.open("certificate_template.jpg")#provide the template of the certificate
    draw=ImageDraw.Draw(img)
    draw.text(xy=(305,330),text='{}'.format(j['name']),fill=(250,105,180),font=font)#provide the position to place the text in image
    img.save("certificates/{}.jpg".format(j["name"]))#provide the folder to save the generated certificates
