## -------------------- PNG OPENER -------------------- ##
#Written By: Aarni Junkkala

#To read
#http://www.libpng.org/pub/png/spec/1.2/PNG-Chunks.html

class Image():
    #IHDR Data
    width = -1 # -1 = undefined, max value 2 ** 31
    heigth = -1
    bit_depth = -1 #values 1, 2, 4, 8, or 16
    color_type = -1 # values 0, 2, 3, 4, or 6
    compression_method = -1 #value 0
    filter_method = -1 # value 0, 1, 2, 3 or 4
    interlace_method = -1 #Value 0 = "no interlace" or 1 = "Adam7 interlace"
    
    #PLTE
    ColorPalette = []

#Image variables
Widht = 0
Height = 0


#Turns file into hex
def TurnHex(FileName):
    Hex = ""
    with open(FileName, 'rb') as in_file:
        while True:
            hexdata = in_file.read(16).hex()     
            if len(hexdata) == 0:
                break
            Hex += hexdata.upper()
    return Hex
    

#Check for the file format.
def FileFormat(Hex):
    if(H[:16] == "89504E470D0A1A0A"): #PNG has always this begining
        return "PNG"
    return False

def ReadChunk(Hex,index): #Reads a chunk at a time. Returns [ChunkName,StartIndex,Lenght(Where next chunk start)]
    Data = []
    LenghtInBytes = int(Hex[index:index+8],16)
    ChunkType = bytearray.fromhex(Hex[index+8:index+16]).decode()
    Data.append(ChunkType)
    Data.append(index)
    Data.append(24 + LenghtInBytes * 2)
    return Data

def IHDR(Img,Hex,index):
    print("IHDR KUTSUTTU")
    Img.widht = int(Hex[index+16:index+24],16)
    Img.height = int(Hex[index+24:index+32],16)
    Img.bit_depth = int(Hex[index+32:index+34],16)
    Img.color_type = int(Hex[index+34:index+36],16)
    Img.compression_method = int(Hex[index+36:index+38],16)
    Img.filter_method = int(Hex[index+38:index+40],16)
    Img.interlace_method = int(Hex[index+40:index+42],16)

def sRGB(Img,Hex,index):
    print("sRGB KUTSUTTU")

def PLTE(Img,Hex,index):
    print("PLTE KUTSUTTU")
    LenghtInBytes = int(Hex[index:index+8],16)
    Data = Hex[index+16:index+LenghtInBytes]
    for i in range(int(len(Data) / 6)):
        R = int(Data[i * 6 + 0:i * 6 + 2],16)
        G = int(Data[i * 6 + 2:i * 6 + 4],16)
        B = int(Data[i * 6 + 4:i * 6 + 6],16)
        Img.ColorPalette.append([R,G,B])
    #CONTINUE HERE!!!!
    
def gAMA(Img,Hex,index):
    print("gAMA KUTSUTTU")
    
def pHYs(Img,Hex,index):
    print("pHYs KUTSUTTU")

def IDAT(Img,Hex,index):
    print("IDAT KUTSUTTU")
    
def IEND(Img,Hex,index):
    
    print("IEND KUTSUTTU")

def ConvertPng(ImgName):
    Img = Image()
    Chunks = [] #[ [Chunkname,Index,Lenght], ... ]
    H = TurnHex(ImgName)
    I = 16
    L = 0
    while True:
        C = ReadChunk(H,I + L)
        Chunks.append(C)
        I = C[1]
        L = C[2]
        if I + L >= len(H):
            break

    for C in Chunks:
        print(C)
        s = C[0]
        
        FunktioKutsu = globals()[s]
        FunktioKutsu(Img,H,C[1])
    return Img
Images = []

if __name__ == "__main__":
    Images.append(ConvertPng("Oravapyssyllä.png"))
    print(Images[0].__dict__)
    print(Images[0].ColorPalette)
    print(len(Images[0].ColorPalette))
    print(ReadBinary('Oravapyssyllä.png'))