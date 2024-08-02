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

class ce(MovingCameraScene):
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
        title = MarkupText('Campo Elétrico',gradient=(RED, YELLOW), font='Sans', weight='NORMAL',font_size = 25)
        title.move_to([0.,3.8,0.])
        arroba = Text('@thiagosilva.fisica', font='Sans', weight='BOLD',font_size=14)
        arroba.set_opacity(0.2)
        arroba.to_edge(4*DOWN)
    
        q1 = LabeledDot('+', color = RED).set_sheen(-0.3, DR)
        q1.to_edge(3*UP + LEFT)

        q1s =Text('+', weight="BOLD",font='Sans',color=WHITE, font_size= 25).set_z_index(2)
        q1s.add_updater(
            lambda t: t.move_to(q1.get_center())
        )
        

        q2 = LabeledDot('+', color = BLUE).set_sheen(-0.3, DL)
        q2.to_edge(3*UP + RIGHT)

        q2s = Text('+', weight="BOLD",font='Sans',color=WHITE, font_size= 25).set_z_index(2)

        q2s.add_updater(
            lambda y: y.move_to(q2.get_center())
        )

        self.play(Write(title),Write(arroba),q1.animate.shift(3*DOWN + 0.5*RIGHT).scale(0.75), Write(q1s),  q2.animate.shift(3*DOWN + 0.5*LEFT).scale(0.75), Write(q2s))

        d = LabeledLine(start=q1.get_center(), end=q2.get_center(),label = MathTex(r'd', font_size = 25), label_position=0.5, font_size =18, label_frame=False)
        d.shift(0.5*DOWN)

        dv = Line(start=[0.,0.,0.], end=[0.,0.3,0.])
        dv.move_to(d.get_start())
        dv1= dv.copy()
        dv1.move_to(d.get_end())


        f_12= Arrow(start =q2.get_center(), end=q2.get_right() + 0.8*RIGHT, stroke_width= 5, max_tip_length_to_length_ratio=0.25,max_stroke_width_to_length_ratio=5,  color = RED, buff=0).set_z_index(-2)

        f_12_t = MathTex(r'\vec{F}', font_size=30, color=RED)
        f_12_t.next_to(f_12, UP, buff= 0.3)

        f_21 = Arrow(start =q1.get_center(), end=q1.get_left() + 0.8*LEFT, stroke_width= 5, max_tip_length_to_length_ratio=0.25,max_stroke_width_to_length_ratio=5,  color = BLUE, buff=0).set_z_index(-2)

        f_21_t = MathTex(r'\vec{F}', font_size=30, color=BLUE)
        f_21_t.next_to(f_21, UP, buff= 0.3)


        self.wait(3)

        self.play(Create(d), Create(dv), Create(dv1))
        self.wait(3)
        self.play(Create(f_12), Create(f_21), Write(f_12_t), Write(f_21_t))
        self.wait(4)
        
        #Criar q3 aqui, permite que ela já fique na posição final de q2
        q3 =q2.copy().set_color(YELLOW).set_sheen(-0.3, DL)
        q3.move_to(q2)
        q3s =Text('-', weight="BOLD",font='Sans',color=WHITE, font_size=25).set_z_index(2)
        q3s.add_updater(
            lambda u: u.move_to(q3.get_center())
        )

        f_31= Arrow(start =q1.get_center(), end=q1.get_right() + 0.8*RIGHT, stroke_width= 5, max_tip_length_to_length_ratio=0.25,max_stroke_width_to_length_ratio=5,  color = YELLOW, buff=0).set_z_index(-2)
        f_31_t = MathTex(r'\vec{F}', font_size=30, color=YELLOW)
        f_31_t.next_to(f_31, UP, buff= 0.3)
        
        f_13= Arrow(start =q3.get_center(), end=q3.get_left() + 0.8*LEFT, stroke_width= 5, max_tip_length_to_length_ratio=0.25,max_stroke_width_to_length_ratio=5,  color = RED, buff=0).set_z_index(-2)
        f_13_t = MathTex(r'\vec{F}', font_size=30, color=RED)
        f_13_t.next_to(f_13, UP, buff= 0.3)



        self.play(Transform(q2,q3), Transform(q2s, q3s), Transform(f_12,f_13), Transform(f_21, f_31), Transform(f_12_t,f_13_t), Transform(f_21_t, f_31_t))

        self.wait()

        cg =VGroup(q1,q1s, f_31, f_31_t, q3,q3s,f_13,f_13_t, d,dv,dv1)

        cg.generate_target()
        

        cg.target.shift(2*UP)

        eq = MathTex(r'F_E', r'=', r'k_0', r'\frac{Q_1.Q_2}{d^2}', font_size =28)

        rect = SurroundingRectangle(eq)

        eq_t = MathTex(r'\text{Lei de Coulomb}', font_size=28)

        self.remove(q2, q2s, f_12, f_21, f_12_t, f_21_t)
        self.play(MoveToTarget(cg), Write(eq), Create(rect))
        self.wait(0.1)

        eq.generate_target()
        eq.target.shift(1*DOWN)
        self.play(MoveToTarget(eq), rect.animate.shift(1*DOWN),Write(eq_t))
        self.wait(10)
        self.play(Unwrite(eq_t), FadeOut(eq, shift=1*UP), FadeOut(rect, SHIFT= 1*UP))

        cg.target.shift(2*DOWN)
        self.play(MoveToTarget(cg))
        self.wait()

        saídas =VGroup(f_31, f_31_t, q3,q3s,f_13,f_13_t, d,dv,dv1)
        q1.generate_target()
        q1.target.move_to([0.,0.,0.])
        self.play(FadeOut(saídas, shift=LEFT), MoveToTarget(q1))
        self.wait()

        q1n = Charge(2)
        q3n = Charge(-1)
        field = ElectricField(q1n)
        fieldn = ElectricField(q3n)
        
        e1 = MathTex(r'E',r'=', r'k_0', r'\frac{Q}{d^2}', font_size=28)


        self.remove(q1, q1s)
        self.play(Transform(q1, q1n))
        self.wait(3)
        self.play(Create(field))
        self.wait(5)
        self.play(Write(e1.shift(1.5*UP)), field.animate.set_opacity(0.3))
        self.wait(10)
        self.play(Uncreate(field), Unwrite(e1))
        self.remove(q1n)
        self.wait()
        self.play(Transform(q1n,q3n), Create(fieldn))
        self.wait(3)
        self.remove(q1n,q3n,fieldn)
        
        q1n = Charge(2, LEFT)
        q3n = Charge(-2,RIGHT)

        nf = ElectricField(q1n, q3n)
        self.remove(q1,q1s,q1n)
        self.play(Create(q1n), Create(q3n))
        self.play(Create(nf))
        self.wait(3)
        self.remove(nf)

        d = LabeledLine(start=q1n.get_center(), end=q3n.get_center(),label = MathTex(r'd', font_size = 25), label_position=0.5, font_size =18, label_frame=False)
        d.shift(0.5*DOWN)

        dv = Line(start=[0.,0.,0.], end=[0.,0.3,0.])
        dv.move_to(d.get_start())
        dv1= dv.copy()
        dv1.move_to(d.get_end())

        f_13= Arrow(start =q3n.get_center(), end=[0.,0.,0.], stroke_width= 5, max_tip_length_to_length_ratio=0.25,max_stroke_width_to_length_ratio=5,  color = RED, buff=0).set_z_index(-2)
        f_13_t = MathTex(r'\vec{F}', font_size=30, color=RED)
        f_13_t.next_to(f_13, UP, buff= 0.3)

        self.play(Create(d), Create(dv), Create(dv1), Create(f_13), Create(f_13_t))
        self.wait(5)
        self.remove(q1n,q3n)

        q1n = Charge(2, LEFT, add_glow=False)
        q3n = Charge(-2,RIGHT, add_glow=False)

        cg1 = VGroup(q1n,q3n,d,dv,dv1,f_13, f_13_t)

        cg1.generate_target()
        cg1.target.shift(1*UP).scale(0.7)

        eq1 = MathTex(r'\vec{F}_E', r'=', r'\vec{E}',r'(-Q)', font_size=28)
        eq1[2].set_color(RED)
        eq1[3].set_color(YELLOW)

        eq2 = MathTex(r'F_E', r'=', r'k_0 \frac{Q_1}{d^2}',r'Q_2', font_size=28)
        eq3 = MathTex(r'F_E', r'=', r'k_0 \frac{Q_1.Q_2}{d^2}', font_size=28)

        self.play(MoveToTarget(cg1), Write(eq1))
        self.wait(4)
        
        self.play(TransformMatchingTex(eq1,eq2))
        self.wait(2)
        self.play(TransformMatchingTex(eq2,eq3))
        self.wait(2)

        self.remove(cg1,eq1,eq2,eq3)
        call = Text('Me siga', font='Sans', weight='BOLD',font_size=14)
        call_1 = Text('para mais conteúdos de Física', font='Sans', weight='BOLD',font_size=14).next_to(call, DOWN, buff=0.5)
        call_2 = Text('@thiagosilva.fisica', font='Sans', weight='BOLD',font_size=14).next_to(call_1, DOWN, buff=0.5)
        self.play(FadeOut(title),Write(call), Write(call_1), Write(call_2))
        self.wait()



    