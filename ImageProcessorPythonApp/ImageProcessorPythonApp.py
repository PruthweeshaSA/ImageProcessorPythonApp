from PIL import Image
import math


def getQuadrantSummary(image,octant):
    width, height = image.size
    halfWidth=math.floor(width/2)
    halfHeight=math.floor(height/2)
    quadrantSummary=1
    octantHorizontal = [1,0,-1,-1,-1,0,1,1][quadrant]
    octantVertical = [0,1,1,1,0,-1,-1,-1][quadrant]
    for i in range(0,halfWidth):
        quadrantSummary*=image.getpixel(halfWidth+octantHorizontal*i, halfHeight+octantVertical*i)
    return quadrantSummary




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
    vectorTotal=1

    for i in range(0,half_dimension):
        x = half_dimension
        primes=[2,3,5,7,11,13,17,19]
        r[i]=[0, 0, 0, 0, 0, 0, 0, 0]
        total=0
        
        r[i][0],g,b = output_image.getpixel((x+i,x))
        total=total+r[i][0]
        vectorTotal*=primes[0]**i

        r[i][1],g,b = output_image.getpixel((x+i,x-i))
        total=total+r[i][1]
        vectorTotal*=primes[1]**i

        r[i][2],g,b = output_image.getpixel((x,x-i))
        total=total+r[i][2]
        vectorTotal*=primes[2]**i
        
        r[i][3],g,b = output_image.getpixel((x-i,x-i))
        total=total+r[i][3]
        vectorTotal*=primes[3]**i
        
        r[i][4],g,b = output_image.getpixel((x-i,x))
        total=total+r[i][4]
        vectorTotal*=primes[4]**i
        
        r[i][5],g,b = output_image.getpixel((x-i,x+i))
        total=total+r[i][5]
        vectorTotal*=primes[5]**i
        
        r[i][6],g,b = output_image.getpixel((x,x+i))
        total=total+r[i][6]
        vectorTotal*=primes[6]**i
        
        r[i][7],g,b = output_image.getpixel((x+i,x+i))
        total=total+r[i][7]
        vectorTotal*=primes[7]**i
        
        print(total)
        print(vectorTotal)
# end of main

if __name__ == '__main__':
    main()  # next section explains the use of sys.exit


