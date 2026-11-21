grade_num = []
num_sum = []

for i in range(20):
    name, num, grade  = input().split()
    num = float(num)
    if grade != "P":
        num_sum.append(num)

        if grade == 'A+':
            grade_num.append(4.5*num)
        elif grade == 'A0':
            grade_num.append(4.0*num)
        elif grade == 'B+':
            grade_num.append(3.5*num)
        elif grade == 'B0':
            grade_num.append(3.0*num)
        elif grade == 'C+':
            grade_num.append(2.5*num)
        elif grade == 'C0':
            grade_num.append(2.0*num)
        elif grade == 'D+':
            grade_num.append(1.5*num)
        elif grade == 'D0':
            grade_num.append(1.0*num)
        elif grade == 'F':
            grade_num.append(0.0)
    else:
        continue

mean_num = sum(grade_num)/sum(num_sum)
print(f'{mean_num: .6f}')


