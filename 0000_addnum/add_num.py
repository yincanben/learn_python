from PIL import Image, ImageDraw, ImageFont
def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('/Library/Fonts/Arial.ttf', size=100)
    fillcolor = "#ff0000"
    width, height = img.size
    print width,height
    draw.text((width-100, 0), '6', font=myfont, fill=fillcolor)
    img.save('result.jpg','jpeg')

    return 0
if __name__ == '__main__':
    image = Image.open('image.jpg')
    add_num(image)
