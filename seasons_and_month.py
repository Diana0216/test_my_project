
winter = ["december", "january", "february", 12, 1, 2]
spring = ["march", "april", "may", 3, 4, 5]
summer = ["june", "july", "august", 6, 7, 8]
autumn = ["september", "october", "november", 9, 10, 11]

user_imput = (input("Input the months name"))

if user_imput in winter:
    print "It`s a winter"

elif user_imput in spring:
    print "It`s a spring"

elif user_imput in summer:
    print "It`s a summer"

elif user_imput in autumn:
    print "It`s an  autumn"

else:
    print "Try again"

