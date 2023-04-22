from api.depot import get_all_paints_remains_list
from colors.mixing import mix_paints, get_depot_info, get_missing_color
from picture.picture import get_pixel_matrix


def main():
    print(get_depot_info())
    # print(get_pixel_matrix('images/1.jpg'))
    # print(hex(get_missing_color(0xd8873f, 0, 0)))
    print(mix_paints(0x94D778))

if __name__ == '__main__':
    main()
