class Solution:
    def studentGrade(self, marks):
        self.marks = marks

        if 0 <= marks <= 100:
            if marks >= 90:
                print("Grade A")

            elif 70 <= marks <= 90:
                print("Grade B")

            elif 50 <= marks <= 70:
                print("Grade C")

            elif 35 <= marks <= 50:
                print("Grade D")

            else:
                print("Fail")

        else:
            print("Error")


marks = int(input("Enter marks 0 to 100"))
grade = Solution()
grade.studentGrade(marks)
