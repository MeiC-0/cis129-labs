#num of coffees and muffins bought + 2 more items
#make a price for items
#add prices and total number of items bought
#put receipt statements together
#add total + sales tax for overall total
print("***************************************")
print("My Cafe")
print("Number of Coffees Bought?")
num_coffee = int(input())
(num_coffee)
print("Number of Muffins Bought?")
num_muffin = int(input())
(num_muffin)
print('Number of Bagels Bought?')
num_bagel = int(input())
(num_bagel)
print('Number of Cakes Bought?')
num_cake = int(input())
(num_cake)
print("***************************************\n\n***************************************")
print("My Cafe Receipt")
total_coffee = 5 * num_coffee
total_muffin = 4 * num_muffin
total_bagel = 3.50 * num_bagel
total_cake = 3 * num_cake
print(num_coffee, 'Coffee at $5 each: $', format(total_coffee,'.2f'))
print(num_muffin, 'Muffin at $4 each: $', format(total_muffin,'.2f'))
print(num_bagel, 'Bagel at $3.50 each: $', format(total_bagel, '.2f'))
print(num_cake, 'Cakes at $3 each: $', format(total_cake, '.2f'))
print('6% sales tax: $', round((total_coffee + total_muffin + total_bagel + total_cake) * .06 ,2))
print('---------')
print('Total: $', total_coffee + total_muffin + total_bagel + total_cake + round((total_coffee + total_muffin + total_bagel + total_cake) * .06 ,2))
print("***************************************")
print("***************************************")
