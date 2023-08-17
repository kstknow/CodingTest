# 백준 2775번 부녀회장이 될테야

# 거주 조건이 a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다는 조건이 있음
# 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇명이 살고 있는지 출력하라. 단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다


'''
문제 풀이
임의의 층과 호수를 입력 받으면 해당 호실에 사는 사라마의 수를 입력하는 문제
해당 호실 사람의 수는 한층 아래 1호부터 같은 호수까지의 수를 합해서 구할수 있다

문제를 풀때, 호수별로 사람 수가 증가하는데에 동일한 규칙성이 없기 때문에 0층부터 입력 받는 층수까지 한층 한층 사람 수를 더해가는 방식

for _ in range(t):
    floor = int(input()) # 층
    num = int(input()) # 호
    f0 = [x for x in range(1, num+1)] # 0층 리스트

입력 받은 테스트케이스 수만큼 for문을 반복하도록 코드를 작성하고서 for문 안에서 층과 호에 해당하는 두수를 입력 받으면 각각 floor, num 변수에 선언하였다.
층과 호수를 입력 받은 후 0충의 1호부터 입력 받은 호수까지 거주자 수 리스트를 생성한다. 
range 함수를 이용해서 1부터 입력 받은 숫자까지의 범위에 해당하는 숫자 리스트를 생성한다.

for k in range(floor): # 층 수 만큼 반복
    for i in range(1, num): # 1 ~ n-1까지(인덱스로 사용)
        f0[i] += f0[i-1] # 층별 각 호실의 사람 수를 변경
print(f0[-1]) #가장 마지막 수 출력

테스트 케이스 수만큼 반복하는 for문 안에서 하위에 두개의 for문을 작성한다. 
첫번째 for문은 입력 받는 층수만큼 반복하고 두번째 for문은 각 층의 1호부터 입력받는 호수까지 숫자를 반복해서 위에서 생성한 f0 리스트의 인덱스로 사용

두번째 for문의 숫자 인덱스를 이용해서 이전 인덱스의 숫자를 더한 값을 리셋한다. 즉, 층 수가 증가할때마다 한층 아래층의 이전 호실에 사는 사람의 숫자를 더하는것과 같은 의미가된다.
위 두개의 반복문이 종료됐을때, 가장 마지막 수를 호출하면 입력받은 층, 호수에 해당하는 사람 수를 출력할수 있다.
'''

#%%
# t = int(input())
t = 1

for _ in range(t):
    # floor = int(input())
    # num = int(input())
    floor = 1
    num = 3
    f0 = [x for x in range(1, num+1)]
    for k in range(floor):
        for i in range(1, num): # 여기서 num+1이 아니고 
            f0[i] += f0[i-1]
    print(f0[-1])
            
# %%
