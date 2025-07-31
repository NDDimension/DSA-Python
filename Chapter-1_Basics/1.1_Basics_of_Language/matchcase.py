class Solution:
    def whichWeekDay(self, day):
        self.day = day

        match day:
            case 1:
                print("Monday")

            case 2:
                print("Tuesday")

            case 3:
                print("Wednesday")

            case 4:
                print("Thursday")

            case 5:
                print("Friday")

            case 6:
                print("Saturday")

            case 7:
                print("Sunday")

            case _:
                print("INVALID")


day = int(input("Enter a day (1-7): "))
object = Solution()
object.whichWeekDay(day)
