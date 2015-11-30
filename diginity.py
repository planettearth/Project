"""Diginity Problem"""
def summary_number(num):
    """Print diginity of num"""
    list_num = []
    if num != '0':
        if len(num) > 1:
            for i in num:
                list_num.append(int(i))
            summary_number(str(sum(list_num)))
        else:
            print(num)
            summary_number(input())
    else:
        return
summary_number(input())
