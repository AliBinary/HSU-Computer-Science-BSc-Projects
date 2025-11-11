import cv2
# from cv2 import *
import numpy as np
from sklearn.cluster import DBSCAN

image = cv2.imread('ghezi\\Example.jpg', cv2.IMREAD_GRAYSCALE)

# image = cv2.imread('14_pp.jpg', cv2.IMREAD_GRAYSCALE)

# اعمال فیلتر گوسیان
image_blurred = cv2.GaussianBlur(image, (5, 5), 0)

# تشخیص لبه‌ها
edges = cv2.Canny(image_blurred, 100, 200)
# خواندن تصویر و تبدیل به مقیاس خاکستری


# تعیین نقاط سفید به عنوان داده‌های ورودی
white_points = np.argwhere(edges == 255)

# اجرای الگوریتم DBSCAN
dbscan = DBSCAN(eps=5, min_samples=13)
dbscan.fit(white_points)

# تعیین خوشه‌ها
labels = dbscan.labels_

# تعداد خوشه‌ها
num_clusters = len(set(labels)) - (1 if -1 in labels else 0)

# تشکیل تصویر نهایی با خوشه‌های مشخص شده
output_image = np.zeros_like(edges)
for i, point in enumerate(white_points):
    if labels[i] != -1:  # اگر نقطه به خوشه تعلق داشته باشد
        output_image[tuple(point)] = labels[i] * 255 // num_clusters

# نمایش تصویر نهایی
cv2.imshow('Clustered Image', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"تعداد خوشه‌ها: {num_clusters}")
