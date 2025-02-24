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


# 2025.01.21
# 문자열 바꿔서 찾기


def solution(myString, pat):
    myString = myString.replace("A", "C")
    myString = myString.replace("B", "A")
    myString = myString.replace("B", "A")

    if pat in myString:
        return 1
    else:
        return 0


# x 사이의 개수
def solution(myString):
    answer = []
    myString = myString.split('x')
    for i in range(len(myString)):
        answer.append(len(myString[i]))
    # for i in myString:
    #   answer.append(len(i))
    return answer

# 공백으로 구분하기 2


def solution(my_string):
    return my_string.split()

# ad 제거하기 - 배열 내의 문자열 중 'ad'라는 부분 문자열을 포함하고 있는 문자열은 제거


def solution(strArr):
    return [x for x in strArr if 'ad' not in x]


def solution(strArr):
    answer = []
    for i in strArr:
        if 'ad' not in i:
            answer.append(i)
        else:
            continue
    return answer

# 특정한 문자를 대문자로 바꾸기


def solution(my_string, alp):
    return my_string.replace(alp, alp.upper())


def solution(my_string, alp):
    answer = ''
    for i in my_string:
        if i == alp:
            answer += i.upper()
        else:
            answer += i
    return answer


def solution(my_string, alp):
    answer = []
    for x in my_string:
        if x == alp:
            answer.append(x.upper())
        else:
            answer.append()
    return ''.join(answer)


# 배열에서 문자열 대소문자 변환하기


def solution(strArr):
    for i in range(len(strArr)):
        if i % 2 == 0:
            strArr[i] = strArr[i].lower()
            strArr[i-1] = strArr[i-1].upper()
    return strArr

# 다른 사람 풀이


def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        if i % 2 == 0:
            answer.append(strArr[i].upper())
        else:
            answer.append(strArr[i].lower())
    return answer


def solution(strArr):
    return [s.lower() if i % 2 == 0 else s.upper() for i, s in enumerate(strArr)]

# 소문자로 바꾸기 & 대문자로 바꾸기


def solution(myString):
    return myString.lower()
    return myString.upper()

# 원하는 문자열 찾기


def solution(myString, pat):
    myString = myString.upper()
    pat = pat.upper()
    if pat in myString:
        return 1
    else:
        return 0

# 다른 사람 풀이


def solution(myString, pat):
    return int(pat.lower() in myString.lower())

# 조건에 맞게 수열 변환하기 1


def solution(arr):
    answer = []
    for i in arr:
        if i >= 50 and i % 2 == 0:
            i = i/2
            answer.append(i)
            # answer.append(i/2)
            # answer.append(i//2)
        elif i < 50 and i % 2 != 0:
            i = i * 2
            answer.append(i)
            # answer.append(i*2)
        else:
            answer.append(i)
    return answer

# n보다 커질 때까지 더하기


def solution(numbers, n):
    answer = 0
    for i in numbers:
        if answer > n:
            return answer
        else:
            answer += i
    return answer

# 다른 사람 풀이


def solution(numbers, n):
    answer = 0
    i = 0
    while answer <= n:
        answer += numbers[i]
        i += 1
    return answer

# 할 일 목록


def solution(todo_list, finished):
    answer = []
    for i, v in enumerate(finished):
        if not v:
            answer.append(todo_list[i])
    # for i in range(len(finished)):
    #   if not finished[i]: answer.append(todo_list[i])
        return answer

# 다른 사람 풀이


def solution(todo_list, finished):
    return [work for idx, work in enumerate(todo_list) if not finished[idx]]
    # return [x for x, b in zip(todo_list, finished) if not b]

# 5명씩


def solution(names):
    return [names[i] for i in range(0, len(names), 5)]

# 다른 사람 풀이


def solution(names):
    return names[::5]


def solution(names):
    answer = []
    for i in range(len(names)):
        if i % 5 == 0:
            answer.append(names[i])
    return answer

# 홀수 vs 짝수


def solution(num_list):
    sum1 = 0
    sum2 = 0
    for i in range(len(num_list)):
        if i % 2 == 0:
            sum1 += num_list[i]
        else:
            sum2 += num_list[i]
    if sum1 > sum2:
        return sum1
    else:
        return sum2

