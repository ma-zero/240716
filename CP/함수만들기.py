# string = "매개변수를 입력하면, 입력한 매개변수가 화면에 출력됩니다."
# print(string)
# print(len(string))

## 함수 만들기

def 안녕하세요() :
    print("안녕하세요. 만나서 반갑습니다.")


def add_numbers(number_1, number_2) :
    result = number_1 + number_2
    print(result)
    return result

b = add_numbers(1,2)
c = add_numbers(5,7)