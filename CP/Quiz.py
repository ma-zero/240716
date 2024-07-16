# ## Quiz 1 : 구구단 3단 만들어보기 대신 멘트는 3 X 3 = 9 처럼 나와야함.
#
# # 1번식
#
# for index in range(1,10) :
#     print("3 x" , index , "=" , int(3*index))
#
# # 2번식
#
# for index2 in range(1,10) :
#     number = 3*index2
#     print("3 x" , index2 , "=" , number )
#
#
# ## Quiz 2 : for 반복문 2번 사용, 2차원 리스트 요소를 모두 출력
#
# num_list = [[10,50], [20,40] , [30,60] , [40,70]]
# for a in num_list :
#     for b in a :
#         print(b)
#
#
# ## Quiz 3 : 다음 이중 리스트의 평균값을 아래 출력 결과와 같이 각각 구해라.
# ## 출력 결과 : 150, 600, 1200
#
# my_list = [[100,200] , [400,800], [1000,1400]]
# for m in my_list :
#     u = 0
#     for h in (m) :
#         u = u + h
#     print(u/len(m))
#
#
# ## Quiz 4 : "10번 찍어 안 넘어가는 나무 없다" 속담을 while 문을 사용하여 구현
#
# check = 0
# while check < 10 :
#     check = check + 1
#     print( "나무를" ,check , "번 찍었습니다.")
# print("나무가 넘어갑니다!")
#
#
# ## Quiz 5 : 네개의 수에 대해 덧셈 함수, 곱셈 함수 코드를 작성하라.
#
# def plus_num(num_1, num_2, num_3, num_4) :
#     result = num_1 + num_2 + num_3 + num_4
#     print(result)
#     return result
#
# def press_num(num_1, num_2, num_3, num_4) :
#     result_2 = num_1 * num_2 * num_3 * num_4
#     print(result_2)
#     return result_2
#
# a = plus_num(1,2,5,6)
# b = press_num(8,5,6,2)
#
#
# ## Quiz 6 : 피라미드 별 찍기
#
# for star in range(1,11) :
#     print("★" * star)
#
#
# ## Quiz 7 : 1부터 100까지 수를 2의 배수, 3의 배수, 5의 배수로 분류하려고 한다.
# ## 2의 배수는 number_1, 3의 배수는 number_2, 5의 배수는 number_3에 저정하는 코드 작성해라.
#
# number_1 = []
# number_2 = []
# number_3 = []
#
# for a in range(1,101) :
#     if a % 2 == 0 :
#         number_1.append(a)
#     if a % 3 == 0 :
#         number_2.append(a)
#     if a % 5 == 0 :
#         number_3.append(a)
#
# print(number_1)
# print(number_2)
# print(number_3)


## Quiz 8 : while 문 사용해서 1~45 사이에 중복이 없는 랜덤한 수 6개 생성, 이를 result 리스트 변수에 추가하는 코드 작성

import random
i = 0
result_13 = []
new_num = []
while i < 6 :
    i = i + 1
    x = random.randint(1,45)
    result_13.append(x)
    if new_num in result_13 :
        print("값이 기존 리스트에 있습니다. 추가하지 않습니다.")
    else :
        result_13.append(i)

print(result_13)