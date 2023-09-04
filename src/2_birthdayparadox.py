import datetime
import random

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')


def get_birthdays(num_birthdays: int):
    # Trả về 1 list có 'num_birthdays' đối tượng date
    birthdays = []
    for i in range(num_birthdays):
        start_of_year = datetime.date(2001, 1, 1)  # Năm không quan trọng

        random_number_of_days = datetime.timedelta(random.randint(0, 364))  # Chọn độ lệch ngẫu nhiên tính từ 1/1
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)
    return birthdays


def get_match(birthdays):
    # Trả về đối tượng date trùng lặp trong list birthdays
    if len(birthdays) == len(set(birthdays)):  # Do ép kiểu list sang set sẽ loại bỏ phần tử trùng lặp
        return None

    # Hai vòng for để tìm ngày sinh trùng lặp (có thể sắp xếp và dùng chia để trị-->nhanh hơn nếu số lần mô phỏng lớn)
    for a, birthday_a in enumerate(birthdays):
        for b, birthday_b in enumerate(birthdays[a+1:]):
            if birthday_a == birthday_b:
                return birthday_a


while True:  # Hỏi cho đến khi người dùng cung cấp đúng đầu vào là số từ 1 đến 100
    print('Nhập số ngày sinh nhật bạn muốn tạo? (Tối đa 100)')
    response = input('>> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        num_birthdays = int(response)
        break
print()

# Generate and display the birthdays:
print('Đây là ', num_birthdays, 'sinh nhật được tạo ra:')
birthdays = get_birthdays(num_birthdays)
for i, birthday in enumerate(birthdays):
    if i != 0:  # Nếu không phải phần tử đầu thì in trước dấu phẩy để ngăn cách
        print(', ', end='')
    month_name = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(month_name, birthday.day)
    print(dateText, end='')
print("\n\n")

# Biến lưu ngày trùng lặp
match = get_match(birthdays)

# Display the results:
print('Ở ví dụ này, ', end='')
if match != None:
    month_name = MONTHS[match.month - 1]
    dateText = '{} {}'.format(month_name, match.day)
    print('nhiều hơn 1 người có ngày sinh nhật là', dateText)
else:
    print('không có ai trùng ngày sinh với nhau.')
print()

# Chạy 100.000 lần mô phỏng
print('Sản sinh ngẫu nhiên', num_birthdays, 'ngày sinh nhật 100.000 lần...')
input('Bấm Enter để bắt đầu...')

print('Bắt đầu chạy mô phỏng 100.000 lần.')
num_match = 0  # Biến lưu số lần mô phỏng trùng nhau
for i in range(100000):
    # Báo cáo tiến độ mỗi 10.000 lần mô phỏng
    if i % 10000 == 0:
        print(i, 'lần lặp đã hoàn thành...')
    birthdays = get_birthdays(num_birthdays)
    if get_match(birthdays) != None:
        num_match = num_match + 1
print('100.000 lần lặp đã hoàn thành.')

probability = round(num_match / 100000 * 100, 2)  # Làm tròn đến 2 chữ số thập phân
# In ra kêt quả
print('Trong 100.000 lần lặp với', num_birthdays, 'người, đã có', num_match, 'lần xuất hiện ngày sinh trùng nhau.')
print('Tức là cứ', num_birthdays, 'người, xác suất có ngày sinh trùng nhau là', probability, '%')
print('Đó chính là nghịch lý ngày sinh nhật!')
