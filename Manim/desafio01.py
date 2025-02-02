from manim import *

SCALE_FACTOR = 0.8

tmp_pixel_height = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = tmp_pixel_height

config.frame_height = config.frame_height/SCALE_FACTOR
config.frame_width = config.frame_height * 9/16

FRAME_HEIGHT = config.frame_height
FRAME_WIDTH = config.frame_width

class Energy(MovingCameraScene):
    def setup(self, add_border =True):
        if add_border:
            self.border = Rectangle(
                width=FRAME_WIDTH,
                height=FRAME_HEIGHT,
                    color = RED
            )
            self.border_1 = Rectangle(width=FRAME_WIDTH -1,
                height=FRAME_HEIGHT - 1,
                    color = YELLOW)
            self.add(self.border)
            self.add(self.border_1)
    def construct(self):
        self.camera.background_color = WHITE
        title = MarkupText('Qual bola tem mais energia?',font='Open Sans SemiBold', color=LOGO_BLACK, font_size=25)
        title.move_to([0.,3.5,0.0])

        arroba = Text('@thiagosilva.fisica', font='Open Sans SemiBold',color=BLACK,font_size=14)
        arroba.set_opacity(0.2)
        arroba.to_edge(3*DOWN)

        in_text =[
            Write(title), 
            Write(arroba),
        ]

        predio = Rectangle(height=3, width=0.4, color=BLACK)
        ground = Line([-2.0,0.0,0.0], [2.0,0.0,0.00], color= BLACK)

        bol1 = Circle(radius=0.2, color=PURE_BLUE, fill_opacity = 1)
        bol1.next_to(predio.get_center(), UP, buff=0)
      
        bol1_mass = Text('2 kg', font='Open Sans bold', color = WHITE, font_size = 12)
        bol1_mass.move_to(bol1.get_center())
        bol1_v = MathTex(r'0 m/s', color = LOGO_BLACK, font_size = 25)
        bol1_v.next_to(bol1.get_end(), UP, buff = 0.5)

        self.add(title,arroba, predio, ground,bol1, bol1_mass, bol1_v)
        