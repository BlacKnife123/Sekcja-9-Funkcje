import math

def poleProstokata(x,y):
    return x*y

def poleKwadratu(x):
    return x*x

def poleTrojkata(x,h):
    return x*h/2

def poleTrapezu(x,y,h):
    return (x+y)*h/2

def poleKola(r):
    return r*r*math.pi

while True:
    print("1) Pole prostokąta")
    print("2) Pole kwadratu")
    print("3) Pole trójkąta")
    print("4) Pole trapezu")
    print("5) Pole koła")
    print("6) Wyjście")
    wybor = int(input("Co chcesz obliczyć jeśli chcesz wyjść naciśnij 6: "))

    if wybor == 1:
        x = int(input("Wprowadź długość pierwszego boku: "))
        y = int(input("Wprowadź długość drugiego boku: "))
        print("Pole prostokąta jest równe:",poleProstokata(x,y))
    elif wybor == 2:
        x = int(input("Wprowadź długość boku: "))
        print("Pole kwadratu jest równe:",poleKwadratu(x))
    elif wybor == 3:
        x = int(input("Wprowadź długość boku: "))
        h = int(input("Wprowadź długość wysokości: "))
        print("Pole trójkąta jest równe:",poleTrojkata(x,h))
    elif wybor == 4:
        x = int(input("Wprowadź długość pierwszej podstawy: "))
        y = int(input("Wprowadź długość drugiej podstawy: "))
        h = int(input("Wprowadź długość wysokości: "))
        print("Pole trapezu jest równe:",poleTrapezu(x,y,h))
    elif wybor == 5:
        r = int(input("Wprowadź długość średnicy: "))
        print("Pole koła jest równe:",poleKola(r))
    elif wybor == 6:
        print("No to pa")
        break
    else:
        print("Nie ma takiego wyboru spróbuj ponownie")


