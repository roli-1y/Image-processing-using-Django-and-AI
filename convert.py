import cv2
import numpy as np
import sys
from PIL import Image
imageFull=sys.argv[1]
imgname=sys.argv[2]
img = cv2.imread(sys.argv[1])
#print(type(img))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
con = cv2.Canny(img, 100, 200)
#print(type(con))
im=Image.fromarray(con)
im=im.resize((203,250))
#203 250
imgsav=imageFull.replace(imgname,"rot.png")
im.save(imgsav)
print("/Media/rot.png")
