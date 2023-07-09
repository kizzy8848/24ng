
def main(list_a:list[int], list_b:list[int]):
    if list_a.count(0) == 0 and list_b.count(0) == 0 and sum(list_a) != sum[list_b]:
        return -1
    if list_a.count(0) == 0 and sum(list_a) + list_a.count(0) < sum(list_b) + list_b.count(0):
        return -1
    if list_b.count(0) == 0 and sum(list_a) + list_a.count(0) > sum(list_b) + list_b.count(0):
        return -1
    return max(sum(list_a) + list_a.count(0), sum(list_b) + list_b.count(0))


if __name__ == "__main__":
    list_a = [2, 5, 0, 1, 1]
    list_b = [2, 1, 0, 0]
    list_c = [0, 0, 0]
    list_d = [1, 1]
    print(main(list_b, list_a))
    print(main(list_c, list_d))