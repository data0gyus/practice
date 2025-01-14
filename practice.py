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

"""

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
