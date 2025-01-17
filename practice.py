"""N = int(input())

for n in range(N):
    print("123")





def solution(price):
    if price >= 500000:
        return int(price*0.8)
    elif price >= 300000 and price < 500000:
        return int(price * 0.9)
    elif price >= 100000 and price < 300000:
        return int(price * 0.95)
    else:
        return int(price)
# 코딩 테스트 입문 - 직각 삼각형 만들기
# "*"의 높이와 너비를 1이라고 했을 때, "*"을 이용해 직각 이등변 삼각형을 그리려고합니다.
# 정수 n 이 주어지면 높이와 너비가 n 인 직각 이등변 삼각형을 출력하도록 코드를 작성해보세요.

n = int(input())
for i in range(1, n+1):
    print(i*"*")


# 가위는 2 바위는 0 보는 5로 표현합니다.
# 가위 바위 보를 내는 순서대로 나타낸 문자열 rsp가 매개변수로 주어질 때,
# rsp에 저장된 가위 바위 보를 모두 이기는 경우를 순서대로 나타낸 문자열을 return하도록 solution 함수를 완성해보세요.


def solution(rsp):
    d = {"2": "0", "0": "5", "5": "2"}
    return ''.join(d[i] for i in rsp)


def solution(rsp):
    answer = ''
    for s in rsp:
        if (s == '2'):
            answer += '0'
        elif (s == '0'):
            answer += '5'
        elif (s == '5'):
            answer += '2'
    return answer


rsp = input()

answer = ''
for s in rsp:
    if (s == '2'):
        answer += '0'
    elif (s == '0'):
        answer += '5'
    elif (s == '5'):
        answer += '2'
print(answer)

# 코딩테스트 입문 - 숨어있는 숫자의 덧셈(1)

# 문자열 my_string이 매개변수로 주어집니다.
# my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

def solution(my_string):
    answer = [int(x) for x in my_string if x.isdigit()]
    return sum(answer)

# 문자열.isdigit()은 문자열이 '숫자'로만 이루어져있는지 확인하는 함수로
# my_string의 각 문자 x를 순회하면서 x가 숫자인지 확인하고 
# 숫자라면 int(x)를 통해 문자열 형태의 숫자를 정수로 변환하여 리스트에 추가
# 결과적으로 answer리스트는 정수의 형태로 구성됨 


# 코딩테스트 입문 - 아이스 아메리카노

# 아이스 아메리카노는 한잔에 5,500원입니다.
# 머쓱이가 가지고 있는 돈 money가 매개변수로 주어질 때,
# 머쓱이가 최대로 마실 수 있는 아메리카노의 잔 수와 남는 돈을 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.


def solution(money):
    price = 5500
    return [money // price, money % price]

# 더하기 + , 빼기 - , 곱셈 * , 나눗셈 /
# 정수 나누기 연산자 = 몫 //
# 나머지 연산자 %
# 제곱 연산자 **

"""

# 코딩테스트 기초 트레이닝 - 꼬리 문자열
# 문자열 리스트 str_list와 제외하려는 문자열 ex가 주어질 때,
# str_list에서 ex를 포함한 문자열을 제외하고 만든 꼬리 문자열을 return하도록 solution 함수를 완성해주세요.


def solution(str_list, ex):
    answer = ''
    for i in str_list:
        if ex not in i:
            answer += 1
    return answer

# 부분 문자열 또한 다음과 같이 해결가능
# 문자열 my_string 과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1 아니면 0을 retrun


def solution(my_string, target):
    if target in my_string:
        return 1
    return 0


def solution2(my_string, target):
    return int(target in my_string)

# 정수 배열 arr과 delete_list가 있습니다.
# arr의 원소 중 delete_list의 원소를 모두 삭제하고
# 남은 원소들은 기존의 arr에 있던 순서를 유지한 배열을 return 하는 solution 함수를 작성해 주세요.


def solution(arr, delete_list):
    return [x for x in arr if x not in delete_list]

# 파이썬 데이터 변환
# 정수 변환 = int() : True 는 1, False 는 0으로 변환
# 실수 변환 = float()
# 문자열 변환 = str()
# 문자 변환 = chr()
# 불리언 변환 = bool() : 숫자는 -인지 아닌지에 따라서 결정 / 문자는 비었는지 안 비었는지에 따라서 결정

# 정수 n이 주어질 때, n을 문자열로 변환하여 retrun


def solution(n):
    return str(n)

# 0 떼기
# 정수로 이루어진 문자열 n_str이 주어질 때,
# n_str의 가장 왼쪽에 처음으로 등장하는 0들을 뗀 문자열을 return하도록 solution 함수를 완성해주세요.


def solution(n_str):
    return n_str.lstrip('0')


def solution(n_str):
    for i in range(len(n_str)):
        if n_str[i] != '0':
            return n_str[i:]

# 공백과 문자 제거 함수
# strip() : 양쪽 문자열에 공백이나 문자열의 모든 조합을 제거
# ex) 'apple'.strip('ae') -> 'ppl'
# lstrip() : 문자열 왼쪽 공백이나 인자로 여러 문자를 전달하면 그 문자들과 동일한 것들을 모두 제거,
# ex) 'apple'.lstrip('ap') -> 'le'
# rstrip() : 문자열 오른쪽 공백이나 인자가 된 문자열의 모든 조합을 제거
# ex) 'apple'.rstrip('lep') -> 'a'

# 인자로 전달된 한 문자와 동일한 개체는 모두 제거, 동일하지 않은 문자가 나올 때까지 진행
# 인자로 여러 문자를 전달하면, 그 문자들과 동일한 것들을 모두 제거, 동일하지 않은 문자가 나올 때까지 진행
# text = "rrrrr865.....pretty....rr,,,,"
# print(text.strip(',865.r'))
# result -> [pretty]
# ',' '.' '8' '6' '5' 다 각각 확인 하기 때문에 pretty만 남게됨


# 문자열 정수의 합
# 한 자리 정수로 이루어진 문자열 num_str이 주어질 때, 각 자리수의 합을 return하도록 solution 함수를 완성해주세요.

def solution(num_str):
    return sum(map(int, list(num_str)))
# list로 변환하지 않아도 됨
# map 함수는 주어진 함수를 반복 가능한 객체(iterable)의 모든 항목에 적용하고, 결과를 반환합니다.
# 여기서 문자열도 시퀀스이기에 당연히 반복 가능한 객체이며, 때문에 각 문자에 대해 int 함수를 적용할 수 있습니다.


def solution(num_str):
    answer = 0
    a = []

    for i in range(len(num_str)):
        a.append(int(num_str[i]))

    for i in range(len(a)):
        answer += a[i]


def solution(num_str):
    return sum([int(i) for i in num_str])

# map(function, iterable)
# map() 함수는 여러 개의 데이터를 받아서 각 요소에 함수(function)를 적용한 결과를 반환한다.
# iterable 객체를 입력으로 받을 수 있다.
