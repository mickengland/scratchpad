def inches_to_cm(inches):
    conversion = inches * 2.54
    print "There are %.2f centimeters in %.2f inches" % (conversion, inches)

s = raw_input('Enter the number of inches you want to convert: ')
ret = float(s)
inches_to_cm(ret)

#Assigns 20 to cheese_count and 30 to boxes_of_crackers
#print "We can just give the function numbers directly"
#cheese_and_crackers(20, 30)

#Assigns the variables and uses them as arguments to cheese_and_crackers function
#print "Or we can use variables for our scripts:"
#amount_of_cheese = 10
#amount_of_crackers = 50

#cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#Uses math to assign the totals to the two variables
#print "We can even do math inside too:"
#cheese_and_crackers(10 + 20, 5 + 6)

#Uses math to change the two variables
#print "And we can combine the two, variables and math:"
#cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

