from PIL import Image
im = Image.open('westbrook.jpg')
pix = im.load()
width = im.size[0]
height = im.size[1]
for x in range(width):
    for y in range(height):
        r,g,b = pix[x, y]
        pix[x,y] = int(r/2), int(g/2), int(b/2)
im.save('H:/Q2.jpg')

