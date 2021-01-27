# Lab 09
# 30 points
# Nuria Perez Casas

import cImage

def kaleidoscope():
    """This function takes a squared image and makes a kaleidoscope
    out of it and it allows you to save afterwards. 
    """
    # Task 1
    # Create a kaleidoscope from an image
    # Slice into 8 pieces, copy one of them
    # to cover all 8 regions
    # 1. Find an appropriate .gif image, keep size under
    #    1000x1000 for sure, 500x500 is about right
    #    (the image should be square unless you really want
    #     to do some extra work to make rectangular images work)
    # 2. Modify the code below, now copy the 1/8 region
    #    into the other 6 untouched areas
    # 3. Optionally, save the image to have a copy to keep
    fileName = "landscape.gif"
    windowName = "Kaleidoscope"

    image = cImage.FileImage(fileName)
    height = image.getHeight()
    width = image.getWidth()

    window = cImage.ImageWin(windowName, width, height)
    image.draw(window)

    for row in range(height // 2):
        for col in range(row):
            pixel = image.getPixel(col, row)
            image.setPixel(row, col, pixel)
            image.setPixel(height - row, width - col, pixel)
            image.setPixel(height - col, width - row, pixel)
            image.setPixel(height // 2 + row, width // 2 - col, pixel)
            image.setPixel(width // 2 + col, height // 2 - row, pixel)
            image.setPixel(height // 2 - row, width // 2 + col, pixel)
            image.setPixel(width // 2 - col, height // 2 + row, pixel)


    image.draw(window)
    print("Would you like to save the kaleidoscope? ")
    while True:
        response = input("Enter Y or N: ")
        if response.lower() == "y" or response.lower() == "yes":
            image.save('kaleidoscope.gif')
            break
        else:
            break

def posterization():
    """This function takes an image and transforms it into a simpler
    one with only 8 colors. It allows you to save it afterwards.
    """
    # Task 2
    # Simplify an image to use fewer total colors
    # Apply posterization to make the image use
    # only 8 colors. The starting code below
    # gets most of the extra work out of the way
    # so you can focus on the colors.
    fileName = "wave1.gif"
    windowName = "Posterization"
    image = cImage.FileImage(fileName)
    height = image.getHeight()
    width = image.getWidth()
    window = cImage.ImageWin(windowName, width, height)
    image.draw(window)
    for row in range(image.getHeight()):
        for col in range(image.getWidth()):
            pixel = image.getPixel(col, row)
            red = pixel.getRed()
            blue = pixel.getBlue()
            green = pixel.getGreen()

            # If red >> blue, green, make the pixel red!
            if red <= 5 and green <= 5 and blue <= 5:
                pixel.setRed(0)
                pixel.setBlue(0)
                pixel.setGreen(0)
            elif red <= 30 and green <= 50 and blue <= 90:
                pixel.setRed(10)
                pixel.setBlue(74)
                pixel.setGreen(16)
            elif red <= 60 and green <= 110 and blue <= 130:
                pixel.setRed(65)
                pixel.setBlue(130)
                pixel.setGreen(100)
            elif red <= 160 and green <= 170 and blue<= 135:
                pixel.setRed(145)
                pixel.setBlue(131)
                pixel.setGreen(136)
            elif red <= 220 and green <= 185 and blue <= 125:
                pixel.setRed(214)
                pixel.setBlue(121)
                pixel.setGreen(182)
            elif red <= 235 and green <= 210 and blue <= 165:
                pixel.setRed(230)
                pixel.setBlue(163)
                pixel.setGreen(202)
            elif red <= 245 and blue <= 240 and blue <= 220:
                pixel.setRed(244)
                pixel.setBlue(216)
                pixel.setGreen(238)
            elif red <= 245 and blue <= 245 and blue <= 245:
                pixel.setRed(245)
                pixel.setBlue(230)
                pixel.setGreen(240)
            
            # Modify the original image with
            # this new pixel
            image.setPixel(col, row, pixel)
    image.draw(window)
    
    print("Would you like to save the poster? ")
    while True:
        response = input("Enter Y or N: ")
        if response.lower() == "y" or response.lower() == "yes":
            image.save('poster.gif')
            break
        else:
            break
        
def shrink():
    """This function takes an image and shrinks it to half its size.
    It also allows you to save it afterwards. 
    """
    # Task 3
    # Shrink an image down by a factor of 1/2
    # Doesn't have to be perfect
    """

    X.X
    .O.
    X.X


    XZ..XY
    YX..XY
    ..OO..
    ,-LO..
    XH..XZ
    GX..ZZ


    """
    windowName = "Blank"
    fileName = "bluetones.gif"

    image = cImage.FileImage(fileName)
    height = image.getHeight()
    width = image.getWidth()

    newImage = cImage.EmptyImage(width // 2, height // 2)
    newHeight = newImage.getHeight()
    newWidth = newImage.getWidth()
    window = cImage.ImageWin(windowName, newWidth, newHeight)


    for row in range(newHeight):
        for col in range(newWidth):
            pixel1 = image.getPixel(col * 2, row * 2)
            blue1 = pixel1.getBlue()
            pixel2 = image.getPixel(col * 2 + 1, row * 2)
            blue2 = pixel2.getBlue()
            pixel3 = image.getPixel(col * 2, row * 2 + 1)
            blue3 = pixel3.getBlue()
            pixel4 = image.getPixel(col * 2 + 1, row * 2 + 1)
            blue4 = pixel4.getBlue()
            
            if blue1 <= blue2 and blue1 <= blue3 and blue1 <= blue4:    
                newImage.setPixel(col, row, pixel1)
            elif blue2 <= blue1 and blue2 <= blue3 and blue2 <= blue4:    
                newImage.setPixel(col, row, pixel2)
            elif blue3 <= blue1 and blue3 <= blue2 and blue3 <= blue4:    
                newImage.setPixel(col, row, pixel3)
            elif blue4 <= blue1 and blue4 <= blue3 and blue4 <= blue2:    
                newImage.setPixel(col, row, pixel4)
            
    newImage.draw(window)
    
    print("Would you like to save the shrinked image? ")
    while True:
        response = input("Enter Y or N: ")
        if response.lower() == "y" or response.lower() == "yes":
            image.save('small.gif')
            break
        else:
            break
        
def main():
    kaleidoscope()
    posterization()
    shrink()
    
if __name__ == "__main__":
    main()
    





