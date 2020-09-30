lovely_loveseat_description = 'Lovely Loveseat. Tufted polyester blend on wood. 32 inches x 40 inches wide x 30 inches deep. Red or white.'

lovely_loveseat_price = 254.00

stylish_settee_description = 'Stylist Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.'

stylist_settee_price = 180.50

Side Table = Side table 44*44*46

STOOL w/WOODEN TOP = STOOL w/WOODEN TOP in mango wood  33*33*46

CENTER TABLE WOODEN TOP (TEAK TOP) = 60*60*49

NEST OF 3 TABLES = 40*30*45

BED SIDE CABINET L&R OPEN = 50*40*70

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

luxurious_lamp_price = 52.15

sales_tax = 0.088

customer_one_total = 0
customer_one_itemization = ""

customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

customer_one_total += luxurious_lamp_price
customer_one_itemization += ", " + luxurious_lamp_description

customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax


print("Customer One Items: ")
print(customer_one_itemization + "\n")
print("Customer One Total: ")
print(customer_one_total)
