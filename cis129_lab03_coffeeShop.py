#num of coffees and muffins bought
#make a price for items
#add prices and total number of items bought
#put receipt statements together
#add total + sales tax for overall total
print("***************************************")
print("My Coffee and Muffin Shop")
print("Number of Coffees Bought?")
num_coffee = int(input())
(num_coffee)
print("Number of Muffins Bought?")
num_muffin = int(input())
(num_muffin)
print("***************************************\n\n***************************************")
print("My Coffee and Muffin Shop Receipt")
total_coffee = 5 * num_coffee
total_muffin = 4 * num_muffin
print(num_coffee, 'Coffee at $5 each: $', format(total_coffee,'.2f'))
print(num_muffin, 'Muffin at $4 each: $', format(total_muffin,'.2f'))
print('6% sales tax: $', round((total_coffee + total_muffin) * .06 ,2))
print('---------')
print('Total: $', total_coffee + total_muffin + round((total_coffee + total_muffin) * .06 ,2))
print("***************************************")
