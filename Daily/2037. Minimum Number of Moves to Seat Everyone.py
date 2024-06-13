def minMovesToSeat(seats, students):
    seats_ = sorted(seats)
    students_ = sorted(students)
    m = len(seats)
    count_ = 0
    for i in range(m):
        count_ += abs(seats_[i] - students_[i])
    return count_


seats = [3, 1, 5]
students = [2, 7, 4]
print(minMovesToSeat(seats, students))  # Output: 4

seats = [4, 1, 5, 9]
students = [1, 3, 2, 6]
print(minMovesToSeat(seats, students))  # Output: 7

seats = [2, 2, 6, 6]
students = [1, 3, 2, 6]
print(minMovesToSeat(seats, students))  # Output: 4
