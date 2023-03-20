import sys
input = sys.stdin.readline

N, K = map(int, input().split())
numbers = [int(input()) for _ in range(N)]
numbers.sort()

dp = [0]*(K+1)
dp[0] = 1

for n in range(N):
    for k in range(numbers[n], K+1):
        dp[k] += dp[k-numbers[n]]

print(dp[K])
'''
dp[1] -> 1원 짜리만 쓰는 경우: 1
dp[2] -> 1) 1원만 쓰는 경우: 1+1
         2) 1원과 2원을 같이 쓰되 2원을 적어도 한번 이상 쓰는 경우: 2
dp[3] -> 1) 1원만 쓰는 경우: 1+1+1
         2) 1원과 2원을 같이 쓰되 2원을 적어도 한번 이상 쓰는 경우: 1+2 
dp[4] -> 1) 1원만 쓰는 경우: 1+1+1+1
         2) 1원과 2원을 같이 쓰되 2원을 적어도 한번 이상 쓰는 경우: 1+2+1
                                                             2+2
dp[5] -> 1) 1원만 쓰는 경우: 1+1+1+1+1
         2) 1원과 2원을 같이 쓰되 2원을 적어도 한번 이상 쓰는 경우: 1+2+2, 1+1+1+2
         3) 1원과 2원, 5원을 같이 쓰되 5원을 적어도 한번 이상 쓰는 경우: 5

dp[6] -> 1) 1원만 쓰는 경우: 1+1+1+1+1+1
         2) 1원과 2원을 같이 쓰되 2원을 적어도 한번 이상 쓰는 경우: 2+2+2, 1+1+2+2, 1+1+1+1+2 
         3) 1원과 2원, 5원을 같이 쓰되 5원을 적어도 한번 이상 쓰는 경우: 5+1
         
dp[7] -> 1) 1원만 쓰는 경우: 1+1+1+1+1+1+1
         2) 1원과 2원을 같이 쓰되 2원을 적어도 한번 이상 쓰는 경우: 2+2+2+1, 1+1+2+2+1, 1+1+1+1+2+1
         3) 1원과 2원, 5원을 같이 쓰되 5원을 적어도 한번 이상 쓰는 경우: 5+1+1, 5+2

dp[8] -> 1) 1원만 쓰는 경우: 1+1+1+1+1+1+1+1
         2) 1원과 2원을 같이 쓰되 2원을 적어도 한번 이상 쓰는 경우: 2+2+2+1, 1+1+2+2+1, 1+1+1+1+2+1, 2+2+2+2
         3) 1원과 2원, 5원을 같이 쓰되 5원을 적어도 한번 이상 쓰는 경우: 5+1+1+1, 5+2+1
         
여기서 중요한 건, dp[1], dp[2], dp[3]... 순서로 업데이트하는 게 아니라
쓸 수 있는 동전 크기 오름차순으로 업데이트를 해야한다는 점이다.

이미 dp[8]은 동전 1원으로 쓸 수 있는 가짓수로 업데이트되었다고 가정해보자.
그리고 여기에 동전 2원을 적어도 하나 이상 사용하여 8을 만드는 방법 가짓수를 더해주면 된다.
6 + 2 = 8이므로, 기존 dp[8](1원짜리 동전만으로 만드는 방법 수)에 dp[6] 값을 그대로 더해주면 된다. 이게 어떻게 가능한가?
이미 dp[6]은 1원 짜리 동전을 적어도 하나 이상 사용하여 만드는 방법(1+1+1+1+1+1)과 
2원짜리 동전을 적어도 하나 이상 사용하여 만드는 방법의 가짓수의 합으로 업데이트되었다고 가정된 것이다.
6 + 2 = 8 -> 이미 만들어진 6에 동전 2를 반드시 하나는 사용해서 8을 만든다는 뜻.
따라서 동전 2원을 적어도 하나 이상 쓴다는 보장이 되어있으므로 dp[8](1+1+1+1+1+1+1+1)과 중복이 일어나지 않는다.

dp 배열의 업데이트 순서는
1) 0번째 동전만으로 0부터 K까지 모든 가치를 다 만들어서 dp 배열 값 업데이트
2) 0번째 동전과 1번째 동전을 쓰되 1번째 동전은 적어도 하나 이상 사용하여 
   0부터 K까지 모든 가치를 다 만들어본 후, 기존 dp배열 값을 이용하여 dp 배열 값 업데이트
3) 0번째, 1번째, 2번째 동전을 쓰되 2번째 동전은 적어도 하나 이상 사용하여 
   0부터 K까지 모든 가치를 다 만들어본 후, 기존 dp배열 값을 이용하여 dp 배열 값 업데이트
4) ... 0번째, 1번째, ... N-1번째 동전을 쓰되 N-1번째 동전은 적어도 하나 이상 사용하여 
   0부터 K까지 모든 가치를 다 만들어본 후, 기존 dp배열 값을 이용하여 dp 배열 값 업데이트
   
따라서 2차원 배열이 필요없다.
'''

