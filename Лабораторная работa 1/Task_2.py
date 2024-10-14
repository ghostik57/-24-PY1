pages = 100
line = 50
symbols = 25
value_disk = 1.44
one_symbol = 4
symbol_on_page = symbols*line
symbols_in_book = symbol_on_page*pages
value_symbol = int(4*symbols_in_book)
value_disk_bits = int(value_disk*1024*1024)
books = (value_disk_bits//value_symbol)
print("Количество книг, помещающихся на дискету:", books)
