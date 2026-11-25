from builtins import print

gewicht = float(input("wat is je gewicht in kg? "))
lengte= float(input("wat is je lengte in meters?"))

bmi=gewicht/(lengte**2)
print(f"jou bmi is{round(bmi,1)}")
if bmi<18.5:
    print(" categorie:ondergewicht")
elif bmi < 25:
    print(" categorie:gemiddeld")
elif bmi < 30:
    print(" categorie:overgewicht")
