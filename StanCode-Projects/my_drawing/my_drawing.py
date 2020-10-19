"""
File: My drawing: Bonjour Paris
Name: Jenny Wei
----------------------
This program will draw a picture of a French flag and
Paris's most popular tourist attractions on the canvas.
"""


from campy.graphics.gobjects import GOval, GRect, GLabel, GLine
from campy.graphics.gwindow import GWindow

# global variables
window=GWindow(width=1200, height=800, title="Bonjour Paris")


def main():
    """
    This picture will draw the flag of France with France's most popular tourist attractions,
    including the Tower Eiffel, the Arch De Triomphe and the museum Louvre .
    創作理念：用python畫出我腦海裡的巴黎，包括巴黎鐵塔、凱旋門與羅浮宮！
    """
    flag()
    words_label()
    arch_triomphe_body()
    arch_triomphe_deco()
    Louvre()
    eiffel_tower()


def flag():
    """
    This function will draw the flag of France.
    """
    # blue part
    blue_flag=GRect(400, 800, x=0, y=0)
    blue_flag.filled=True
    blue_flag.fill_color='dark_blue'
    blue_flag.color='dark_blue'
    window.add(blue_flag)
    # red part
    red_flag=GRect(400, 800, x=800, y=0)
    red_flag.filled = True
    red_flag.fill_color = 'red'
    red_flag.color = 'red'
    window.add(red_flag)


def words_label():
    """
    This function will write the label of Bonjour Paris.
    """
    # paris label
    label2 = GLabel('PARIS', x=90, y=450)
    label2.font = '-80'
    label2.color = 'white'
    window.add(label2)
    # Bonjour label
    label3 = GLabel('BONJOUR', x=40, y=340)
    label3.font = '-70'
    label3.color = 'white'
    window.add(label3)


def eiffel_tower():
    """
    This function will draw the eiffel tower on the canvas.
    The tower is devided into four parts.
    """
    eiffel_tower_bottom()
    eiffel_tower_middle_lower()
    eiffel_tower_middle_top()
    eiffel_tower_top()


def eiffel_tower_bottom():
    """
    This function will draw the eiffel tower's bottom on the canvas.
    """
    bottom = GRect(398, 100, x=401, y=705)
    bottom.filled = True
    bottom.fill_color = 'gray'
    bottom.color = 'gray'
    window.add(bottom)
    for i in range(20):
        rect = GRect(90-(i*5), 10, x=401, y=700+i*5)
        rect.filled=True
        rect.fill_color = 'white'
        rect.color = 'white'
        window.add(rect)
    for i in range(20):
        rect = GRect(90-(i*5), 10, x=709+i*5, y=700+i*5)
        rect.filled = True
        rect.fill_color = 'white'
        rect.color = 'white'
        window.add(rect)
    arch = GOval(150, 150, x=523, y=730)
    arch.filled = True
    arch.fill_color = 'white'
    arch.color = 'white'
    window.add(arch)


def eiffel_tower_middle_lower():
    """
    This function will draw the middle lower part of the
    Eiffel tower
    """
    for i in range(11):
        square = GRect(19, 19, x=495+19*i, y=681)
        square.filled = True
        square.fill_color = 'gray'
        square.color = 'white'
        window.add(square)
    middle = GRect(206, 65, x=496, y=610)
    middle.filled = True
    middle.fill_color = 'gray'
    middle.color = 'gray'
    window.add(middle)
    for i in range(10):
        rect = GRect(100-(i*5), 35, x=450, y=550+i*10)
        rect.filled = True
        rect.fill_color = 'white'
        rect.color = 'white'
        window.add(rect)
    for i in range(10):
        rect = GRect(100-(i*5), 35, x=650+i*5, y=550+i*10)
        rect.filled = True
        rect.fill_color = 'white'
        rect.color = 'white'
        window.add(rect)
    middle_square = GRect(75, 30, x=563, y=650)
    middle_square.filled = True
    middle_square.fill_color = 'white'
    middle_square.color = 'white'
    window.add(middle_square)
    top_line = GRect(130, 30, x=535, y=573)
    top_line.filled = True
    top_line.fill_color = 'gray'
    top_line.color = 'gray'
    window.add(top_line)


def eiffel_tower_middle_top():
    """
    This function will draw the middle upper part of the
    Eiffel tower
    """
    big_square = GRect(130, 245, x=535, y=320)
    big_square.filled = True
    big_square.fill_color = 'gray'
    big_square.color = 'gray'
    window.add(big_square)
    for i in range(30):
        rect = GRect(30, 30, x=538-i*1.15, y=250+i*10)
        rect.filled = True
        rect.fill_color = 'white'
        rect.color = 'white'
        window.add(rect)
    for i in range(30):
        rect = GRect(30, 30, x=632 + i * 1.15, y=250 + i * 10)
        rect.filled = True
        rect.fill_color = 'white'
        rect.color = 'white'
        window.add(rect)
    for i in range(14):
        triangle = GRect(40-i, 13, x=570+i, y=545-i*13)
        triangle.filled = True
        triangle.fill_color = 'white'
        triangle.color = 'white'
        window.add(triangle)
    for i in range(14):
        triangle = GRect(40-i, 13, x=593-i/2, y=545-i*13)
        triangle.filled = True
        triangle.fill_color = 'white'
        triangle.color = 'white'
        window.add(triangle)


