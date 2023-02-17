from PIL import Image


try:
    input_image = Image.open(input("image exact name> "))
except:
    print("\nwrong name.")
    exit()
    
pixel_map = input_image.load()
width, height = input_image.size

counter = -1
message = input("\nmessage>  ").replace(" ", "")
bin_message = ''.join('{0:08b}'.format(ord(i)) for i in message) # Bien
bin_pairs_string = ' '.join(bin_message[i:i+2] for i in range(0, len(bin_message), 2))
bin_pairs = bin_pairs_string.split()


for i in range(width):
    for j in range(height):
        if counter >= len(message)-1:
            break

        r, g, b = input_image.getpixel((i, j))
        rbin = str('{0:08b}'.format(r))
        gbin = str('{0:08b}'.format(g))
        bbin = str('{0:08b}'.format(b))
        
        newr = ""
        newg = ""
        newb = ""

        try:
            newr = int((rbin[:-2] + bin_pairs.pop(0)), 2)
            newg = int((gbin[:-2] + bin_pairs.pop(0)), 2)
            newb = int((bbin[:-2] + bin_pairs.pop(0)), 2)
        except IndexError:
            break
        
        new_pixel = []
        if newr != "":
            new_pixel.append(newr)
        else:
            new_pixel.append(r)

        if newg != "":
            new_pixel.append(newg)
        else:
            new_pixel.append(g)

        if newb != "":
            new_pixel.append(newb)
        else:
            new_pixel.append(b)
        pixel_map[i, j] = tuple(new_pixel)

output_name = input("Output image name: ")

input_image.save(f"{output_name}.png", 'png')
