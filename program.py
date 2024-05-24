from tests.car import Car, Color, Make, Model

def main():
    print('Hello world!')

    car = Car(vin='123456789', color=Color.RED, make=Make.TOYOTA, model=Model.COROLLA)
    print(car)
    car2 = Car(vin='123456789', color=Color.RED, make=Make.TOYOTA, model=Model.COROLLA)
    print(car2)
    car3 = Car(vin='123456789', color=Color.RED, make=Make.TOYOTA, model=Model.COROLLA)
    print(car3)

if __name__ == '__main__':
    main()
