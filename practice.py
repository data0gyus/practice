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
# target이 문자열 my_string의 부분 문자열이라면 1 아니면 0을 return


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

# 정수 n이 주어질 때, n을 문자열로 변환하여 return


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
# num_str 자체가 iterable이기 때문에 list로 변환하는 작업은 꼭 필요한 것은 아니다.

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
"""

# 코딩테스트 기초 테스트 - 뒤에서 5등 위로
# 정수로 이루어진 리스트 num_list가 주어집니다.
# num_list에서 가장 작은 5개의 수를 제외한 수들을 오름차순으로 담은 리스트를 return하도록 solution 함수를 완성해주세요.


def solution(num_list):
    num_list.sort()
    return num_list[5:]


def solution(num_list):
    return sorted(num_list[5:])

# sort() 함수 : list.sort()로 사용이 되며 list 객체 자체를 정렬해주는 함수입니다.
# sorted() : 순서대로 정렬, 정렬된 리스트를 반환
# 기본값은 오름차순 정렬, reverse=True 는 내림차순 정렬 key = '조건' : key 옵션에 지정된 함수의 결과에 따라 정렬
# reverse() 함수 : 리스트를 거꾸로 뒤집는다. desc 정렬 X
# reversed() : 거꾸로 뒤집기, iteravle한 객체를 반환하기 때문에 list로 한번 더 변형 필요


# 슬라이싱 [시작 인덱스 : 끝 인덱스]
# 콜론 왼쪽 숫자 = 우리가 추출하기 원하는 시작 인덱스
# 콜론 오른쪽에 써주는 숫자 = 우리가 추출하기 원하는 끝 인덱스 + 1
# [:] 처음부터 끝까지
# [start:] start오프셋(인덱스)부터 끝까지
# [:end] 처음부터 end-1 오프셋(인덱스)까지
# [start: end] start오프셋부터 end-1 오프셋(인덱스)까지
# [start: end : step] step만큼 문자를 건너뛰면서, 위와 동일하게 추출

# 코딩 기초 트레이닝 - 배열의 길이에 따라 다른 연산하기
# 정수 배열 arr과 정수 n이 매개변수로 주어집니다.
# arr의 길이가 홀수라면 arr의 모든 짝수 인덱스 위치에 n을 더한 배열을,
# arr의 길이가 짝수라면 arr의 모든 홀수 인덱스 위치에 n을 더한 배열을
# return 하는 solution 함수를 작성해 주세요.

def solution(arr, n):
    if len(arr) % 2 == 0:
        for i in range(0, len(arr), 2):
            arr[i] += n
    else:
        for i in range(1, range(arr), 2):
            arr[i] += n
    return arr

# 다른 사람 풀이


def solution(arr, n):
    N = len(arr)
    if N % 2:
        for i in range(0, N, 2):
            arr[i] += n
    else:
        for i in range(1, N, 2):
            arr[i] += n
    return arr


def solution(arr, n):
    answer = []
    if len(arr) % 2 == 0:
        for idx, value in enumerate(arr):
            if idx % 2 == 1:
                answer.append(value+n)
            else:
                answer.append(value)
    else:
        for idx, value in enumerate(arr):
            if idx % 2 == 0:
                answer.append(value+n)
            else:
                answer.append(value)

    return answer

# enumerate(iterable, start=0) 함수 :
# 반복 가능한 객체를 인자로 받아서 해당 객체의 요소들을 순회하면서 각 요소의 인덱스와 값을 순서쌍으로 반환
# iterable : 반복 가능한 객체 (list, tuple, str, dictionary)
# start : 인덱스의 시작값을 설정, 기본값은 0
# for 문과 주로 함께 사용됨
# for idx, value in enumerate(arr):
# 0 49
# 1 12 형식으로 나오게 됨
# 따라서 전체 if문에서 짝수 판별, 다음 for문에서 idx가 홀수 판별 값 넣기 진행

# 코딩 기초 테스트 - 배열 비교하기
# 두 배열의 길이가 다르다면, 배열의 길이가 긴 쪽이 더 큽니다.
# 배열의 길이가 같다면 각 배열에 있는 모든 원소의 합을 비교하여
# 다르다면 더 큰 쪽이 크고, 같다면 같습니다.
# 두 정수 배열 arr1, arr2가 주어질 때
# arr2가 크다면 -1 , arr1이 크다면 1, 두 배열이 같다면 0을 return


def solution(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    s1 = sum(arr1)
    s2 = sum(arr2)
    if n1 > n2:
        return 1
    elif n1 < n2:
        return -1
    else:
        if s1 > s2:
            return 1
        elif s1 < s2:
            return -1
        else:
            return 0

# 다른 사람 풀이


def solution(arr1, arr2):
    return (len(arr1) > len(arr2)) - (len(arr2) > len(arr1)) or (sum(arr1) > sum(arr2)) - (sum(arr2) > sum(arr1))

# 코딩 기초 테스트 - 배열의 원소만큼 추가하기
# 양의 정수 배열 arr가 매개변수로 주어질 때,
# arr의 앞에서부터 차례대로 원소를 보면서 원소가 a라면 X의 맨 뒤에
# a를 a번 추가하는 일을 반복한 뒤, 배열 X를 return


def solution(arr):
    answer = []
    for i in arr:
        answer += [i]*i
    return answer

# 다른 사람 풀이


def solution(arr):
    answer = []
    for i in range(len(arr)):
        for j in range(arr[i]):
            answer.append(arr[i])
    return answer


def solution(arr):
    answer = []
    for x in arr:
        for i in range(x):
            answer.append(x)
    return answer

# 안 풀었던 코딩테스트 입문 - 세균 증식
# 1시간에 2배만큼 증식하는 세균.
# 처음 세균의 마리수 n 과 경과한 시간 t가 주어질 때, t시간 후의 세균 수를 return


def solution(n, t):
    return n * (2 ** t)

# 다른 사람 풀이


def solution(n, t):
    return n << t

# 비트 시프트 (<< , >>)
# 왼쪽 시프트 연산자(<<) : 2를 곱한 갓과 같은 효과 ex) n << m : m * 2의 m승
# 오른쪽 시피트 연산자(>>) : 2로 나눈 것과 같은 효과 ex) n >> m : n/2의 m승


# 자릿수 더하기

def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)
    return answer


def solution(n):
    return sum(map(int, str(n)))
#   retrun sum(list(map(int,list(str(n)))))


def solution(n):
    return sum(int(i) for i in str(n))

# 특정 문자열 제거


def solution(my_string, letter):
    return my_string.replace(letter, '')


def solution(my_string, letter):
    answer = ''
    for string in my_string:
        if string != letter:
            answer += string
    return answer


# 홀짝 구분하기
a = int(input())
if a % 2 == 0:
    print(a, 'is even')
else:
    print(a, 'is odd')

a = int(input())
if a % 2 == 0:
    print(f'{a} is even')
else:
    print(f'{a} is odd')

a = int(input())
print(f"{a} is odd" if a % 2 else f"{a} is even")
