from exception import Dataframe

def main():
    filename = input("Введите имя вашего файла: ")
    df = Dataframe(filename)

if __name__ == "__main__":
    main()