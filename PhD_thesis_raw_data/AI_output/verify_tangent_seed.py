"""Reproduce the finite-field certificate in tangent_counterexample_revised.tex.

Run with Python 3; only the standard library is needed. Coefficients in all
polynomial lists are in increasing degree order. This checks the arithmetic,
not the cited geometric existence and tangentiality results.
"""
from fractions import Fraction as F
from itertools import permutations


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    c = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] += x
    return trim(c)


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return trim(c)


def rem(a, b, p):
    a = trim([x % p for x in a])
    b = trim([x % p for x in b])
    while a != [0] and len(a) >= len(b):
        k = len(a) - len(b)
        c = a[-1] * pow(b[-1], -1, p) % p
        for i, x in enumerate(b):
            a[i + k] = (a[i + k] - c * x) % p
        a = trim(a)
    return a


def gcd(a, b, p):
    while b != [0]:
        a, b = b, rem(a, b, p)
    return [(x * pow(a[-1], -1, p)) % p for x in a]


def powmod(a, n, f, p):
    r = [1]
    while n:
        if n & 1:
            r = rem(mul(r, a), f, p)
        a = rem(mul(a, a), f, p)
        n >>= 1
    return r


def prime_divisors(n):
    return [r for r in range(2, n + 1)
            if n % r == 0 and all(r % k for k in range(2, r))]


def irreducible(f, p):
    n = len(f) - 1
    x = [0, 1]
    for r in prime_divisors(n):
        if gcd(f, add(powmod(x, p ** (n // r), f, p), [0, -1]), p) != [1]:
            return False
    return rem(add(powmod(x, p ** n, f, p), [0, -1]), f, p) == [0]


def count_points(branch, modulus, p=11):
    r = len(modulus) - 1
    q = p ** r
    digits = [tuple((a // (p ** i)) % p for i in range(r)) for a in range(q)]

    def product(a, b):
        c = [0] * (2 * r - 1)
        for i, ai in enumerate(digits[a]):
            for j, bj in enumerate(digits[b]):
                c[i + j] += ai * bj
        for k in range(2 * r - 2, r - 1, -1):
            ck = c[k] % p
            for j in range(r):
                c[k - r + j] -= ck * modulus[j]
        return sum((c[i] % p) * p ** i for i in range(r))

    squares = {product(a, a) for a in range(1, q)}
    assert len(squares) == (q - 1) // 2
    character_sum = 0
    for x in range(q):
        y = 0
        for c in reversed(branch):
            y = product(y, x)
            y = y - y % p + (y % p + c) % p
        character_sum += 0 if y == 0 else (1 if y in squares else -1)
    return q + 1 + character_sum, character_sum


def main():
    # Norm of B^2 + 10*e*B - 35*e^2 - 28 in Q[e]/(e^3-e-1/4).
    matrix = [
        [[-28, 0, 1], [-F(35, 4)], [0, F(5, 2)]],
        [[0, 10], [-63, 0, 1], [-F(35, 4), 10]],
        [[-35], [0, 10], [-63, 0, 1]],
    ]
    norm = [0]
    for permutation in permutations(range(3)):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(3) for j in range(i + 1, 3))
        term = [(-1) ** inversions]
        for i, j in enumerate(permutation):
            term = mul(term, matrix[i][j])
        norm = add(norm, term)
    lame = mul([560, -208, 0, 1], norm)
    integral = [F(16 * c) for c in lame]
    assert all(c.denominator == 1 for c in integral)
    print('16 L_4, coefficients in increasing degree:', [int(c) for c in integral])
    branch = [int(F(c).numerator * pow(F(c).denominator, -1, 11)) % 11 for c in lame]
    expected_branch = [5, 7, 9, 6, 1, 0, 0, 0, 0, 1]
    assert branch == expected_branch
    print('L_4 mod 11:', branch)
    factors = [[2, 1], [5, 9, 1], [1, 6, 5, 1], [6, 7, 6, 1]]
    factored = [1]
    for factor in factors:
        assert irreducible(factor, 11)
        factored = [c % 11 for c in mul(factored, factor)]
    assert factored == branch
    derivative = [i * branch[i] % 11 for i in range(1, len(branch))]
    assert gcd(branch, derivative, 11) == [1]
    print('Branch factorization and squarefreeness: PASS')

    moduli = [[0, 1], [1, 0, 1], [1, 0, 4, 1], [1, 0, 0, 4, 1]]
    counts = []
    for modulus in moduli:
        assert irreducible(modulus, 11)
        count, character_sum = count_points(branch, modulus)
        counts.append(count)
        print(f'r={len(modulus)-1}: N_r={count}, character sum={character_sum}')
    assert counts == [10, 120, 1312, 15312]

    # Newton identities and the weight-one functional equation in genus four.
    power_sums = [0] + [11 ** r + 1 - counts[r - 1] for r in range(1, 5)]
    leading = [F(1)]
    for k in range(1, 5):
        leading.append(-sum(leading[k - i] * power_sums[i] for i in range(1, k + 1)) / k)
    descending = leading + [11 ** (4 - i) * leading[i] for i in range(3, -1, -1)]
    assert all(c.denominator == 1 for c in descending)
    jacobian = [int(c) for c in reversed(descending)]
    elliptic_count = 1 + sum(1 if (v := (4*x*x*x - 4*x - 1) % 11) == 0
                             else 2 if pow(v, 5, 11) == 1 else 0 for x in range(11))
    assert elliptic_count == 7
    elliptic = [11, -5, 1]
    quotient = [1331, 363, 55, -14, 5, 3, 1]
    assert mul(elliptic, quotient) == jacobian
    print('#E_0(F_11) =', elliptic_count)
    print('Jacobian Frobenius polynomial, descending coefficients:', list(reversed(jacobian)))
    print('Quotient Frobenius polynomial, descending coefficients:', list(reversed(quotient)))
    assert irreducible(quotient, 3)
    assert quotient[3] % 11 != 0
    assert quotient[5] != 0
    print('Quotient: irreducible mod 3; ordinary; not of the exceptional form T^6+cT^3+11^3.')
    print('All arithmetic checks passed.')


if __name__ == '__main__':
    main()
