from manim import *
from eletrostatic import *
SCALE_FACTOR = 0.8

tmp_pixel_height = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = tmp_pixel_height

config.frame_height = config.frame_height/SCALE_FACTOR
config.frame_width = config.frame_height * 9/16

FRAME_HEIGHT = config.frame_height
FRAME_WIDTH = config.frame_width

class waves(MovingCameraScene):
    def setup(self, add_border =False):
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
        self.camera.background_color = WHITE
        background = Rectangle(width=FRAME_WIDTH,height=FRAME_HEIGHT,
                    color = WHITE)
        background.set_fill(color=WHITE, opacity=1)
        title = MarkupText('Ondas',color=BLACK)
        title.move_to([0.,3.8,0.])
        arroba = Text('@thiagosilva.fisica', font='Open Sans SemiBold',color=BLACK,font_size=14)
        arroba.set_opacity(0.2)
        arroba.to_edge(3*DOWN)

         # Parâmetros da onda
        A = 1  # Amplitude
        k = 1  # Número de onda
        w = 20  # Frequência angular

        # Função da onda
        def onda(x, t):
            return A * np.sin(k * x - w * t)

        tempo = ValueTracker(0)

        # Criar o objeto da onda
        onda_obj = ParametricFunction(
            lambda t: np.array([t, onda(t, tempo.get_value()), 0]),
            t_range=[-PI,2*PI], color=PURE_BLUE
        )

        # Animação da onda
        def animar_onda(mob, dt):
            mob.become(
                ParametricFunction(
                    lambda t: np.array([t, onda(t, tempo.get_value()), 0]),
                    t_range=[-PI,2*PI], color=PURE_BLUE
                )
            )
    
        self.play(Write(title), Write(arroba))
        self.wait()
    


        eq = MathTex(r'\nabla^2 y =\frac{1}{c^2} \frac{\partial^2y }{\partial t^2}',color=BLACK,font_size =25)
        eq.next_to(title, 2*DOWN)

        eq1 = MathTex(r'y(x,t) =', r'y_m.', r'sin',r'(',r'k.x - \omega.t'r')',color=BLACK,font_size =25)
        eq1.next_to(title, 2*DOWN)


        onda_obj.add_updater(animar_onda)
        

        self.play(Create(onda_obj))
    
        self.play(ChangeSpeed(tempo.animate.set_value(2), speedinfo={0:0.08, 1:0.08}, rate_func=linear), Write(eq))
        self.wait()
        onda_obj.remove_updater(animar_onda)

        self.remove(eq)
        self.play(Transform(eq,eq1))
        
        A = 2  
        k = 2
        w = 20
        def onda(x, t):
            return A * np.sin(k * x - w * t)
        
        wave = ParametricFunction(
            lambda x: np.array([x, onda(x, tempo.get_value()), 0]),
            t_range=[-2*PI,2*PI], color=PURE_BLUE
        )
    
        wave.scale(0.3)
        

        x_eixo = Arrow(start =[-1.5,0.0,0.0], end = [3.0,0.0,0.0], stroke_width=3, max_tip_length_to_length_ratio=0.070, color = BLACK)

        x_eixo_t = Text('x', font_size=18, color = BLACK)
        x_eixo_t.next_to(x_eixo.get_end(), DOWN)
        y_eixo = Arrow(start =[0.0,-1.5,0.0], end = [0.0,2.0,0.0], stroke_width=3, max_tip_length_to_length_ratio=0.09, color = BLACK)
        y_eixo_t = Text('y', font_size=18, color = BLACK)
        y_eixo_t.next_to(y_eixo.get_end(), RIGHT)

        eixos = VGroup(x_eixo, x_eixo_t, y_eixo, y_eixo_t)
        eixos.shift(1*LEFT)
        wave.shift(0.5*LEFT)
        
        v = Arrow(start=[0.5,0.0,0.0], end = [1.7,0.0,0.0], stroke_width=2, max_tip_length_to_length_ratio=0.2, color = RED)
        v.next_to(wave, UP, buff= 0.3)
        v.shift(0.3*RIGHT)
        vt = MathTex(r'\vec{v}', color = BLACK, font_size =23)
        vt.next_to(v, UP, buff =0.3)


        self.play(Uncreate(onda_obj),Create(wave),tempo.animate.set_value(1), Create(eixos), Create(v), Write(vt))
        self.wait(3)
        self.play(Indicate(eq1[4], color = PURE_BLUE))
        self.wait(0.5)
        self.remove(eq,eq1,eq1[4])

        posicao_original = self.camera.frame.get_center()
        update_func = lambda m, dt: m.move_to(wave)
        self.camera.frame.add_updater(update_func)

        comprimento = LabeledLine(start=[0.0,0.0,0.0], end = [1.0,0.0,0.0],label= MathTex(r'\lambda', font_size=25, color =BLACK), label_color=BLACK, label_frame=False, frame_fill_color=WHITE, color=BLACK)

        comprimento.next_to(wave, UP, buff= 0.3)
        comprimento.shift(1.1*RIGHT)

        self.play(self.camera.frame.animate.scale(0.8).move_to(wave),Create(comprimento), v.animate.set_opacity(0), vt.animate.set_opacity(0))







        eq2 = MathTex(r'k.x - w.t = c.t.e',color=BLACK,font_size =25)
        eq2.next_to(title, 2*DOWN)

        eq3 = MathTex(r'\frac{d(k.x - w.t)}{dt}= \frac{d (c.t.e)}{dt}',color=BLACK,font_size =25)
        eq3.next_to(title, 2*DOWN)

        eq4 =  MathTex(r'v= \frac{\omega}{k}',color=BLACK,font_size =25)
        eq4.next_to(title, 2*DOWN)

        eq5 = MathTex(r'v= \frac{2\pi f}{\frac{2\pi}{\lambda}}',color=BLACK,font_size =25)
        eq5.next_to(title, 2*DOWN)

        eq6 = MathTex(r'v= \lambda . f',color=BLACK,font_size =25)
        eq6.next_to(title, 2*DOWN)

        rect = SurroundingRectangle(eq6, color= BLUE)
        self.remove(eq,eq1,eq1[4])
        '''self.play(Write(eq2))
        self.wait()
        self.remove(eq2)
        self.play(TransformMatchingTex(eq2,eq3))
        self.wait(2)
        self.remove(eq2, eq3)
        self.play(TransformMatchingTex(eq3,eq4))
        self.wait(2)
        self.remove(eq2,eq3, eq4)
        self.play(TransformMatchingTex(eq4,eq5))
        self.wait(3)
        self.remove(eq2,eq3, eq4, eq5)
        self.play(TransformMatchingTex(eq5,eq6), Create(rect))
        self.wait(3)

        self.play(Unwrite(vt), Uncreate(v), Uncreate(wave), Uncreate(eixos))
        call = Text('Me siga', font='Sans', weight='BOLD',font_size=14, color = BLACK)
        call_1 = Text('para mais conteúdos de Física', font='Sans', weight='BOLD',font_size=14, color = BLACK).next_to(call, DOWN, buff=0.5)
        call_2 = Text('@thiagosilva.fisica', font='Sans', weight='BOLD',font_size=14, color = BLACK).next_to(call_1, DOWN, buff=0.5)
        self.play(FadeOut(title),FadeOut(arroba),Write(call), Write(call_1), Write(call_2), Uncreate(rect), Unwrite(eq6))'''
        self.wait()
