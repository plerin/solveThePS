'''

'''
import math

n = int(input())

dp = [i for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, int(math.sqrt(i))+1):
        # if j*j > i: # 제곱근까지 알아본다는 제한이 없으면 시간 복잡도는 10만*10만으로 시간초과가 나옴
        #     continue
        # j*j가 i보다 작거나 같다는 말은 dp[i]를 구성할 때 j**2을 사용해도 된다는 말
        dp[i] = min(dp[i], dp[i - j*j] + 1)
        # if dp[i] > dp[i - j*j] + 1:
        #     dp[i] = dp[i-j*j] + 1


print(dp[n])
