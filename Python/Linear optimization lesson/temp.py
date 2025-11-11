def print_table(table):
    # برای هر سطر در جدول
    for row in table:
        print(' '.join([f'{val:.2f}' for val in row]))


def simplex(c, A, b):
    # تعداد متغیرها و محدودیت‌ها
    n_constraints = len(A)

    # ایجاد جدول ساده‌سازی
    table = [row + [0] + [b[i]] for i, row in enumerate(A)]
    table.append([i for i in c] + [0, 0])

    # حل مسئله با استفاده از روش ساده‌سازی
    while any(value > 0 for value in table[-1][:-2]):
        pivot_column = table[-1].index(max(table[-1][:-2]))
        pivot_row_list = [table[i][-1] / table[i][pivot_column] if table[i]
                          [pivot_column] > 0 else float('inf') for i in range(n_constraints)]
        pivot_row = pivot_row_list.index(min(pivot_row_list))
        pivot_element = table[pivot_row][pivot_column]

        # تقسیم سطر محور بر عنصر محور
        table[pivot_row] = [
            element / pivot_element for element in table[pivot_row]]

        # به‌روزرسانی سطرهای دیگر
        for i in range(len(table)):
            if i != pivot_row:
                multiplier = table[i][pivot_column]
                table[i] = [i - j * multiplier for i,
                            j in zip(table[i], table[pivot_row])]

    # برگرداندن راه‌حل بهینه
    return [table[i][-1] if table[i][pivot_column] == 1 else 0 for i in range(n_constraints)] + [table[-1][-1]]


# تعریف ضرایب تابع هدف
c = [1, -2, 1]

# تعریف ضرایب محدودیت‌های نامساوی
A = [[1, 2, 1], [2, 1, -1], [-1, 3, 0]]

# تعریف سمت راست محدودیت‌های نامساوی
b = [12, 6, 9]

# حل مسئله برنامه‌ریزی خطی با استفاده از روش ساده‌سازی
solution = simplex(c, A, b)

# چاپ راه‌حل بهینه
print('\nOptimal solution:', solution[:-1])
print('Value of the objective function at the optimal point:',
      solution[-1], '\n')