# 다른 사람 풀이


def solution(num_list):
    even = 0
    odd = 0

    for i, e in enumerate(num_list):
        if i % 2 == 0:
            even += e
        else:
            odd += e
    return max(even, odd)


def solution(num_list):
    return max(sum(num_list[::2], sum(num_list[1::2])))

# n개 간격의 원소들


def solution(num_list, n):
    return [num_list[i] for i in range(0, len(num_list), n)]

# 다른 사람 풀이


def solution(num_list, n):
    return num_list[::n]


def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i])
    return answer


# n 번째 원소까지

def solution(num_list, n):
    return num_list[:n]


# 순서 바꾸기

def solution(num_list, n):
    return num_list[n:] + num_list[:n]


# n 번째 원소부터

def solution(num_list, n):
    return num_list[n-1:]

# 첫 번재로 나오는 음수


def solution(num_list):
    for i, v in enumerate(num_list):
        if v < 0:
            return i
    return -1


def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i
    return -1


# 가까운 1 찾기
def solution(arr, idx):
    for i, v in enumerate(arr):
        if i >= idx and v == 1:
            return i
    return -1


def solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
    return -1

# 카운트 다운


def solution(start_num, end_num):
    answer = [i for i in range(start_num, end_num-1, -1)]
    return answer


def solution(start_num, end_num):
    answer = []
    for i in range(start_num, end_num-1, -1):
        answer.append(i)
    return answer

# 배열 만들기


def solution(n, k):
    answer = []
    for i in range(n+1):
        if i % k == 0:
            answer.append(i)
    return answer


def solution(n, k):
    return [i for i in range(k, n+1, k)]

# 접두사인지 확인하기


def solution(my_string, is_prefix):
    tmp = [my_string[:i] for i in range(len(my_string))]
    for i in tmp:
        if is_prefix == i:
            return 1
    else:
        return 0


def solution(my_string, is_prefix):
    return int(my_string.istartwth(is_prefix))

# 문자열 앞의 n글자


def solution(my_string, n):
    return my_string[:n]
    # return ''.join(my_string[:n])

# 접미사인지 확인하기


def solution(my_string, is_suffix):
    return int(my_string.endswith(is_suffix))


def solution(my_string, is_suffix):
    answer = 0
    for i in range(len(my_string)):
        if my_string[i:] == is_suffix:
            answer = 1
    return answer

# 접미사 배열


def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[i:])
    answer.sort()
    return answer

# 부분 문자열을 이어 붙여 문자열 만들기


def solution(my_strings, parts):
    answer = ''
    for i, v in enumerate(parts):
        answer += my_strings[i][v[0]:v[1]+1]
    return answer


def solution(my_strings, parts):
    answer = ''
    for i in range(len(parts)):
        l, r = parts[i]
        answer += my_strings[i][l:r+1]
    return answer

# 글자 이어 붙여 문자열 만들기


def solution(my_string, index_list):
    answer = ''
    for i in index_list:
        answer += my_string[i]
    return answer


def solution(my_string, index_list):
    return ''.join([my_string[idx] for idx in index_list])

# 콜라츠 수열 만들기


def solution(n):
    answer = []
    while n != 1:
        # while n > 1 :
        answer.append(n)
        if n % 2 == 0:
            n = n / 2
            # n // 2
        else:
            n = 3 * n + 1
    answer.append(n)
    return answer
# 수 조작하기 1


def solution(n, control):
    answer = n
    con = {'w': +1, 's': -1, 'd': +10, 'a': -10}
    for i in control:
        answer += con[i]
    return answer


def solution(n, control):
    for c in control:
        if c == 'w':
            n += 1
        elif c == 's':
            n -= 1
        elif c == 'd':
            n += 10
        else:
            n -= 10
    return n

# 수 조작하기 2


def solution(numLog):
    answer = ''
    con = {1: 'w', -1: 's', 10: 'd', -10: 'a'}
    for i, v in enumerate(numLog):
        if i != len(numLog)-1:
            answer += con[numLog[i+1]-numLog[i]]
    return answer


