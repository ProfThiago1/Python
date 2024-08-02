from manim import *

SCALE_FACTOR = 0.8

tmp_pixel_height = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = tmp_pixel_height

config.frame_height = config.frame_height/SCALE_FACTOR
config.frame_width = config.frame_height * 9/16

FRAME_HEIGHT = config.frame_height
FRAME_WIDTH = config.frame_width

class work(MovingCameraScene):
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
        
        title = MarkupText('Teorema Trabalho-Energia',color=BLACK, font_size=28)
        title.move_to([0.,3.5,0.0])


        arroba = Text('@thiagosilva.fisica', font='Open Sans SemiBold',color=BLACK,font_size=14)
        arroba.set_opacity(0.2)
        arroba.to_edge(3*DOWN)

        self.play(Write(title), Write(arroba))
        self.wait(0.5)


        bloco = Rectangle(height=1, width=1, color=ORANGE)
        bloco.set_fill(color=ORANGE, opacity=0.6).move_to([-1.50,0.0,0.0])

        text_m = Text('m', font_size= 25, color=WHITE).set_z_index(2)
        text_m.add_updater(lambda m: m.move_to(bloco.get_center()))
        bloco_path_c = TracedPath(bloco.get_center, dissipating_time=0.5, stroke_opacity=[0,1], stroke_color=BLACK)
        bloco_path_l1 = TracedPath(bloco.get_left, dissipating_time=0.5, stroke_opacity=[0,1], stroke_color=BLACK)

        force = Arrow(start = [0.0,0.0,0.0], end= [1.5,0.0,0.0], color = RED, stroke_width= 2, max_tip_length_to_length_ratio=0.2)
        force.add_updater(lambda b: b.next_to(bloco,LEFT,buff = 0))

        force_text = MathTex(r'\vec{F}', color = RED, font_size =27)
        force_text.add_updater(lambda t: t.next_to(force, UP, buff=0.2))


        line_d = Line(LEFT, [10.0,0.0,0.0], color = BLACK)
        line_d.to_edge(0.5*LEFT)
        line_d.next_to(bloco,DOWN, buff=0)

        desloc = LabeledLine(start=[-2.09,-0.2,0.0], end = [0.5,-0.2,0.0],label_frame=False, frame_fill_color=WHITE, label = MathTex(r'\vec{d}', color=BLACK, font_size= 27), color = BLACK, stroke_width = 1.5)

        up_bar = Line(start = [0.0,0.5,0.0], end =[0.0,0.7,0.0], color = BLACK,stroke_width = 1.5)
        up_bar.next_to(desloc,LEFT, buff=0)

        self.add(bloco, bloco_path_c, bloco_path_l1,text_m)

        self.play(Create(line_d.set_z_index(0)),Create(bloco), Create(force), Write(force_text))
        self.wait(0.5)
        self.play(bloco.animate.shift(2.5*RIGHT).set_z_index(2), Write(desloc),Create(up_bar))
        self.wait()

        eq = MathTex(r'W', r'=', r'F', r'.', r'd', color = BLACK, font_size = 27 )
        eq.move_to([0.0,-1.2,0.0])
        eq1 = MathTex(r'v^2', r'=', r'v^{2}_0', r'+', r'2.a.d', color = BLACK, font_size = 27 )
        eq1.next_to(eq, DOWN, buff = 1)
        eq2 =MathTex(r'\frac{v^2 - v^{2}_0}{2.a}', r'=', r'd',  color = BLACK, font_size = 27 )
        eq2.next_to(eq, DOWN, buff = 1)
        eq3 = MathTex(r'W', r'=', r'F', r'.', r'\left(\frac{v^2 - v^{2}_0}{2.a}\right)',  color = BLACK, font_size = 27 )
        eq3.next_to(eq, DOWN, buff = 1)

        eq4 = MathTex(r'W', r'=', r'm.a', r'.', r'\left(\frac{v^2 - v^{2}_0}{2.a}\right)',  color = BLACK, font_size = 27 )
        eq4.next_to(eq, DOWN, buff = 1)

        eq5 = MathTex(r'W', r'=',  r'\frac{m.v^2}{2}', r' - ', r'\frac{m.v^2_0}{2}' , color = BLACK, font_size = 27 )
        eq5.next_to(eq, DOWN, buff = 1)

        eq6 = MathTex(r'W', r'=',  r'\Delta E_c' , color = BLACK, font_size = 27 )
        eq6.next_to(eq, DOWN, buff = 1)

        rect = SurroundingRectangle(eq6, color = ORANGE)
        self.play(Write(eq))
        self.wait()
        
        self.play(Create(eq1))
        self.wait(0.5)
        self.remove(eq1)
        self.play(TransformMatchingTex(eq1,eq2))
        self.wait(0.5)
        self.remove(eq,eq1,eq2)
        self.play(TransformMatchingTex(eq2,eq3))
        self.wait(0.5)
        self.remove(eq,eq1,eq2,eq3)
        self.play(TransformMatchingTex(eq3,eq4))
        self.wait(0.5)
        self.remove(eq,eq1,eq2,eq4)
        self.play(TransformMatchingTex(eq4,eq5))
        self.wait(0.5)
        self.remove(eq,eq1,eq2,eq4,eq5)
        self.play(TransformMatchingTex(eq5,eq6), Create(rect))
        self.wait()
        


        '''call = Text('Me siga', font='Sans', weight='BOLD',font_size=14, color = BLACK)
        call_1 = Text('para mais conteúdos de Matemática', font='Sans', weight='BOLD',font_size=14, color = BLACK).next_to(call, DOWN, buff=0.5)
        call_2 = Text('@thiagosilva.fisica', font='Sans', weight='BOLD',font_size=14, color = BLACK).next_to(call_1, DOWN, buff=0.5)
        
        self.play(FadeOut(esf_a), Unwrite(eq1), Unwrite(title2),FadeOut(arroba),Write(call), Write(call_1), Write(call_2))
        self.wait()'''
