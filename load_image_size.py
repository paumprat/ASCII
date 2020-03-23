from PIL import Image
import numpy as np

# Read your image and print its height and width in pixels

try:
    image=Image.open("image_test.jpg")
    print("The size of the image is: ",image.size)
    #image_bw=image.convert('L')
    #image_bw.save("image_test_ bw.jpg")
    resized_image=image.thumbnail((150,150))
    print("Image successfully loaded")
except:
    print("Image unable to load")
    
#2. Load your image’s pixel data into a 2-dimensional array

pixel_matrix=np.array(image)
row=pixel_matrix.shape[0]
column=pixel_matrix.shape[1]

print(row,column)

print("Successfully constructed pixel matrix")
print("Pixel matrix size: ",column," x ",row)
#Converting each pixel from list into tuple
#for i in range(row):
#    for j in range(column):
#        pixel_matrix[i][j]=tuple(pixel_matrix[i][j])

#3. Convert the RGB tuples of your pixels into single brightness numbers        

brightness_matrix=np.zeros((row,column))
#print(brightness_matrix.shape)

for i in range(row):
    for j in range(column):
        brightness_matrix[i][j]=(float(pixel_matrix[i][j][0])+float(pixel_matrix[i][j][1])+float(pixel_matrix[i][j][2]))/3

print("Successfully constructed brightness matrix")
print("Pixel brightness size: ",len(brightness_matrix[0])," x ",len(brightness_matrix))    

#print("Iterating through pixel brightnesses:")
#for i in range(10):
#    for j in range(10):
#        print(brightness_matrix[i][j])
#print("etc...")

#4. Convert brightness numbers to ASCII characters

ASCII_characters="`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
ASCII_list=list(ASCII_characters)

ASCII_list_size=len(ASCII_list)
#print(ASCII_list_size)                 
max_brightness=np.amax(brightness_matrix)
#print(max_brightness)
intensity_interval=max_brightness/ASCII_list_size


intensity_list=[]
for i in range(ASCII_list_size):
    intensity_list.append(intensity_interval+intensity_interval*i)
    i+=1
#print(intensity_list)
#print(len(intensity_list))
    
ASCII_matrix=np.empty((len(brightness_matrix),len(brightness_matrix[0])),dtype=str)

s=0
for i in range(len(brightness_matrix)):
    for j in range(len(brightness_matrix[0])):
        while brightness_matrix[i][j]>intensity_list[s]:
            s+=1
        ASCII_matrix[i][j]=ASCII_list[s]
        s=0

print("Successfully constructed ASCII matrix")
print("ASCII matrix size: ",len(ASCII_matrix[0])," x ",len(ASCII_matrix))    

print("Iterating through ASCII pixel:")
#for i in range(10):
#    for j in range(10):
#        print(ASCII_matrix[i][j])
#print("etc...")


#5. Print your ASCII art

np.set_printoptions(threshold=np.inf,linewidth=np.inf)

#print(ASCII_matrix)
for i in ASCII_matrix:
    three_characters=[j+j+j for j in i]
    print ("".join(three_characters))
    
    
#for row in ASCII_matrix:
#    line=[p+p+p for p in row]
#    print("".join(line))