from PIL import Image, ImageChops

if __name__ == "__main__":
    image1 = Image.open("image.png").convert("1")
    image2 = Image.open("image2.png").convert("1")
    r = ImageChops.logical_xor(image1, image2)
    r.save("res.png")
