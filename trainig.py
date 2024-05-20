# ____________________________________ Add Two Numbers
# def sum_lists(l1, l2):
#     sum = []
#     flag = 0
#
#     if len(l1) >= len(l2):
#         long_list = l1
#         short_list = l2
#     else:
#         long_list = l2
#         short_list = l1
#
#     for i in range(-1, -len(long_list) - 1, -1):
#
#         try:
#             elem = long_list[i] + short_list[i]
#         except IndexError:
#             elem = long_list[i]
#         if flag == 1:
#             elem += 1
#         if elem > 9:
#             elem -= 10
#             flag = 1
#         else:
#             flag = 0
#         sum.insert(0, elem)
#
#     if flag == 1:
#         sum.insert(0, 1)
#     sum.reverse()
#     return sum


# l1 = [9, 9, 9, 9, 9, 9, 9]
# l2 = [9, 9, 9, 9]
#
# print(sum_lists(l1, l2))
# _______________________________________ Zigzag Conversion
# s = "PAYPALISHIRING"
# new_list = []
#
# i = 0
# while True:
#     try:
#         new_list.append(s[i])
#         i += 4
#     except:
#         break
# i = 1
# while True:
#     try:
#         new_list.append(s[i])
#         i += 2
#     except:
#         break
# i = 2
# while True:
#     try:
#         new_list.append(s[i])
#         i += 4
#     except:
#         break
#
# delim = ""
# new_string = delim.join(new_list)
# print(new_string)
# ____________________________________________
