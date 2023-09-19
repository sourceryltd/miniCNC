from PIL import Image
import glob
import os
import sys

def decodePixel(pixeldata):
    byte = int(HexString, 16)
    return (a, r, g, b)

def Extract(filename):
    ImageFile = open(filename, "r").read()

    # Extrat image resolution
    ImageData = ImageFile.split("#if LV_COLOR_DEPTH")
    ImageResolution = ImageData[len(ImageData) -1].split(".header")
    ImageWidth = int(ImageResolution[2].split('= ')[1].replace(",", "").strip())
    ImageHeight = int( ImageResolution[3].split('= ')[1].split(",")[0])

    ImageData = ImageFile.split("#if LV_COLOR_DEPTH")[1]
    ImageData = ImageData.replace("#endif", "")
    ImageData = ImageData.replace("\n", "")
    ImageData = ImageData.replace(" ", "")
    ImageData = ImageData.split("/")[2]
    ImageData = ImageData.split("}")[0]
    ImageData = ImageData.rstrip(",")

    PNG_32 = ImageData.split(",")

    hexbytes = ImageData.replace("0x", "")
    hexbytes = hexbytes.replace(",", "")
    hexbytes = "0x" + hexbytes
    return ImageWidth, ImageHeight, PNG_32, hexbytes

def GenerateImage(filename, width, height, byteData, hexbytes):
    img = Image.frombytes("LA", (width, height), hexbytes)
    img.save(filename.replace(".c", ".png"))



FileList = glob.glob('./lvgl_ui/*.c')

for x in range(len(FileList)-1):
    try:
        imageData = Extract(FileList[x])
        GenerateImage(FileList[x], imageData[0], imageData[1], imageData[2], imageData[3])
    except:
           print ("Error in file: " + FileList[x])
