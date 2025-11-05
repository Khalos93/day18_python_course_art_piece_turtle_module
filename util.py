import random


def draw_modern_painting(timmy, x_cor: int, y_cor: int, size: int, colors_list):
    for _ in range(0, size):
        y_cor += 50
        timmy.setx(x_cor)
        timmy.sety(y_cor)
        for _ in range(0, size):
            timmy.dot(20, random.choice(colors_list))
            timmy.forward(50)
