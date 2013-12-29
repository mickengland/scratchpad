def inches_to_cm(inches):
    conversion = inches * 2.54
    print "There are %.2f centimeters in %.2f inches" % (conversion, inches)

s = raw_input('Enter the number of inches you want to convert: ')
ret = float(s)
inches_to_cm(ret)

