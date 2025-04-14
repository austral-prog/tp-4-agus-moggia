def leap_year():
	A = int(input("Ingrese un año: "))
	if A%4 == 0:
	    if A%100 != 0:
		    print(f"El año {A} es bisiesto")
	    elif A%400 == 0:
	    	print(f"El año {A} es bisiesto")
	    else:
	    	print(f"El año {A} no es bisiesto")
	else:
		print(f"El año {A} no es bisiesto")
