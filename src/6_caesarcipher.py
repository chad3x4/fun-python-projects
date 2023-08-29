import pyperclip  # module để copy kết quả vào clipboard (cho tiện)

# Có thể mã hóa các kí tự chữ cái, chữ số hoặc kí tự đặc biệt được giữ nguyên
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = 'abcdefghijklmnopqrstuvwxyz'

print('Mật mã Caesar là một hệ mật mã cổ diển.')
print('Nó là một hệ mã dịch vòng kinh điển, dù lỗi thời nhưng phù hợp với người mới bắt đầu tìm hiểu về mật mã')
print('Julius Caesar đưa ra vào thế kỷ thứ 1 trước CN, sử dụng trong quân sự')
print()

while True:  # Hỏi lại cho đến khi người dùng nhập đúng e hoặc d.
    print('Bạn muốn chọn encrypt (mã hóa) or decrypt (giải mã)?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'mã hóa'
        break
    elif response.startswith('d'):
        mode = 'giải mã'
        break
    print('Hãy chọn e hoặc d.')

while True:  # Hỏi lại cho đến khi người dùng nhập đúng giá trị số cho khóa
    maxKey = len(SYMBOLS) - 1
    print('Nhập khóa muốn dùng để mã hóa hoặc giải mã (từ 1 đến {}).'.format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue
    key = int(response)
    if 0 < int(response) < len(SYMBOLS):  # Tiếp tục hỏi cho đến khi người dùng nhập khóa hợp lệ
        break

print('Nhập thông điệp để {}.'.format(mode))
message = input('> ')

# Biến lưu trữ kết quả sau khi thực hiện mã hóa hoặc giải mã
translated = ''

# Mã hóa hoặc giải mã từng kí tự trong thông điệp
for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)  # Tìm vị trí của kí tự trong bảng chữ cái

        if mode == 'mã hóa':
            num = (num + key) % len(SYMBOLS)
        elif mode == 'giải mã':
            num = (num - key) % len(SYMBOLS)

        translated = translated + SYMBOLS[num]
    elif symbol in symbols:
        num = symbols.find(symbol)  # Tìm vị trí của kí tự trong bảng chữ cái

        if mode == 'mã hóa':
            num = (num + key) % len(symbols)
        elif mode == 'giải mã':
            num = (num - key) % len(symbols)

        translated = translated + symbols[num]
    else:
        # Nếu không phải kí tự chữ cái thì giữ nguyên
        translated = translated + symbol

print(translated)  # In kết quả ra

pyperclip.copy(translated)  # Copy kết quả vào clipboard
print('Thông điệp đã {} vừa được copy vào clipboard.'.format(mode))