def solution(numLog):
    answer = ''
    for i in range(1, len(numLog)):
        diff = numLog[i] - numLog[i-1]
        if diff == 1:
            answer += 'w'
        elif diff == -1:
            answer += 's'
        elif diff == 10:
            answer += 'd'
        elif diff == -10:
            answer += 'a'
    return answer

# 마지막 두 원소


def solution(num_list):
    answer = []
    for i in num_list:
        answer.append(i)
    # for문 대신에
    # answer = num_list도 가능
    if num_list[-1] > num_list[-2]:
        answer.append(num_list[-1] - num_list[-2])
    else:
        answer.append(num_list[-1] * 2)

    return answer

# 원소들의 곱과 합


def solution(num_list):
    mul = 1
    add = 0
    for i in num_list:
        mul *= i
        add += i
    if mul < add * add:
        # if mul < add**2
        return 1
    else:
        return 0


# 문자열 돌리기
str = input()
str = list(str)
for i in str:
    print(i)

for a in input():
    print(a)

# l로 만들기


def solution(myString):
    chars = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12,
             "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}
    char = ""

    for i in myString:
        if chars[i] < 11:
            i = "l"
        char += i

    return char


def solution(myString):
    answer = ''
    for i in myString:
        if i < "l":
            answer += 'l'
        else:
            answer += i
    return answer

# 특이한 이차원 배열 1


def solution(n):
    answer = [[0 for i in range(n)] for j in range(n)]
    # answer = [[0]*n for _ in range(n)] : _(언더바) 반복을 수행하되, 변수 값이 필요 없을 때 사용 가능
    for i in range(n):
        answer[i][i] = 1
    return answer

# 간단한 식 계산하기


def solution(binomial):
    a, op, b = binomial.split()
    if op == '+':
        return int(a) + int(b)
    if op == '-':
        return int(a) - int(b)
    if op == '*':
        return int(a) * int(b)

# 주사위 게임 1


def solution(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return abs(a-b)
    elif a % 2 == 0 or b % 2 == 0:
        return 2 * (a+b)
    elif a % 2 != 0 and b % 2 != 0:
        return a**2 + b ** 2

# 조건에 맞게 수열 변환하기 3


def solution(arr, k):
    answer = []
    if k % 2 == 0:
        for i in arr:
            answer.append(i+k)
        return answer
    else:
        for i in arr:
            answer.append(i*k)
        return answer

# 9로 나눈 나머지


def solution(number):
    a = 0
    num = list(number)
    # 굳이 안해도 됨
    for i in num:
        a += int(i)
    return a % 9


def solution(number):
    return int(number) % 9


def solution(number):
    return sum(map(int, number)) % 9


# 덧셈식 출력하기
a, b = map(int, input().strip().split(''))
print(f'{a}+{b}={a+b}')

a, b = map(int, input().strip().split(''))
print(a, '+', b, '=', a+b)

# 특별한 이차원 배열 2


def solution(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1

# flag에 따라 다른 값 반환하기


def solution(a, b, flag):
    if int(flag) == 1:
        return a + b
    else:
        return a - b


def solution(a, b, flag):
    return a+b if flag else a-b

# 이어 붙인 수


def solution(num_list):
    even = ''
    odd = ''
    for i in num_list:
        if i % 2 == 0:
            even += str(i)
        else:
            odd += str(i)
    return int(even) + int(odd)

# 더 크게 합치기


def solution(a, b):
    q = int(str(a) + str(b))
    w = int(str(b) + str(a))

    if q > w:
        return q
    else:
        return w


def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))
    # return int(max(f'{a}{b}', f'{b}{a}')) 도 가능

# 배열 만들기 3


def solution(arr, intervals):
    a1, b1 = intervals[0]
    a2, b2 = intervals[1]
    return arr[a1:b1+1] + arr[a2:b2+1]


def solution(arr, intervals):
    answer = []
    for a, b in intervals:
        answer += arr[a:b+1]
    return answer


def solution(arr, intervals):
    return arr[intervals[0][0]:intervals[0][1]+1] + arr[intervals[1][0]:intervals[1][1]+1]

# 주사위 게임2


def solution(a, b, c):
    if a == b == c:
        return (a+b+c) * (a**2+b**2+c**2) * (a**3+b**3+c**3)
    elif a != b and a != c and b != c:
        return a+b+c
    elif a == b != c or a == c != b or b == c != a:
        return (a+b+c) * (a**2+b**2+c**2)


