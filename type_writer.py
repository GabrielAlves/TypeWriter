import turtle
import string

class TypeWriter(object):
    def __init__(self):
        self.cursor = turtle.Turtle()
        self.cursor.speed(10)
        self.cursor.pensize(3)
        self.pen_color = "Black"
        self.set_pen_color()

        self.color_chart = ["Black", "Gray", "Red", "Green", "Blue", "Yellow"]
        self.color_chart_index = 0

        self.segment_width = 40
        self.distance_between_letters = 2 * self.segment_width
        self.distance_between_lines = 3 * self.segment_width
        self.distance_space_key = 4 * self.segment_width

        self.initial_x_position = -400
        self.initial_y_position = 200
        self.initial_drawing_point = (self.initial_x_position, self.initial_y_position)

        self.actions = {
            "a" : self.write_letter_a,
            "b" : self.write_letter_b,
            "c" : self.write_letter_c,
            "d" : self.write_letter_d,
            "e" : self.write_letter_e,
            "f" : self.write_letter_f,
            "g" : self.write_letter_g,
            "h" : self.write_letter_h, 
            "i" : self.write_letter_i,
            "j" : self.write_letter_j,
            "k" : self.write_letter_k,
            "l" : self.write_letter_l,
            "m" : self.write_letter_m,
            "n" : self.write_letter_n,
            "o" : self.write_letter_o,
            "p" : self.write_letter_p,
            "q" : self.write_letter_q,
            "r" : self.write_letter_r,
            "s" : self.write_letter_s,
            "t" : self.write_letter_t,
            "u" : self.write_letter_u,
            "v" : self.write_letter_v,
            "w" : self.write_letter_w,
            "x" : self.write_letter_x,
            "y" : self.write_letter_y,
            "z" : self.write_letter_z,
            "0" : self.write_number_0,
            "1" : self.write_number_1,
            "2" : self.write_number_2,
            "3" : self.write_number_3,
            "4" : self.write_number_4,
            "5" : self.write_number_5,
            "6" : self.write_number_6,
            "7" : self.write_number_7,
            "8" : self.write_number_8,
            "9" : self.write_number_9,
            "space" : self.space_letters,
            "Up" : self.move_up,
            "Down" : self.move_down,
            "Left" : self.move_left,
            "Right" : self.move_right,
            "Return" : self.break_line,
            "BackSpace" : self.undo,
            "Escape" : self.close_window,
            "Delete" : self.close_window,
            1 : self.move_color_chart_index_to_left,
            3 : self.move_color_chart_index_to_right
        }

        self.move_to_initial_drawing_point()
        self.binding()

    
    def set_pen_color(self):
        self.cursor.pencolor(self.pen_color)
        self.change_window_title()

    
    def change_window_title(self):
        self.cursor.screen.title(f"Pen Color : {self.pen_color}")

    
    def binding(self):
        turtle.listen()

        for event in self.actions:
            action = self.actions[event]

            if type(event) is int:
                turtle.onscreenclick(action, event)
                continue

            turtle.onkey(action, event)

            if event in string.ascii_lowercase:
                turtle.onkey(action, event.upper())



    def move_to_initial_drawing_point(self):
        self.cursor.penup()
        self.cursor.setposition(self.initial_drawing_point)
        self.cursor.pendown()


    def move_right(self):
        self.cursor.penup()
        self.cursor.forward(self.distance_between_letters)
        self.cursor.pendown()

    
    def move_left(self):
        self.cursor.setheading(180)
        self.cursor.penup()
        self.cursor.forward(self.distance_between_letters)
        self.cursor.setheading(0)
        self.cursor.pendown()


    def move_up(self):
        self.cursor.penup()
        self.cursor.setheading(90)
        self.cursor.forward(self.distance_between_lines)
        self.cursor.setheading(0)
        self.cursor.pendown()


    def move_down(self):
        self.cursor.penup()
        self.cursor.setheading(270)
        self.cursor.forward(self.distance_between_lines)
        self.cursor.setheading(0)
        self.cursor.pendown()


    def break_line(self):
        self.cursor.penup()
        self.cursor.setx(self.initial_x_position)
        self.cursor.right(90)
        self.cursor.forward(3 * self.segment_width)
        self.cursor.left(90)
        self.cursor.pendown()

    
    def space_letters(self):
        self.cursor.penup()
        self.cursor.forward(self.distance_space_key)
        self.cursor.pendown()


    def close_window(self):
        turtle.Screen().bye()


    def undo(self):
        self.cursor.undo()


    def move_color_chart_index_to_left(self, x, y):
        self.color_chart_index -= 1

        if self.color_chart_index < 0:
            self.color_chart_index = len(self.color_chart) - 1

        self.pen_color = self.color_chart[self.color_chart_index]
        self.set_pen_color()


    def move_color_chart_index_to_right(self, x, y):
        self.color_chart_index += 1

        if self.color_chart_index > len(self.color_chart) - 1:
            self.color_chart_index = 0

        self.pen_color = self.color_chart[self.color_chart_index]
        self.set_pen_color()


    def write_letter_a(self):
        self.cursor.setheading(90)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.setheading(0)
        self.cursor.forward(self.segment_width)
        self.cursor.setheading(270)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.backward(self.segment_width)
        self.cursor.setheading(180)
        self.cursor.forward(self.segment_width)
        self.cursor.setheading(270)
        self.cursor.forward(self.segment_width )
        self.cursor.setheading(0)


    def write_letter_b(self):
        self.cursor.setheading(0)
        self.cursor.forward(self.segment_width)
        self.cursor.setheading(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(180)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.left(180)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.left(90)


    def write_letter_c(self):
        self.cursor.setheading(0)
        self.cursor.forward(self.segment_width)
        self.cursor.left(180)
        self.cursor.forward(self.segment_width)
        self.cursor.right(90)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.right(90)
        self.cursor.forward(self.segment_width)
        self.cursor.penup()
        self.cursor.right(90)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.right(90)
        self.cursor.forward(self.segment_width)
        self.cursor.right(180)
        self.cursor.pendown()


    def write_letter_d(self):
        self.cursor.setheading(0)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.left(180)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.right(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(180)


    def write_letter_e(self):
        self.cursor.setheading(90)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.right(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(180)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width )
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(180)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width )
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(180)
        self.cursor.forward(self.segment_width)
        self.cursor.left(180)


    def write_letter_f(self):
        self.cursor.setheading(90)
        self.cursor.forward(self.segment_width * 2)
        self.cursor.right(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(180)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(180)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width )
        self.cursor.left(90)


    def write_letter_g(self):
        self.cursor.setheading(0)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.penup()
        self.cursor.forward(self.segment_width)
        self.cursor.pendown()
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.left(90)


    def write_letter_h(self):
        self.cursor.setheading(90)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.left(180)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(180)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.penup()
        self.cursor.right(90)
        self.cursor.forward(self.segment_width)
        self.cursor.right(180)
        self.cursor.pendown()


    def write_letter_i(self):
        self.cursor.setheading(90)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.left(180)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.left(90)


    def write_letter_j(self):
        self.cursor.setheading(0)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.left(90)
        self.cursor.penup()
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.pendown()
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)


    def write_letter_k(self):
        self.cursor.setheading(90)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.right(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(180)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.right(90)
        self.cursor.forward(self.segment_width)
        self.cursor.right(90)
        self.cursor.penup()
        self.cursor.forward(self.segment_width)
        self.cursor.pendown()
        self.cursor.left(180)


    def write_letter_l(self):
        self.cursor.setheading(90)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.left(180)
        self.cursor.forward(2 * self.segment_width)        
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(180)
        self.cursor.forward(self.segment_width)
        self.cursor.left(180)


    def write_letter_m(self):
        self.cursor.setheading(0)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.penup()
        self.cursor.forward(self.segment_width)
        self.cursor.pendown()
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.penup()
        self.cursor.forward(self.segment_width)
        self.cursor.pendown()
        self.cursor.left(90)


    def write_letter_n(self):
        self.cursor.setheading(90)
        self.cursor.forward(self.segment_width)
        self.cursor.right(90)
        self.cursor.forward(self.segment_width)
        self.cursor.right(90)
        self.cursor.forward(self.segment_width)
        self.cursor.right(90)
        self.cursor.penup()
        self.cursor.forward(self.segment_width)
        self.cursor.pendown()
        self.cursor.left(180)


    def write_letter_o(self):
        self.cursor.setheading(0)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)


    def write_letter_p(self):
        self.cursor.setheading(90)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.right(90)
        self.cursor.forward(self.segment_width)
        self.cursor.right(90)        
        self.cursor.forward(self.segment_width)
        self.cursor.right(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)


    def write_letter_q(self):
        self.cursor.setheading(0)
        self.cursor.penup()
        self.cursor.forward(self.segment_width)
        self.cursor.pendown()
        self.cursor.left(90)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.right(90)
        self.cursor.forward(self.segment_width)
        self.cursor.right(90)
        self.cursor.penup()
        self.cursor.forward(self.segment_width)
        self.cursor.pendown()
        self.cursor.left(180)


    def write_letter_r(self):
        self.cursor.setheading(90)
        self.cursor.forward(self.segment_width)
        self.cursor.right(90)
        self.cursor.forward(self.segment_width)
        self.cursor.right(90)
        self.cursor.penup()
        self.cursor.forward(self.segment_width)
        self.cursor.right(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(180)
        self.cursor.pendown()


    def write_letter_s(self):
        self.cursor.setheading(0)
        self.cursor.forward(self.segment_width)        
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)        
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.right(90)
        self.cursor.forward(self.segment_width)
        self.cursor.right(90)
        self.cursor.forward(self.segment_width)
        self.cursor.right(90)
        self.cursor.penup()
        self.cursor.forward(2 * self.segment_width)
        self.cursor.right(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(180)
        self.cursor.pendown()


    def write_letter_t(self):
        self.cursor.setheading(90)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.left(180)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(180)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(180)
        self.cursor.forward(self.segment_width)
        self.cursor.left(180)


    def write_letter_u(self):
        self.cursor.setheading(90)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.left(180)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.left(180)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.right(90)
        self.cursor.forward(self.segment_width)
        self.cursor.right(180)


    def write_letter_v(self):
        self.cursor.setheading(0)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.penup()
        self.cursor.forward(self.segment_width)
        self.cursor.pendown()
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.penup()
        self.cursor.forward(self.segment_width)
        self.cursor.pendown()
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.penup()
        self.cursor.forward(self.segment_width)
        self.cursor.pendown()
        self.cursor.left(90)


    def write_letter_w(self):
        self.cursor.setheading(0)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.left(180)
        self.cursor.forward(self.segment_width)
        self.cursor.right(90)
        self.cursor.forward(self.segment_width)
        self.cursor.right(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(180)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.left(90)


    def write_letter_x(self):
        self.cursor.setheading(0)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.penup()
        self.cursor.forward(self.segment_width)
        self.cursor.pendown()
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.right(90)
        self.cursor.penup()
        self.cursor.forward(self.segment_width)
        self.cursor.right(90)
        self.cursor.pendown()
        self.cursor.forward(self.segment_width)
        self.cursor.penup()
        self.cursor.right(90)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.right(90)
        self.cursor.forward(self.segment_width)
        self.cursor.pendown()
        self.cursor.left(180)



    def write_letter_y(self):
        self.cursor.setheading(0)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.left(180)
        self.cursor.forward(self.segment_width)
        self.cursor.right(90)
        self.cursor.forward(self.segment_width)
        self.cursor.right(90)
        self.cursor.forward(self.segment_width)
        self.cursor.right(180)
        self.cursor.penup()
        self.cursor.forward(2 * self.segment_width)
        self.cursor.pendown()
        self.cursor.left(90)


    def write_letter_z(self):
        self.cursor.setheading(0)
        self.cursor.forward(self.segment_width)
        self.cursor.left(180)
        self.cursor.forward(self.segment_width)
        self.cursor.right(90)        
        self.cursor.forward(self.segment_width )
        self.cursor.right(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.penup()
        self.cursor.forward(2 * self.segment_width)
        self.cursor.pendown()
        self.cursor.left(90)


    def write_number_0(self):
        self.cursor.setheading(0)
        self.cursor.forward(self.segment_width)
        self.cursor.setheading(90)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.setheading(180)
        self.cursor.forward(self.segment_width)
        self.cursor.setheading(270)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.setheading(0)

    
    def write_number_1(self):
        self.cursor.setheading(0)
        self.cursor.penup()
        self.cursor.forward(self.segment_width)
        self.cursor.pendown()
        self.cursor.setheading(90)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.backward(2 * self.segment_width)
        self.cursor.setheading(0)
        self.cursor.penup()
        self.cursor.backward(self.segment_width)
        self.cursor.pendown()


    def write_number_2(self):
        self.cursor.setheading(0)
        self.cursor.forward(self.segment_width)
        self.cursor.left(180)
        self.cursor.forward(self.segment_width)
        self.cursor.right(90)        
        self.cursor.forward(self.segment_width )
        self.cursor.right(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.penup()
        self.cursor.forward(2 * self.segment_width)
        self.cursor.pendown()
        self.cursor.left(90)


    def write_number_3(self):
        self.cursor.setheading(0)
        self.cursor.forward(self.segment_width)
        self.cursor.setheading(90)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.setheading(180)
        self.cursor.forward(self.segment_width)
        self.cursor.penup()
        self.cursor.setheading(270)
        self.cursor.forward(self.segment_width)
        self.cursor.setheading(0)
        self.cursor.pendown()
        self.cursor.forward(self.segment_width)
        self.cursor.backward(self.segment_width)
        self.cursor.penup()
        self.cursor.setheading(270)
        self.cursor.forward(self.segment_width)
        self.cursor.setheading(0)
        self.cursor.pendown()


    def write_number_4(self):
        self.cursor.setheading(0)
        self.cursor.penup()
        self.cursor.forward(self.segment_width)
        self.cursor.pendown()
        self.cursor.setheading(90)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.backward(self.segment_width)
        self.cursor.setheading(180)
        self.cursor.forward(self.segment_width)
        self.cursor.setheading(90)
        self.cursor.forward(self.segment_width)
        self.cursor.penup()
        self.cursor.backward(2 * self.segment_width)
        self.cursor.pendown()
        self.cursor.setheading(0)

    
    def write_number_5(self):
        self.cursor.setheading(0)
        self.cursor.forward(self.segment_width)
        self.cursor.setheading(90)
        self.cursor.forward(self.segment_width)
        self.cursor.setheading(180)
        self.cursor.forward(self.segment_width)
        self.cursor.setheading(90)
        self.cursor.forward(self.segment_width)
        self.cursor.setheading(0)
        self.cursor.forward(self.segment_width)
        self.cursor.penup()
        self.cursor.setheading(270)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.setheading(0)
        self.cursor.backward(self.segment_width)
        self.cursor.pendown()


    def write_number_6(self):
        self.cursor.setheading(0)
        for i in range(4):
            self.cursor.forward(self.segment_width)
            self.cursor.left(90)
        self.cursor.setheading(90)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.setheading(0)
        self.cursor.forward(self.segment_width)
        self.cursor.backward(self.segment_width)
        self.cursor.setheading(270)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.setheading(0)

    
    def write_number_7(self):
        self.cursor.setheading(0)
        self.cursor.penup()
        self.cursor.forward(self.segment_width)
        self.cursor.pendown()
        self.cursor.setheading(90)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.setheading(180)
        self.cursor.forward(self.segment_width)
        self.cursor.penup()
        self.cursor.setheading(270)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.setheading(0)
        self.cursor.pendown()

    
    def write_number_8(self):
        self.cursor.setheading(0)
        self.cursor.forward(self.segment_width)
        self.cursor.setheading(90)
        self.cursor.forward(self.segment_width)
        self.cursor.setheading(180)
        self.cursor.forward(self.segment_width)
        self.cursor.setheading(90)
        self.cursor.forward(self.segment_width)
        self.cursor.setheading(0)
        self.cursor.forward(self.segment_width)
        self.cursor.setheading(270)
        self.cursor.forward(self.segment_width)
        self.cursor.setheading(180)
        self.cursor.forward(self.segment_width)
        self.cursor.setheading(270)
        self.cursor.forward(self.segment_width)
        self.cursor.setheading(0)

    
    def write_number_9(self):
        self.cursor.setheading(0)
        self.cursor.penup()
        self.cursor.forward(self.segment_width)
        self.cursor.pendown()
        self.cursor.left(90)
        self.cursor.forward(2 * self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(90)
        self.cursor.forward(self.segment_width)
        self.cursor.right(90)
        self.cursor.forward(self.segment_width)
        self.cursor.right(90)
        self.cursor.forward(self.segment_width)
        self.cursor.left(180)

        
if __name__ == "__main__":
    TypeWriter()
    turtle.mainloop()