def eiffel_tower_top():
    """
    This function will draw the top part of the
    Eiffel tower.
    """
    for i in range(3):
        square = GRect((65-i*15), 25, x=568+(i*7), y=290-(i*30))
        square.filled = True
        square.fill_color = 'gray'
        square.color = 'gray'
        window.add(square)
    pin= GRect(10, 50, x=595, y=175)
    pin.filled = True
    pin.fill_color = 'gray'
    pin.color = 'gray'
    window.add(pin)


def arch_triomphe_body():
    """
    This function will draw the body part of the
    Arch de Triomphe.
    """
    body = GRect(280,280, x=860, y=520)
    body.filled = True
    body.fill_color = 'white'
    body.color = 'white'
    window.add(body)
    arch = GOval(170,290,x=915,y=610)
    arch.filled = True
    arch.fill_color = 'red'
    arch.color = 'red'
    window.add(arch)
    middle_line = GRect(280, 15, x=860, y=660)
    middle_line.filled = True
    middle_line.fill_color = 'red'
    middle_line.color = 'red'
    window.add(middle_line)
    upper_line = GRect(280, 15, x=860, y=600)
    upper_line.filled = True
    upper_line.fill_color = 'red'
    upper_line.color = 'red'
    window.add(upper_line)
    top_line = GRect(280, 20, x=860, y=550)
    top_line.filled = True
    top_line.fill_color = 'red'
    top_line.color = 'red'
    window.add(top_line)


def arch_triomphe_deco():
    """
    This function will add the deco part on the Arch de Triomphe.
    """
    # middle circle part
    middle_circle = GOval(60, 60, x=970, y=580)
    middle_circle.filled = True
    middle_circle.fill_color = 'white'
    middle_circle.color = 'white'
    window.add(middle_circle)
    middle_circle_inside = GOval(40, 40, x=980, y=590)
    middle_circle_inside.filled = True
    middle_circle_inside.fill_color = 'red'
    middle_circle_inside.color = 'red'
    window.add(middle_circle_inside)
    # dots on the roof
    for i in range(9):
        small_dot = GOval(15,15, x=875+(i*30), y=528)
        small_dot.filled = True
        small_dot.fill_color = 'red'
        small_dot.color = 'red'
        window.add(small_dot)
    # small squares on the pillar
    for i in range(2):
        small_square = GRect(20, 20, x=890+(i*200), y=630)
        small_square.filled = True
        small_square.fill_color = 'red'
        small_square.color = 'red'
        window.add(small_square)
    # ovals on the pillar
    for i in range(2):
        small_oval = GOval(20,50, x=875+(i*230), y=690)
        small_oval.filled = True
        small_oval.fill_color = 'red'
        small_oval.color = 'red'
        window.add(small_oval)
    # lines on the pillar
    for i in range(2):
        small_line = GRect(30, 5, x=870 + (i * 230), y=750)
        small_line.filled = True
        small_line.fill_color = 'red'
        small_line.color = 'red'
        window.add(small_line)


def Louvre():
    """
    This function will draw the Louvre museum.
    """
    # Louvre museum's body
    body = GRect(400, 300, x=0, y=520)
    body.filled = True
    body.fill_color = 'white'
    body.color = 'white'
    window.add(body)
    # to cut the body into triangle
    for i in range(200):
        l_cut = GRect(200-i, 1.5, x=0, y=520+i*1.4)
        l_cut.filled = True
        l_cut.fill_color = 'dark_blue'
        l_cut.color = 'dark_blue'
        window.add(l_cut)
    for i in range(200):
        l_cut = GRect(200-i, 1.5, x=200+i, y=520+i*1.4)
        l_cut.filled = True
        l_cut.fill_color = 'dark_blue'
        l_cut.color = 'dark_blue'
        window.add(l_cut)
    for i in range(8):
        left_line=GLine(20*i, 800-(40*i), i*50, 800)
        left_line.color='dark_blue'
        window.add(left_line)
    for i in range(8):
        right_line = GLine(45 *(i+1), 800, 230+i*30, 550+i*10)
        right_line.color = 'dark_blue'
        window.add(right_line)
    # to cover the line that out of the range
    rect= GRect(40, 110, x=401, y=600)
    rect.filled = True
    rect.fill_color = 'white'
    rect.color = 'white'
    window.add(rect)



if __name__ == '__main__':
    main()
