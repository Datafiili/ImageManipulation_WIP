
def TurnHex(FileName):
    Hex = ""
    with open(FileName, 'rb') as in_file:
        while True:
            hexdata = in_file.read(16).hex()     # I like to read 16 bytes in then new line it.
            if len(hexdata) == 0:                # breaks loop once no more binary data is read
                break
            Hex += hexdata.upper()# I also like it all in caps.
    return Hex


def FileFormat(Hex):
    if(H[:16] == "89504E470D0A1A0A"): #PNG has always this begining
        return "PNG"
    return False

def ReadChunk(Hex,index):
    LenghtInBytes = int(Hex[index:index+8],16)
    print(LenghtInBytes)
    ChunkType =bytearray.fromhex(Hex[index+8:index+16]).decode()
    print(ChunkType)
    ChunkData = Hex[index+ 16:index + 16 + LenghtInBytes]
    print(ChunkData)
    CRC = Hex[index+ 16 + LenghtInBytes: index+ 16 + LenghtInBytes + 4]
    print(CRC)
H = TurnHex("Kuva.png")    
ReadChunk(H,16)