def solution(a, b, c):
    check = len(set([a, b, c]))
    if check == 1:
        return 3*a * 3*(a**2) * 3*(a**3)
    elif check == 2:
        return (a+b+c) * (a**2+b**2+c**2)
    else:
        return a+b+c

# 문자열 잘라서 정리하기


def solution(myString):
    str = list(filter(None, myString.split('x')))
    return sorted(str)


def solution(myString):
    return sorted(i for i in myString.split('x') if i)

# 이차원 배열 대각선 순회하기


def solution(board, k):
    answer = []
    # total_sum = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i+j <= k:
                answer.append(board[i][j])
                # total_sum += board[i][j]
    return sum(answer)
    # return total_sum

    # 날짜 비교하기


def solution(date1, date2):
    if date1 < date2:
        return 1
    else:
        return 0


def solution(date1, date2):
    for i in range(3):
        if date1[i] < date2[i]:
            return 1
        elif date1[i] > date2[i]:
            return 0

# 수열과 구간 쿼리 1


def solution(arr, queries):
    for s, e in queries:
        arr = [a+1 if s <= i <= e else a for i, a in enumerate(arr)]
    return arr


def solution(arr, queries):
    for query in queries:
        for i in range(query[0], query[1]+1):
            arr[i] += 1
    return arr


def solution(arr, queries):
    for l, r in queries:
        for i in range(l, r+1):
            arr[i] += 1
    return arr

# 글자 지우기


def solution(my_string, indices):
    str = list(my_string)
    indices.sort(reverse=True)

    for idx in indices:
        del str[idx]
    return ''.join(str)


def solution(my_string, indices):
    answer = ''
    for i in range(len(my_string)):
        if i not in indices:
            answer += my_string[i]
    return answer

# 세로 읽기


def solution(my_string, m, c):
    answer = ''
    for i in range(0, len(my_string), m):
        answer += my_string[i:i+m][c-1]
    return answer


def solution(my_string, m, c):
    answer = ''
    mystr = [list(map(str, my_string[i:i+m]))
             for i in range(0, len(my_string), m)]
    for i in range(len(mystr)):
        answer += mystr[i][c-1]
    return answer

# 등차수열의 특정한 항만 더하기


def solution(a, d, included):
    answer = 0
    tmp = []
    for i in range(0, len(included)):
        tmp.append(a+(d*i))
    # 위에 for문은 굳이 있을 필요 없이 answer에서 더해도 충분

    for j in range(len(included)):
        if int(included[j-1]) == 1:
            # if included[j] == True:
            answer += tmp[j-1]
            # answer += a+i*d
    return answer


def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        answer += (a+d*i) * int(included[i])
    return answer

# 문자열 섞기


def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += str1[i] + str2[i]
    return answer

# 배열의 길이를 2의 거듭제곱으로 만들기


def solution(arr):
    a = len(arr)
    while a & a-1 != 0:
        arr.append(0)
        a += 1
    return arr

# 빈 배열에 추가, 삭제하기


def solution(arr, flag):
    answer = []
    for i in range(len(flag)):
        if flag[i] == True:
            for j in range(arr[i]*2):
                answer.append(arr[i])
            # answer += [arr[i]]* arr[i] * 2
            # answer.extend([arr[i]] * (arr[i] * 2))
        else:
            for j in range(arr[i]):
                answer.pop()
            # answer = answer[:-arr[i]]
    return answer


def solution(arr, flag):
    arr1 = []
    for i, j in zip(arr, flag):
        if j:
            arr1 += [i] * i * 2
        else:
            arr1 = arr1[:-i]
    return arr1

# 문자열이 몇 번 등장하는지 세기


def solution(myString, pat):
    cnt = 0
    a = len(pat)
    for i in range(len(myString)):
        if myString[i:i+a] == pat:
            cnt += 1
    return cnt


def solution(myString, pat):
    answer = 0
    for i, x in enumerate(myString):
        if myString[i:].startswith(pat):
            answer += 1
    return answer


def solution(myString, pat):
    end = myString.rfind(pat)

    return myString[:end + len(pat)]
