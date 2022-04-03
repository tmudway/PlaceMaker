from PIL import Image, ImageColor
import sys

palette = [
    109, 0, 26 ,
    190, 0, 57 ,
    16, 69, 0 ,
    255, 168, 0 ,
    255, 214, 53 ,
    255, 248, 184 ,
    0, 163, 104 ,
    0, 204, 120 ,
    126, 237, 86 ,
    0, 117, 111 ,
    0, 158, 170 ,
    0, 204, 192 ,
    36, 80, 164 ,
    54, 144, 234 ,
    81, 233, 244 ,
    73, 58, 193 ,
    106, 92, 255 ,
    148, 179, 255 ,
    129, 30, 159 ,
    180, 74, 192 ,
    228, 171, 255 ,
    222, 16, 127 ,
    255, 56, 129 ,
    255, 153, 170 ,
    109, 72, 47 ,
    156, 105, 38 ,
    255, 180, 112 ,
    0, 0, 0 ,
    81, 82, 82 ,
    137, 141, 144 ,
    212, 215, 217 ,
    255, 255, 255 ,
]

palette.extend((768-len(palette)) * [0])

img_dir = sys.argv[1]
sz = int(sys.argv[2]) if len(sys.argv) > 2 else 0

img = Image.open(img_dir)
w, h = img.size
print(img.size)
if sz != 0:
    if w > h:
        h = int(h / (w / sz))
        w = sz 
    else:
        w = int(w/(h/sz))
        h = sz
    
    img = img.resize((w,h), resample = Image.NONE)

pallette_image= Image.new("P", (1,1))
pallette_image.putpalette(palette)
img = img.convert("RGB").quantize(palette=pallette_image, dither=Image.NONE, method = Image.NEAREST)

#img = img.resize((w*10, h*10), resample = Image.NONE)
img.convert('RGBA')
img.save("output_" + img_dir)


