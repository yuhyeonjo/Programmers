a, b = map(int, input().strip().split(' '))

def star() :
    
    # global 변수 참조
    global a, b
    
    # a번 열, b번 행
    for _ in range(b) :
        print("*" * a)

star()