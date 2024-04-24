book_1_price = 10
book_2_price = 20
book_3_price = 30
book_4_price = 40
book_5_price = 50
book_6_price = 60
book_7_price = 70
book_8_price = 80
book_9_price = 90
book_10_price = 100

small_discount = 10
large_discount = 20

book1_afther_small_discount = book_1_price - (book_1_price * small_discount/100)
book_small_discount2 = book_2_price * small_discount/100
book_small_discount3 = book_3_price * small_discount/100
book_small_discount4 = book_4_price * small_discount/100
book_small_discount5 = book_5_price * small_discount/100

book_large_discount1 = book_1_price * small_discount/100
book_large_discount2 = book_2_price * small_discount/100
book_large_discount3 = book_3_price * small_discount/100
book_large_discount4 = book_4_price * small_discount/100
book_large_discount5 = book_5_price * small_discount/100

print("book1'prise is",book1_afther_small_discount,"book2's prise is",book_small_discount2,
      "book3's prise is",book_small_discount3,"book4's price is",book_small_discount4
      ,"book5's price is",book_small_discount5)

print("book6 costs",book_large_discount1,"book7 costs",book_large_discount2,
      "book8 costs",book_large_discount3,"book9 costs",book_large_discount4,
      "book10 costs",book_large_discount5,)