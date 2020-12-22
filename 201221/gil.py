def read_image(filepath):
    img = []
    with open(filepath, 'r') as f:
        data = f.readlines()

    for row in data:
        row = row[:-1]
        img.append([int(bit) for bit in row])
    return img



def invert(img):
    height, width = len(img), len(img[0])
    new_img = empty_image(height, width)
    for i in range(height):
        for j in range(width):
            if img[j][i] == 0:
                new_img[j][i] = 1
            else:
                new_img[j][i] = 0

    return new_img


# invert(img) 함수는 주어진 이미지의 색상을 반전시켜서 새로운 이미지를 리턴해 줍니다. 검은색은 흰색으로, 흰색은 검은색으로 만들어 주는 거죠. 원본 이미지 img는 바뀌면 안 됩니다.
#
# invert(img) 함수 구현을 돕기 위해서 다른 함수들을 만들어 놨는데 이 함수들에 대해서 설명드리겠습니다.
#
# empty_image(height, width) 함수는 높이가 height, 너비가 width인 '비어있는 이미지' (중첩 리스트)를 만들어 줍니다. 리스트의 값은 모두 -1로 채워져 있습니다.
x = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(x)
print(x[1])
x[0][1] = 1
x.append([int(i) for i in range(3)])
print(x[0][1])
print(x)

img = [
    [1, 0, 0],
    [0, 1, 0],
    [1, 0, 1]
]

print(img)
print(img[0][1])
print(len(img))
print(len(img[0]))



# -1로 채워진 새로운 이미지 생성
def empty_image(height, width):
    new_img = []
    for i in range(height):
        new_img.append([-1] * width)
    return new_img


height, width = len(img), len(img[0])
new_img = empty_image(height, width)
for i in range(height):
    for j in range(width):
        if img[j][i] == 0:
            new_img[j][i] = 1
        else:
            new_img[j][i] = 0


print(new_img)


img = []
with open("img1", 'r') as f:
    data = f.readlines()
cc = []
print(data)
for a in data:
    a = a[:-1]
    cc.append([int(b) for b in a])
print(cc)

for row in data:
    row = row[:-1]
    img.append([int(bit) for bit in row])

print(img)