# 바이너리 파일 읽기 img

with open("owl.png","rb") as file:
    # data = file.read()
    # print(len(data))

    header = file.read(10) # 최대 10바이트 # 파일 확장자를 찾는 방법
    print(header)

def files(file_path): # 바이너리 읽기
    with open(file_path, "rb") as file:
        header = file.read(4)
        print(header)

        if header == 'X89PNG':
            return "png"
        elif header == "\xff\xd8":
            return "jpg"
        else:
            return "unknown"

files("owl.png")
files("cat03.jpg")

# 바이너리 파일 쓰기

with open("owl.png", "rb") as file:
    data = file.read()

with open("owl_copy.png","wb") as file:
    file.write(data)