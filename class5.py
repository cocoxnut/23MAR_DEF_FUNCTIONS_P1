from random import choice as ch
suffix = '0444'
nums = [1, 4, 5, 7, 9, 0]
nums2 = "".join(map(str,nums))

def shuffle():
    mob_num = ['0444']
    for i in range(7):
        q = ch(nums)
        mob_num.append(q)
    print("".join(map(str,mob_num)))

shuffle()
