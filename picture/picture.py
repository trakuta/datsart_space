from PIL import Image


def get_pixel_matrix(image_path):
    # загружаем изображение
    img = Image.open(image_path)

    # получаем размеры изображения
    width, height = img.size

    # создаем пустую матрицу для хранения пикселей
    pixel_matrix = [[None for x in range(width)] for y in range(height)]

    # проходим по каждому пикселю в изображении
    for x in range(width):
        for y in range(height):
            # получаем RGB-значение пикселя
            pixel = img.getpixel((x, y))
            # сохраняем его в матрицу
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            pixel_matrix[y][x] = (r << 16) ^ (g << 8) ^ b

    return pixel_matrix
