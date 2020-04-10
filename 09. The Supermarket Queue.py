# The Supermarket Queue
# https://www.codewars.com/kata/57b06f90e298a7b53d000a86
# 6 kyu


def queue_time(customers, n):
    tills_list = []

    if len(customers) == 0:  # catch edge case with 0 customers
        return 0
    if n == 1:  # catch case if just a single till is available
        return sum(customers)
    if n >= len(customers):  # catch case if there are more tills than customers
        return max(customers)

    for i in range(n):  # put a customer on each till
        tills_list.append(customers[0])
        del customers[0]

    for each in customers:  # put next customer on the till with shortest wait time
        tills_list[tills_list.index(min(tills_list))] += each

    return max(tills_list)


my_list = [4, 3, 10]
empty_list = []
print(queue_time(my_list, 2))
print(queue_time(empty_list, 1))
