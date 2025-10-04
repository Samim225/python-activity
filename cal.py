# نصب کتابخانه‌ها (اگر نصب نیست)
# pip install numpy scikit-learn tensorflow

import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# داده‌های آموزشی: قد (cm) → وزن (kg)
X = np.array([150, 160, 170, 180, 190], dtype=float)
y = np.array([50, 55, 65, 70, 80], dtype=float)

# تبدیل داده‌ها به شکل (نمونه‌ها، ویژگی‌ها)
X = X.reshape(-1, 1)

# تقسیم داده‌ها به آموزش و تست
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# تعریف مدل شبکه عصبی
model = Sequential()
model.add(Dense(10, input_dim=1, activation='relu'))  # لایه پنهان با 10 نورون
model.add(Dense(1))  # لایه خروجی (وزن)

# کامپایل مدل
model.compile(optimizer='adam', loss='mean_squared_error')

# آموزش مدل
model.fit(X_train, y_train, epochs=500, verbose=0)

# پیش‌بینی
predicted = model.predict(X_test)
for i, val in enumerate(X_test):
    print(f"قد: {val[0]}, وزن واقعی: {y_test[i]}, وزن پیش‌بینی: {predicted[i][0]:.2f}")
