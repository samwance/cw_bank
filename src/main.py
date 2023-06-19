from utils import get_data, select_data, sort_data, format_data



def main():
    data = get_data()
    data = select_data(data)
    data = sort_data(data)
    data = format_data(data)
    print(*data)


if __name__ == "__main__":
    main()
