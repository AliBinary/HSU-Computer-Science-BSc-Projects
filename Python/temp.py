# تابع کوله پشتی کسری
def fractional_knapsack(items, capacity):
  """
  items: لیستی از لیست ها [value, weight]
  capacity: ظرفیت کوله پشتی
  """

  # 1️⃣ محاسبه نسبت ارزش به وزن برای هر آیتم
  for item in items:
    value, weight = item
    ratio = value / weight
    item.append(ratio)  # افزودن ratio به هر آیتم
    # در پایتون واقعی باید از لیست‌ها استفاده کنیم

  # 2️⃣ مرتب‌سازی آیتم‌ها بر اساس نسبت (v/w) به ترتیب نزولی
  items.sort(key=lambda x: x[2], reverse=True)

  print(items)

  total_value = 0.0     # مقدار کل ارزش داخل کوله
  remaining = capacity  # ظرفیت باقی‌مانده

  # 3️⃣ پر کردن کوله پشتی
  for value, weight, ratio in items:
    if remaining == 0:
      break  # ظرفیت پر شده

    if weight <= remaining:
      # کل آیتم را برمی‌داریم
      total_value += value
      remaining -= weight
    else:
      # فقط بخشی از آیتم را برمی‌داریم
      fraction = remaining / weight
      total_value += value * fraction
      remaining = 0

  return total_value


items = [
    [60, 10],
    [180, 60],
    [100, 20],
    [80, 4],
    [100, 25]
]

capacity = 50
result = fractional_knapsack(items, capacity)

print(result)
