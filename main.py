


def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def print_sum(x, y):
    print("print_sum関数実行")
    sum = x+y
    print(sum)
    return sum


def print_loop_count_sum(loop_num):
    print("print_loop_count_sum関数実行m")
    sum = 0
    array = []
    for num in range(loop_num):
        sum += num
        array.append(num)
        print(num)
    print(sum)

def print_loop_count_sum_add(x, y, loop_num):
    print("print_loop_count_sum_add関数実行m")
    sum = print_sum(x, y)
    array = []
    for num in range(loop_num):
        sum += num
        array.append(num)
        print(num)
    print(sum)

print_sum(2, 3)
print_loop_count_sum(10)
print_loop_count_sum_add(2,3, 10)