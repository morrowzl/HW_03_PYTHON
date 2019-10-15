shopping = 'y'

pie_purchases = []

pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun", "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

print("Welcome to the House of Pies! Here are today's pies:")

while shopping == 'y':
    
    print("---------------------------------------------------------------------" +
          "")
    print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, " +
          "(5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, " +
          "(9) Tamale, (10) Steak" +
          "")
    
    pie_choice = int(input("Which would you like? "
                           ""))
                
    pie_purchases.append(pie_choice)
    
    print("------------------------------------------------------------------------" +
          "")
    
    print("Great! We'll have that " + pie_list[int(pie_choice) - 1] + " right out for you.")
    
    shopping = input("Would you like to make another purchase: (y) or (n)o? ")
    
    
print("------------------------------------------------------------------------")

print("You purchased the following for a total of " + str(len(pie_purchases)) + " pies:" + "")

print(" - " + str(pie_purchases.count(1)) + " " + pie_list[0])
print(" - " + str(pie_purchases.count(2)) + " " + pie_list[1])
print(" - " + str(pie_purchases.count(3)) + " " + pie_list[2])
print(" - " + str(pie_purchases.count(4)) + " " + pie_list[3])
print(" - " + str(pie_purchases.count(5)) + " " + pie_list[4])
print(" - " + str(pie_purchases.count(6)) + " " + pie_list[5])
print(" - " + str(pie_purchases.count(7)) + " " + pie_list[6])
print(" - " + str(pie_purchases.count(8)) + " " + pie_list[7])
print(" - " + str(pie_purchases.count(9)) + " " + pie_list[8])
print(" - " + str(pie_purchases.count(10)) + " " + pie_list[9])