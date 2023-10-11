import sys
input = sys.stdin.readline

def mod_pow(base, exponent, mod):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exponent //= 2
    return result

def mod_inverse(n, mod):
    return mod_pow(n, mod - 2, mod)

def nCr_mod_p(n, r, mod):
    if r == 0:
        return 1

    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = (fact[i - 1] * i) % mod

    numerator = fact[n]
    denominator = (fact[r] * fact[n - r]) % mod

    denominator_inverse = mod_inverse(denominator, mod)

    return (numerator * denominator_inverse) % mod

MOD = 1234567891

T = int(input())
for t in range(1, T + 1):
    N, R = map(int, input().split())
    result = nCr_mod_p(N, R, MOD)
    print("#{} {}".format(t, result))