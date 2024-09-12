from fileinput import close

def custom_write(file_name, strings):
    strings_positions = {}
    f = open(file_name, 'w', encoding='utf-8')
    for el in strings:
        f.write(el + '\n')
    f.close()
    f = open(file_name, 'r', encoding='utf-8')
    for i in range(len(strings)):
        line = f.readline().replace('\n', '')
        key = (i+1, f.tell())
        strings_positions.update({key: line})
    f.close()
    return strings_positions


info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!', '9999999']
result = custom_write('test.txt', info)
for el_dict in result.items():
    print(el_dict)
