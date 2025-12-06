# TODO Найдите количество книг, которое можно разместить на дискете
disk_storage = 1.44
sheets = 100
strings_on_one_sheet = 50
symbols_on_one_sheet = 25
symbol_code = 4
book_mass = symbol_code * symbols_on_one_sheet*strings_on_one_sheet*sheets
disk_storage_bt = disk_storage * 1024 ** 2
number_books = int(disk_storage_bt // book_mass)
print("Количество книг, помещающихся на дискету:", number_books)
