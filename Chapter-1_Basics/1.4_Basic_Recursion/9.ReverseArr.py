class Reverse_Array:
    def rev(self, array, left, right):
        if left >= right:
            return
        array[left], array[right] = array[right], array[left]
        self.rev(array, left + 1, right - 1)

    def rev_array(self, i):
        if i >= n // 2:
            return

        array[i], array[n - i - 1] = array[n - i - 1], array[i]
        self.rev_array(i + 1)


n = int(input("Enter length of array: "))
array = list(map(int, input(f"Enter {n} elements separated by space : ").split()))

Paras2 = Reverse_Array()
Paras1 = Reverse_Array()

if len(array) != n:
    print("Error: Number of elements entered does not match the specified length.")
else:
    print(f"Original Array => {array}")
    Paras2.rev(array, 0, len(array) - 1)
    print(f"Reversed Array => {array}")


if len(array) != n:
    print("Error: Number of elements entered does not match the specified length.")
else:
    print(f"Original Array => {array}")
    Paras1.rev_array(0)
    print(f"Reversed Array => {array}")


# def rev_array(i):
#     if i >= n // 2:
#         return
#     array[i], array[n - i - 1] = array[n - i - 1], array[i]
#     rev_array(i + 1)

# n = int(input("Enter length of array: "))
# array = list(map(int, input(f"Enter {n} elements separated by space: ").split()))

# if len(array) != n:
#     print("Error: Number of elements entered does not match the specified length.")
# else:
#     print(f"Original Array => {array}")
#     rev_array(0)
#     print(f"Reversed Array => {array}")
