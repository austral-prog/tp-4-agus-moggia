def leap_year():
   A = int(input("Ingrese un año: "))

    if A%4 == 0:
	    if A%100 != 0:
		    print(f"El año {A} es biciesto")
	    if A%400 == 0:
		    print(f"El año {A} es biciesto")
    else:
	    print(f"El año {A} no es biciesto")
