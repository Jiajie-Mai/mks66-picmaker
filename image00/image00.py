import math

cols = 500
rows = 500
maxVal = 255

def header():
    f = open('image.txt','a')
    f.write("P3" + "\n")
    f.write(str(cols) + " " + str(rows) + "\n")
    f.write(str(maxVal) + "\n")
    f.close

def pixels():
    f = open('image.txt','a')
    for r in range(rows):
        for c in range(cols):
            if ( (r - 250) ** 2 + (c - 250) ** 2 <= 150 ** 2):
                red   = int(c/10 + 200)
                green = int((500 - r)/2)
                blue  = int(r/100)
            else:
                red   = int((500 - r)/2)
                green = int((500 - c)/2)
                blue  = int(r/3)
            f.write(str(red)+" ")
            f.write(str(green)+" ")
            f.write(str(blue)+" \t")
        f.write("\n")
    f.close()

def main():
    header()
    pixels()
    
main()
