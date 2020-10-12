fruit = ['banana', 'apple', 'orange', 'pear']
price = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}
stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}

for i in fruit:
  print(i)
  for j in (price and stock):
    if j == i:
      print("price: ", price[j])
      print("stock: ", stock[j])
      print()


total = []

for i in fruit:
  for j in (price and stock):
    if j == i:
      a = price[j] * stock[j]
      total.append(a)

sum = sum(total)
print(f'Amount: {sum}')