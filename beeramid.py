def beeramid(cash, cost):
    """
    определяет уровень пирамиды n^2, который можно достичь
    колличеством банок пива, купленных по цене cost
    за деньги cash
    """
    count = cash // cost
    total = 0
    n = 1
    while True:
        total += n ** 2
        if total >= count:
            return n - 1
        n += 1

res = beeramid(cash=1500, cost = 2)
print(res)


