from MyList import MyList



def main():
    list_ = MyList()
    print("Podawaj wartości do wpisania na listę. Wpisanie -1 powoduje koniec wczytywania")

    while True:
        value = int(input())
        if value == -1:
            break
        list_.add_element(value)

    print("-----------------------")
    list_.display()

    list_.add_element(10)
    print("-----------------------")
    list_.display()

    list_.remove_element()
    print("-----------------------")
    list_.display()


if __name__ == "__main__":
    main()