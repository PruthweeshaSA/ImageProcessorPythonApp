from PIL import Image
import math


def main():
    input_image = Image.open("C:\\Users\\Pruthweesha\\Downloads\\DL\\Bandipur.jpg")
    # Extracting pixel map:
    pixel_map = input_image.load()

    width = 0
    height = 0

    width, height = input_image.size
  
    # taking half of the width:
    for i in range(width):
        for j in range(height):
        
            # getting the RGB pixel value.
            r, g, b = input_image.getpixel((i, j))
          
            # Apply formula of grayscale:
            grayscale = 255 if ( (0.299*r + 0.587*g + 0.114*b) > 127 ) else 0
  
            # setting the pixel value.
            pixel_map[i, j] = (int(grayscale), int(grayscale), int(grayscale))
  
    # Saving the final output
    # as "grayscale.png":
    input_image.save("C:\\Users\\Pruthweesha\\Downloads\\DL\\grayscale.png", format="png")


    output_image = Image.open("C:\\Users\\Pruthweesha\\Downloads\\DL\\grayscale.png")
    output_image.show()

    smaller_dimension = 0

    if(width<height):
        smaller_dimension = width
    else:
        smaller_dimension = height

    smaller_dimension = math.floor(smaller_dimension)
    rows, cols = (smaller_dimension/2, 8)
    rows = math.floor(rows)
    r = [[0]*cols]*rows

    half_dimension = math.floor(smaller_dimension/2)
    

    for i in range(0,half_dimension):
        x = half_dimension
        r[i]=[0, 0, 0, 0, 0, 0, 0, 0]
        total=0
        r[i][0],g,b = output_image.getpixel((x+i,x))
        total=total+r[i][0]
        r[i][1],g,b = output_image.getpixel((x+i,x-i))
        total=total+r[i][1]
        r[i][2],g,b = output_image.getpixel((x,x-i))
        total=total+r[i][2]
        r[i][3],g,b = output_image.getpixel((x-i,x-i))
        total=total+r[i][3]
        r[i][4],g,b = output_image.getpixel((x-i,x))
        total=total+r[i][4]
        r[i][5],g,b = output_image.getpixel((x-i,x+i))
        total=total+r[i][5]
        r[i][6],g,b = output_image.getpixel((x,x+i))
        total=total+r[i][6]
        r[i][7],g,b = output_image.getpixel((x+i,x+i))
        total=total+r[i][7]
        print(total)
# end of main

if __name__ == '__main__':
    main()  # next section explains the use of sys.exit


