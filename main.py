from api.depot import get_all_paints_remains_list
from colors.mixing import mix_paints, get_depot_info


def main():
    mix_paints(0)
    print(get_depot_info())


if __name__ == '__main__':
    main()
