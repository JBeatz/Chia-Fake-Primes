def odd_primes_below_n(n):
    """ Returns a list of odd primes less than n. """
    sieve = [True] * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2 * i + 1 for i in range(1, n//2) if sieve[i]]


POTENTIAL_WITNESSES = odd_primes_below_n(500)


def run_test_for_potential_nonprime_witness(a, d, n, r):
    if a % n == 0:
        return False
    x = pow(a, d, n)
    if x in (1, n-1):
        return False
    for _ in range(r - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return False
    return True


def miller_rabin_test(n, count=2):
    # see https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Computational_complexity
    if n == 2:
        return True

    if n & 1 == 0:
        return False

    r = 0
    d = n - 1
    while d & 1 == 0:
        r += 1
        d >>= 1

    assert d & 1 == 1
    assert (2 ** r) * d + 1 == n

    for _, a in zip(range(count), POTENTIAL_WITNESSES):
        if run_test_for_potential_nonprime_witness(a, d, n, r):
            return False
    return True

is_strong_prp = None

#1024 bit n
p1 = 17316868081892944814245898804781344373625169673277941408549866301660022650691
p2 = 51950604245678834442737696414344033120875509019833824225649598904980067952071
p3 = 190485548900822392956704886852594788109876866406057355494048529318260249157591
p4 = 571456646702467178870114660557784364329630599218172066482145587954780747472771

n = p1*p2*p3*p4
print n
print "is n prime?", miller_rabin_test(n)
