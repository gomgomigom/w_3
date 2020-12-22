from t_201221.shapes import area_2


def main():
    x = float(input('원의 지름을 입력해 주세요: '))
    print('지름이 {}인 원의 면적은 {}입니다.\n'.format(x, area_2.circle(x)))

    y = float(input('정사각형의 변의 길이를 입력해 주세요: '))
    print('변의 길이가 {}인 정사각형의 면적은 {}입니다.'.format(y, area_2.square(y)))


if __name__ == '__main__':
    main()

