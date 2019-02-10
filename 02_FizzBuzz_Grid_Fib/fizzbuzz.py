"""
Header: UW 2017 - Intro To Python
Topic: FizzBuzz
Author: PydPiper

Objective: From the count of 0 to 100 print Fizz on numbers divisible of 3, Buzz on 5, and FizzBuzz on numbers divisible
            by both 3 and 5.
"""


def fizzbuzz(start_no: int = 0, stop_no: int = 100) -> None:
    current_value = start_no
    buffer = ""
    while current_value <= stop_no:
        if current_value % 3 == 0 and current_value % 5 == 0:
            if current_value == 0:
                # for 0 / # = 0 catch
                pass
            else:
                buffer += 'FizzBuzz:{cv}\n'.format(cv=current_value)
        elif current_value % 3 == 0 or current_value % 5 == 0:
            if current_value % 3 == 0:
                buffer += ('Fizz    :{cv}\n'.format(cv=current_value))
            if current_value % 5 == 0:
                buffer += 'Buzz    :{cv}\n'.format(cv=current_value)
        current_value += 1
    return buffer


if __name__ == "__main__":
    print(fizzbuzz(start_no=0, stop_no=100))