# rfind : 오른쪽부터 (끝부분부터) 주어진 문자열을 찾기 시작함
# rindex : 오른쪽부터 (끝부분부터) 주어진 문자를 찾기 시작함

# 1로 만들기


def solution(num_list):
    answer = 0
    for i in num_list:
        while i > 1:
            if i % 2 == 0:
                answer += 1
                i = i // 2
            else:
                answer += 1
                i = (i-1) // 2
    return answer

# 문자열 뒤집기


def solution(my_string, s, e):
    for i in range(len(my_string)):
        str = list[my_string[s:e]]
        str.reverse()
    return my_string[:s] + ''.join(str) + my_string[e+1:]


def solution(my_string, s, e):
    return my_string[:s]+my_string[s:e+1][::-1]+my_string[e+1:]

# 배열 만들기


def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        if int(i[s:s+l]) > k:
            answer.append(int(i[s:s+l]))
    return answer


def solution(intStrs, k, s, l):
    return [int(intStrs[s:s+l]) for intStrs in intStrs if int(intStrs[s:s+l]) > k]

# 수열과 구간 쿼리 3


def solution(arr, queries):
    for i in queries:
        arr[i[0]], arr[i[1]] = arr[i[1]], arr[i[0]]
    return arr


def solution(arr, queries):
    for a, b in queries:
        arr[a], arr[b] = arr[b], arr[a]
    return arr

# 문자열 묶기


def solution(strArr):
    answer = []
    d = []
    for i in strArr:
        d.append(len(i))
    # d= [len(i) for i in strARr]
    for x in set(d):
        answer.append(d.count(x))
    return max(answer)

# 세 개의 구분자


def solution(myStr):
    str = myStr.replace('b', 'a')
    str = str.replace('c', 'a')
    x = list(filter(None, str.split('a')))
    return x if x else ["EMPTY"]


def solution(myStr):
    str = myStr.replace('b', 'a')
    str = str.replace('c', 'a')
    str = str.split('a')
    answer = []
    for x in str:
        if x:
            answer.append(x)
    if not answer:
        return ["EMPTY"]
    return answer


# 2의 영역
def solution(arr):
    answer = []
    d = []
    for i, v in enumerate(arr):
        if v == 2:
            answer.append(i)
    if not answer:
        return [-1]
    else:
        for x in range(min(answer), max(answer)+1):
            d.append(arr[x])
        return d


def solution(arr):
    d = []
    if 2 not in arr:
        return [-1]
    else:
        for i in range(0, len(arr)):
            if arr[i] == 2:
                d.append(i)
    return arr[d[0]:d[-1]+1]

# 리스트 자르기


def solution(n, slicer, num_list):
    # a, b, c = slicer
    answer = []
    if n == 1:
        return num_list[:slicer[1]+1]
    elif n == 2:
        return num_list[slicer[0]:]
    elif n == 3:
        return num_list[slicer[0]:slicer[1]+1]
    # else:
    #   return num_list[slicer[0]:slicer[1]+1:slicer[2]]
    elif n == 4:
        for i in range(slicer[0], slicer[1]+1, slicer[2]):
            answer.append(num_list[i])
        return answer

# 간단한 논리연산


def solution(x1, x2, x3, x4):
    return (x1 | x2) & (x3 | x4)
    # return (x1 or x2) and (x3 or x4)

# 커피 심부름


def solution(order):
    d = [0] * 2
    # answer = 0
    for i in order:
        if 'latter' in i:
            d[1] += 1
            # answer += 5000
        else:
            d[0] += 1
            # answer += 4500
    return 4500*d[0] + 5000*d[1]
    # return answer

# 조건에 맞게 수열 변환하기 2


