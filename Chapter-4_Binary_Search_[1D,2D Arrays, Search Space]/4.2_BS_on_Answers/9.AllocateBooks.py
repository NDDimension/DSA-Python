"""
"Allocate Books"

=> Given a collection of books and number of students we need to distribute the books to them;

Constraints :

    1. Each student gets atleast one book.
    2. Each book should be allocated to only one student.
    3. Book allocation must be done in contiguous manner.

Distribution must be in the way where "max no. of pages assigned to a student is min"  else -1.
"""


def assignment(books, pages):
    student = 1
    pages_student = 0

    for book in range(len(books)):
        if pages_student + books[book] <= pages:
            pages_student += books[book]

        else:
            student += 1
            pages_student = books[book]

    return student


# Naive Approach
# TC : O((sum - max + 1) x N)
# SC : O(1)


def AllocateBooks(books, students):
    l = max(books)
    h = sum(books)

    for pages in range(l, h + 1):
        countStudents = assignment(books, pages)
        if countStudents == students:
            return pages
    return -1


books = [25, 46, 28, 49, 24]
students = 4
print(AllocateBooks(books, students))

# Binary Search
# TC : O(log(sum - max + 1) x N)
# SC : O(1)


def AllocateBooks_BS(books, students):
    low = max(books)
    high = sum(books)

    while low <= high:
        mid = (low + high) // 2

        if assignment(books, mid) > students:
            low = mid + 1
        else:
            high = mid - 1
    return low


print(AllocateBooks_BS(books, students))
