from api.levels import get_next_level_info, start_next_level, get_current_level_info
from api.catapult import shoot

def main():
    print(get_current_level_info())


if __name__ == '__main__':
    main()