def solution(arr):
    answer = 0
    while 1:
        new = []
        for i in arr:
            if i >= 50 and i % 2 == 0:
                new.append(i//2)
            elif i < 50 and i % 2 == 1:
                new.append(i * 2 + 1)
            else:
                new.append(i)
        if arr == new:
            return answer
        else:
            answer += 1
            new = arr

# qr code


def solution(q, r, code):
    # answer = ''
    d = []
    for i, v in enumerate(code):
        if i % q == r:
            d.append(v)
            # answer += v
    return ''.join(d)
    # return answer


def solution(q, r, code):
    return code[r::q]


def solution(q, r, code):
    return ''.join(s for i, s in enumerate(code) if i % q == r)

# 수열과 구간 쿼리 4


def solution(arr, queries):
    for i in queries:
        for x in range(i[0], i[1]+1):
            if x % i[2] == 0:
                arr[x] = arr[x] + 1
    return arr


def solution(arr, queries):
    for s, e, k in queries:
        for i in range(s, e+1):
            if i % k == 0:
                arr[i] += 1
    return arr

# 배열 만들기 6


def solution(arr):
    answer = []
    for i in arr:
        if not answer:
            answer.append(i)
        elif answer[-1] == i:
            del answer[-1]
        elif answer[-1] != i:
            answer.append(i)
    if not answer:
        return [-1]
    return answer


def solution(arr):
    answer = []
    i = 0
    while i < len(arr):
        if not answer:
            answer.append(arr[i])
        elif answer[-1] == arr[i]:
            answer.pop()
        else:
            answer.append(arr[i])
        i += 1
    return answer if answer else [-1]

# 왼쪽 오른쪽


def solution(str_list):
    answer = []
    for i, v in enumerate(str_list):
        if v == 'l':
            answer = str_list[:i]
            break
        elif v == 'r':
            answer = str_list[i+1:]
            break
    return answer

# 문자 개수 새기


def solution(my_string):
    return [my_string.count(c) for c in 'abcdefghijklmnopqrstuvwxyz'.upper()+'abcdefghijklmnopqrstuvwxyz']

# 배열 만들기 4


def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if not stk:
            stk.append(arr[i])
            i += 1
        # else:
         #   if stk[-1] < arr[i]:
          #      stk.append(arr[i])
           #     i += 1
            # else:
            #   stk.pop()
        elif stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        elif stk[-1] >= arr[i]:
            stk.pop()
    return stk

# 문자열 여러 번 뒤집기


def solution(my_string, queries):
    for a, b in queries:
        str = list(my_string)
        str = str[a:b+1]
        str.reverse()
        my_string = my_string[:a] + ''.join(str) + my_string[b+1:]
    return my_string


def solution(my_string, queries):
    answer = list(my_string)
    for s, e in queries:
        answer[s:e+1] = answer[s:e+1][::-1]
    return ''.join(answer)

# 조건 문자열


def solution(ineq, eq, n, m):
    if ineq == "<":
        if eq == "=":
            return 1 if n <= m else 0
        elif eq == "!":
            return 1 if n < m else 0
    elif ineq == ">":
        if eq == "=":
            return 1 if n >= m else 0
        elif eq == "!":
            return 1 if n > m else 0

# 무작위로 k개의 수 뽑기


def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
        else:
            pass
    if len(answer) < k:
        for _ in range(k - len(answer)):
            answer.append(-1)
    else:
        answer = answer[:k]
    return answer


def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
        if len(answer) == k:
            break

    return answer + [-1] * (k - len(answer))

# 수열과 구간 쿼리 2


def solution(arr, queries):
    answer = []
    for a, b, c in queries:
        d = []
        for i in arr[a:b+1]:
            if i > c:
                d.append(i)
        answer.append(-1 if not d else min(d))
    return answer

"""

# 정사각형으로 만들기


def solution(arr):
    a = len(arr)
    b = len(arr[0])

    if a > b:
        for i in range(a):
            arr[i].extend([0] * (a-b))
            # for j in range(a-b):
            # arr[i].append(0)
    elif b > a:
        for _ in range(b-a):
            arr.append([0]*b)
    return arr


def solution(arr):  # 미리 배열 만들기
    answer = []
    x = len(arr)
    y = len(arr[0])
    m = max(x, y)

    answer = [[0]*m for i in range(m)]

    for i in range(x):
        for j in range(y):
            answer[i][j] = arr[i][j]

    return answer

# 그림 확대


def solution(picture, k):
    answer = []
    for row in picture:  # 이미지 한줄 가져오기
        a = ''
        for pixel in row:
            a += pixel * k  # 한 픽셀을 k배 만큼 가로로 늘리기

        for _ in range(k):
            answer.append(a)  # 가로로 늘려진 한 줄을 k배 만큼 세로로 늘리기
    return answer


def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        answer += [picture[i].replace('.', '.'*k).replace('x', 'x'*k)] * k
    return answer

# 문자열 겹쳐쓰기


def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]


def solution(my_string, overwrite_string, s):
    str = list(my_string)
    str[s:s+len(overwrite_string)] = overwrite_string
    return ''.join(str)

# 전국 대회 선발 고사


def solution(rank, attendance):
    d = []
    for i, v in enumerate(rank):
        if attendance[i] == True:
            d.append([v, i])
    d.sort()

    a = d[0][1]
    b = d[1][1]
    c = d[2][1]
    return 10000 * a + 100 * b + c


# 대소문자 바꿔서 출력하기
str = input()
for i in str:
    if i.isupper() == True:
        print(i.lower(), end="")
    else:
        print(i.upper(), end="")

# 배열 만들기 2


def solution(l, r):
    answer = []
    for i in range(l, r+1):
        check = True
        for s in str(i):
            if s != '5' and s != '0':
                check = False
                break
        if check == True:
            answer.append(i)

    if not answer:
        return [-1]
    return answer

# 코드 처리하기


def solution(code):
    a = ''
    mode = 0
    for i in range(len(code)):
        if mode == 0:
            if code[i] != '1' and i % 2 == 0:
                a += code[i]
            elif code[i] == '1':
                mode = 1
        else:
            if code[i] != '1' and i % 2 == 1:
                a += code[i]
            elif code[i] == '1':
                mode = 0
    if a == '':
        return 'EMPTY'
    return a

# 배열 조각하기


def solution(arr, query):
    for i in range(len(query)):
        if i % 2 == 0:
            arr = arr[:query[i]+1]
        else:
            arr = arr[query[i]:]
    return arr

# 주사위 게임 3


def solution(a, b, c, d):
    arr = [a, b, c, d]
    cnt = [arr.count(item) for item in arr]

    if max(cnt) == 4:
        return a*1111

    elif max(cnt) == 3:
        return (10 * (arr[cnt.index(3)]) + (arr[cnt.index(1)]))**2

    elif max(cnt) == 2:
        if 1 in cnt:
            return arr[cnt.index(1)] * arr[cnt.index(1, cnt.index(1)+1, 4)]
        else:
            for item in arr:
                if a != item:
                    return (a+item) * abs(a-item)

    else:
        return min(arr)

# 정수를 나선형으로 배치하기


def solution(n):
    if n == 1:
        return [[1]]

    arr = [[0]*n for _ in range(n)]
    x = 0
    y = 0
    dir = 'r'
    for i in range(n*n):
        arr[x][y] = i + 1
        if dir == 'r':
            y += 1
            if y == n-1 or arr[x][y+1] != 0:
                dir = 'd'
        elif dir == 'd':
            x += 1
            if x == n-1 or arr[x+1][y] != 0:
                dir = 'l'
        elif dir == 'l':
            y -= 1
            if y == 0 or arr[x][y-1] != 0:
                dir = 'u'
        elif dir == 'u':
            x -= 1
            if x == n-1 or arr[x-1][y] != 0:
                dir = 'r'
    return arr


# 문자열 정렬하기 1
def solution(my_string):
    answer = []
    for i in my_string:
        if i.isdigit():
            answer.append(int(i))
    answer.sort()
    return answer


def solution(my_string):
    return sorted([int(i) for i in my_string if i.isdigit()])


# 암호 해독
def solution(cipher, code):
    answer = ''
    for i in range(code-1, len(cipher), code):
        answer += cipher[i]
    return answer


def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer


def solution(cipher, code):
    return [cipher[code-1::code]]

# 주사위의 개수


def solution(box, n):
    a = 0
    b = 1
    for i in box:
        a = i // n
        b *= a
    return b


def solution(box, n):
    x, y, z = box
    return (x//n) * (y // n) * (z // n)

# 문자열 정렬하기(2)


def solution(my_string):
    str = sorted(my_string.lower())
    return ''.join(str)

# 피자 나눠 먹기(2)


def solution(n):
    i = 1
    while (6 * i) % n != 0:
        i += 1
    return i
