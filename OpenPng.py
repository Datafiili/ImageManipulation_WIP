## ----- Open Png ----- ##
#Written By: Aarni Junkkala

#http://www.libpng.org/pub/png/spec/1.2/PNG-Chunks.html

class Image:
    Width = 0 #4 byte
    Height = 0 #4 byte
    BitDepth = 0 # 1 byte
    
    # -- COLORTYPE RULES -- #
    ColorType = 0 # 1 byte
    #Color    Allowed    Interpretation
    #Type    Bit Depths
    #0       1,2,4,8,16  Each pixel is a grayscale sample.
    #2       8,16        Each pixel is an R,G,B triple.   
    #3       1,2,4,8     Each pixel is a palette index; a PLTE chunk must appear.   
    #4       8,16        Each pixel is a grayscale sample, followed by an alpha sample.   
    #6       8,16        Each pixel is an R,G,B triple, followed by an alpha sample.
    
    CompressionMethod = 0 # 1 byte
    FilterMethod = 0 # 1 byte
    InterlaceMethod = 0 # 1 byte, Value 0 = "no interlace" or 1 = "Adam7 interlace"
    
    
    
    def TurnBytes(self,FileName):
        Bytes = []
        with open(FileName, 'rb') as in_file:
            while True:
                BytesData = in_file.read(1)#.hex()     
                if len(BytesData) == 0:
                    break
                Bytes.append(BytesData[0])
        return Bytes

    def CheckFileSignature(self,Bytes):
        if Bytes[:8] == [137,80,78,71,13,10,26,10]:
            return True
        else:
            return False

    def Chunk(self,Bytes,index):
        #Calculates the lenght of the data.
        #Lenght = 4 bytes
        Lenght = self.BytesToDecimal(Bytes[index:index+4])
        Type = Bytes[index + 4: index + 8]
        Data = Bytes[index + 8: index + 8 + Lenght]
        CRC = Bytes[index + 8 + Lenght: index + 8 + Lenght + 4]
        
        print("Lenght:",Lenght)
        print("Type:",Type)
        print("Type:",chr(Type[0])+chr(Type[1])+chr(Type[2])+chr(Type[3]))
        print("DATA:",Data)
        print("CRC:",CRC)
        print("#------------------------------------------#")
        
        # -- Calling a function depending on the chunck -- #
        if Type == [73, 72, 68, 82]:
            self.IHDR(Data)
        if Type == [115, 82, 71, 66]:
            self.sRGB(Data)
        if Type == [103, 65, 77, 65]:
            self.gAMA(Data)
        if Type == [112, 72, 89, 115]:
            self.pHYs(Data)
        if Type == [73, 69, 78, 68]:
            self.IEND()
        
        return index + Lenght + 12

    def IHDR(self,Data):
        # -- Sets data from IHDR -- #
        self.Width = self.BytesToDecimal(Data[0:4]) #4 byte
        self.Height = self.BytesToDecimal(Data[4:8]) #4 byte
        self.BitDepth = Data[8] # 1 byte
        self.ColorType = Data[9] # 1 byte
        self.CompressionMethod = Data[10] # 1 byte
        self.FilterMethod = Data[11] # 1 byte
        self.InterlaceMethod = Data[12] # 1 byte
        
        print("# -- IHDR -- #")
        print("Width:",self.Width)
        print("Height:",self.Height)
        print("BitDepth:",self.BitDepth)
        print("ColorType:",self.ColorType)
        print("CompressionMethod:",self.CompressionMethod)
        print("FilterMethod:",self.FilterMethod)
        print("InterlaceMethod:",self.InterlaceMethod)
        print("# -- ---- -- #")
        
    def PLTE(self,Data):
        pass
    
    def tRNS(self,Data):
        #if self.ColorType == 3: #Contains one byte values that corresponds to palette
            #0 = full transparency, 255 = no trasnparency
        pass  
    
    def cHRM(self,Data):
        pass
    
    def sRGB(self,Data): # Standard RGB
        pass
    
    def gAMA(self,Data):
        pass
    
    def pHYs(self,Data):
        pass
    
    def IEND(self):
        print("Processing image done!");
        pass
    
    def BytesToDecimal(self,Bytes):
        Lenght = 0
        for i in range(len(Bytes)):
            Lenght += 2 ** ((3-i)*8) * Bytes[i]
        return Lenght
    
    def Setup(self):
        H = self.TurnBytes("ShotgunShell.png")
        print(H)
        A = self.CheckFileSignature(H)
        print(A)
        Index = 8
        while Index < len(H):
            Index = self.Chunk(H,Index)

    def __init__(self):
        self.Setup()

A = Image()