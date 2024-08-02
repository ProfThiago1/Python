from manim import *

SCALE_FACTOR = 0.8

tmp_pixel_height = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = tmp_pixel_height

config.frame_height = config.frame_height/SCALE_FACTOR
config.frame_width = config.frame_height * 9/16

FRAME_HEIGHT = config.frame_height
FRAME_WIDTH = config.frame_width

class lanch(MovingCameraScene):
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
        title = MarkupText('Lançamento Horizontal',gradient=(RED, YELLOW), font='Sans', weight='NORMAL',font_size = 30)
        title.move_to([0.,3.8,0.])

        self.play(Write(title))
        self.wait()
       
       #abelha
        abelha = SVGMobject('abelha.svg')
        abelha.scale(0.3)
        abelha.rotate(angle=PI/4.8)
        abelha.move_to([-2.0,0.0,0.0])
       
        bee_path = Line(start=[-1.0,0.0,0.0], end =[2.0,0.0,0.0])
        bee_path.rotate(PI/4)
        bee_path.move_to([-2.0,0.0,0.0])
        bee_path.set_opacity(0)

        self.add(abelha, bee_path)
        self.wait()
        bee_path1 = DashedLine(start=[-1.0,0.0,0.0], end =[2.0,0.0,0.0])
        bee_path1.rotate(PI/4)
        bee_path1.move_to([-2.0,0.0,0.0])
    

        self.play(MoveAlongPath(abelha, bee_path), Create(bee_path1),func_rate =linear)
        self.wait()

        v_bee = Arrow(start=[1.0,0.0,0.0],end=[2.5,0.0,0.0],stroke_width = 3,max_tip_length_to_length_ratio = 0.25,
    max_stroke_width_to_length_ratio = 5, color = PURE_RED)
        v_bee.rotate(angle=PI/4)
        v_bee.next_to(abelha.get_top(),buff=0).set_z_index(-1)
       

        self.play(Create(v_bee))

        self.wait()
        self.remove(bee_path)
        self.play(Uncreate(bee_path1))
        self.wait()

        v_bee1 = Arrow(start=[0.5,0.0,0.0],end=[1.5,0.0,0.0],stroke_width = 3,max_tip_length_to_length_ratio = 0.25,
    max_stroke_width_to_length_ratio = 5, color = BLUE)
    
        v_bee1.next_to(abelha.get_top(),buff=0).set_z_index(-1)


        self.play(Create(v_bee1))
        self.wait()



        # Parâmetros e equações (unidades no SI/10)
        g = 0.98 
        v_0 = 0.5
        H_p= [-2.0,3.0,0.0]
        t_q = (2*3/g)**(1/2)
        D = v_0*t_q

        #atores
        ball = Dot (radius=0.15, color=RED)
        ball.set_sheen(0.5)
        ball.next_to(H_p, RIGHT, buff=0.01)

        altura  = Line(H_p, end = [-2.0,0.0,0.0] )
        altura1 = Line(start=[2.0,3.0,0.0], end = [2.0,0.0,0.0] )

        ball1 = Dot (radius=0.15, color=YELLOW)
        ball1.set_sheen(0.5)
        ball1.next_to(altura1, LEFT, buff=0.01)



        path = ParametricFunction(lambda t: np.array([
            v_0*t, 3.0 -0.5*g*t**2,0
        ]), t_range=[0,t_q])
       
        path.shift(1.8*LEFT)
        path.set_opacity(0)


        self.play(Create(ball), Create(altura))
        self.wait()
        self.play(Create(path))

        path1 =  DashedVMobject(ParametricFunction(lambda t: np.array([
            v_0*t, 3.0 -0.5*g*t**2,0
        ]), t_range=[0,t_q]))
        path1.shift(1.8*LEFT)

        #primeiro lançamento
        self.play(MoveAlongPath(ball, path), Create(path1),run_time = t_q)
        
