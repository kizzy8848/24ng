def main():
    data = [3, 3, 3, 4, 4, 1, 8]
    nums = [1, 2, 2, 3, 3, 3, 8]
    hmap = {}
    for num in data:
        if num in hmap:
            hmap[num] += num
        else:
            hmap[num] = num
    print(hmap)
    prev_num = 0
    sum = [0, 0, 0]
    for num in sorted(hmap.keys()):
        if num - 1 == prev_num:
            sum[2] = max(sum[1], sum[0] + hmap[num])
        else:
            sum[2] = sum[1] + hmap[num]
        sum[0] = sum[1]
        sum[1] = sum[2]
        prev_num = num

    print(sum)

if __name__ == "__main__":
    main()
