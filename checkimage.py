from PIL import Image

try:
    input_image = Image.open(input("\nexact image name> "))
except:
    print("\nwrong name.")
    exit()
pixel_map = input_image.load()

width, height = input_image.size

bits = ""
limit = int(input("how many bits do you want to see?> "))

for i in range(width):
    for j in range(height):
        r, g, b = input_image.getpixel((i,j))
        #print(r, g, b)
        bits += str('{0:08b}'.format(r))[-2:]
        bits += str('{0:08b}'.format(g))[-2:]
        bits += str('{0:08b}'.format(b))[-2:]
        if len(bits) >= limit:
            bits = " ".join(bits[i:i+8] for i in range(0, len(bits), 8))
            print(bits)
            exit()
