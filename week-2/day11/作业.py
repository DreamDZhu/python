# 写函数，传入一个参数n,返回n的阶乘
def my_cal(num):
    count = 1
    # for i in range(num):
    #     count *= i+1
    # return count
    for i in range(num, 0, -1):
        count *= i
    return count


print(my_cal(7))

# 写函数，返回一个扑克牌列表，里面有52项，每一项是一个元祖

card_color = ["红心", "草花", "方块", "黑桃"]
card_num = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

card_lst = []

for color in card_color:
    for num in card_num:
        card_lst.append((color, num))

print(card_lst)
