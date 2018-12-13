import itertools


def choose_best_sum(t, k, ls):
    if len(ls) < k:
        return None
    if k == 1:
        arr = list(filter((lambda v: v <= t), ls))
        if len(arr):
            return max(arr)
        else:
            return None
    else:
        best_sum = 0
        lenth = len(ls)
        for a in range(lenth):
            va = ls[a]
            if va < t:
                temp_sum = choose_best_sum(t-va, k-1, ls[a+1:lenth])
                if(temp_sum != None and va+temp_sum <= t and va+temp_sum > best_sum):
                    best_sum = va+temp_sum
        return None if best_sum == 0 else best_sum
    # your code


def choose_best_sum_t(t, k, ls):
    try:
        return max(sum(i) for i in itertools.combinations(ls, k) if sum(i) <= t)
    except:
        return None


print choose_best_sum(120, 2, [55, 59, 62])
