def actualMemorySize(sizeStr):
    ending = sizeStr[-2:]
    number = float(sizeStr[:-2])
    realSize = number * 0.93

    if ending == "GB":
        if realSize >= 1:
            return f"{realSize:.2f}GB"
        else:
            return f"{int(realSize * 1000)}MB"
    elif ending == "MB":
        return f"{int(realSize)}MB"


print(actualMemorySize("32GB"))
print(actualMemorySize("2GB")) 
print(actualMemorySize("0.9GB"))
print(actualMemorySize("512MB"))
