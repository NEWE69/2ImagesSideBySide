from PIL import Image

#Open images to fusion
imgL = Image.open("/location/to/your/leftimg.png")
imgR = Image.open("/location/to/your/rightimg.png")

#Get images size 
wL, hL = imgL.size
wR, hR = imgR.size

#Convert into RGBA
imgL = imgL.convert("RGBA")
imgR = imgR.convert("RGBA")

#Compare sizes and resize if necessary
if hL != hR:
    if hL > hR:
        imgR = imgR.resize((wL, hL), Image.Resampling.LANCZOS)
        wR, hR = imgR.size
        maxH = hL
    else:
        imgL = imgL.resize((wR, hR), Image.Resampling.LANCZOS)
        wL, hL = imgL.size
        maxH = hR
else:
    maxH = hL


#Create a new image 
newImg = Image.new('RGBA', (wL+wR,maxH), color ='white')

#Assembler les images 
newImg.paste(imgL, (0,0))
newImg.paste(imgR, (wL,0))

newImg.save('NewImg.png')
     
