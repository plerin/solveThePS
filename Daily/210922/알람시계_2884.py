def alarm(H, M):
    s, m = divmod(M-45, 60) if M >= 45 else divmod(60+(60-(45-M)), 60)
    h = H-s if H-s >= 0 else 23

    return (h, m)


# 입력 받기
H, M = map(int, input().split())

# alarm 호출
ret = alarm(H, M)

# 결과 리턴
print(f'{ret[0]} {ret[1]}')
