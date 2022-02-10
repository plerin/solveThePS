
def aiOven(time, dur):
    step = [3600, 60, 1]
    ret = [0 for _ in range(3)]
    carry = 0

    for i in range(len(time)):
        dur, ret[i] = divmod(dur, step[i])

    for i in range(len(ret)-1, -1, -1):
        if i == 0:
            ret[i] = (ret[i]+time[i]+carry) % 24
        else:
            carry, ret[i] = divmod(ret[i]+time[i]+carry, 60)

    return ret


h, m, s = map(int, input().split())
dur = int(input())

an = aiOven([h, m, s], dur)
print(f'{an[0]} {an[1]} {an[2]}')
