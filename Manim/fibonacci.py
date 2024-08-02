from manim import *
SCALE_FACTOR = 0.8

tmp_pixel_height = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = tmp_pixel_height

config.frame_height = config.frame_height/SCALE_FACTOR
config.frame_width = config.frame_height * 9/16

FRAME_HEIGHT = config.frame_height
FRAME_WIDTH = config.frame_width

class Fibonacci(MovingCameraScene):
    def setup(self, add_border =True):
        if add_border:
            self.border = Rectangle(
                width=FRAME_WIDTH,
                height=FRAME_HEIGHT,
                    color = WHITE
            )
            self.border_1 = Rectangle(width=FRAME_WIDTH -1,
                height=FRAME_HEIGHT - 1,
                    color = YELLOW)
            self.add(self.border)
            self.add(self.border_1)
    def construct(self):
        # Definir a sequência de Fibonacci
        fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        q_0 = Square(side_length=fibonacci_sequence[0])
        q_1 = Square(side_length= fibonacci_sequence[1])
        q_2 = Square(side_length=fibonacci_sequence[2])
        q_2.next_to(q_1, UP, buff=0)
        q_3 = Square(side_length=fibonacci_sequence[3])
        q_4 = Square(side_length=fibonacci_sequence[4])
        q_5 = Square(side_length=fibonacci_sequence[5])
        q_6 = Square(side_length=fibonacci_sequence[6])
        q_7 = Square(side_length=fibonacci_sequence[7])
        q_8 = Square(side_length=fibonacci_sequence[8])
        q_9 = Square(side_length=fibonacci_sequence[9])
        

        qs = [q_0,q_1, q_2, q_3, q_4, q_5, q_6, q_7, q_8, q_9]




        a1 = ArcBetweenPoints(start=qs[1].get_corner(DL), end=qs[1].get_corner(UR), color = BLUE)
        a2 = ArcBetweenPoints(start=qs[2].get_corner(DR), end=qs[2].get_corner(UL), color = BLUE)

        self.play(Create(qs[0]))
        posicao_original = self.camera.frame.get_center()
        self.wait(0.1)
        self.play(Create(qs[1]), Create(a1))
        self.wait(0.0001)
        self.play(Create(qs[2]), Create(a2))
       
        qg_1 = VGroup(qs[1],qs[2])
        qs[3].next_to(qg_1,LEFT, buff =0)
        a3 = ArcBetweenPoints(start=qs[2].get_corner(UL), end=qs[3].get_corner(DL), color = BLUE)
        self.wait(0.0001)
        self.play(Create(qs[3]), Create(a3), self.camera.frame.animate.scale(1.5).move_to(qs[3]))
       
        qg_2 = VGroup(qg_1,qs[3])
        qs[4].next_to(qg_2,DOWN, buff=0)
        a4 = ArcBetweenPoints(start=qs[3].get_corner(DL), end=qs[4].get_corner(DR), color = BLUE)

        self.wait(0.0001)
        self.play(Create(qs[4]), Create(a4), self.camera.frame.animate.scale(1.2).move_to(qs[4]))
       
       
        qg_3 = VGroup(qg_2,qs[4])
        qs[5].next_to(qg_3,RIGHT,buff=0)
        a5 = ArcBetweenPoints(start=qs[4].get_corner(DR), end=qs[5].get_corner(UR), color = BLUE)
        

        self.wait(0.0001)
        self.play(Create(qs[5]), Create(a5),self.camera.frame.animate.scale(1.2).move_to(qs[5]))
        
        
        qg_4 = VGroup(qg_3,qs[5])
        qs[6].next_to(qg_4,UP, buff=0)
        a6 = ArcBetweenPoints(start=qs[5].get_corner(UR), end=qs[6].get_corner(UL), color = BLUE)
        self.wait(0.0001)
        self.play(Create(qs[6]), Create(a6),self.camera.frame.animate.scale(1.5).move_to(qs[6]))
        
        
        qg_5 =VGroup(qg_4,qs[6])
        qs[7].next_to(qg_5,LEFT,buff=0)
        a7 = ArcBetweenPoints(start=qs[6].get_corner(UL), end=qs[7].get_corner(DL), color = BLUE)
        self.wait(0.0001)
        self.play(Create(qs[7]),Create(a7), self.camera.frame.animate.scale(1.3).move_to(qs[7].get_center()))
        
        
        qg_6 =VGroup(qg_5,qs[7])
        qs[8].next_to(qg_6,DOWN,buff=0)
        a8 = ArcBetweenPoints(start=qs[8].get_corner(UL), end=qs[8].get_corner(DR), color = BLUE)
        self.wait(0.0001)
        self.play(Create(qs[8]),Create(a8), self.camera.frame.animate.scale(1.5).move_to(qs[8]))
        
        
        qg_7 = VGroup(qg_6,qs[8])
        qs[9].next_to(qg_7,RIGHT,buff=0)
        a9 = ArcBetweenPoints(start=qs[8].get_corner(DR), end=qs[9].get_corner(UR), color = BLUE)
        self.wait(0.0001)
        self.play(Create(qs[9]), Create(a9),self.camera.frame.animate.scale(2.5).move_to(posicao_original))
        qg_8 = VGroup(qg_7,qs[9])
        self.wait(0.0001)
        self.play(self.camera.frame.animate.scale(0.8).move_to(qg_8))
        self.wait()
       

        self.wait()



          
       


