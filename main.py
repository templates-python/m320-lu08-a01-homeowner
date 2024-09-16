from home_owner import HomeOwner
from house import House


def main():
    house = House('Landhaus')
    owner = HomeOwner('Ron', house)  # Dem owner wird die Referenz zum Haus mitgegeben.
    print(owner)


if __name__ == '__main__':
    main()
