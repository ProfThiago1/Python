from manim import *
SCALE_FACTOR = 0.8

tmp_pixel_height = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = tmp_pixel_height

config.frame_height = config.frame_height/SCALE_FACTOR
config.frame_width = config.frame_height * 9/16

FRAME_HEIGHT = config.frame_height
FRAME_WIDTH = config.frame_width

class moeda(MovingCameraScene):
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
        title = MarkupText('Probabilidade',gradient=(RED, YELLOW), font='Sans', weight='NORMAL',font_size = 25)
        title.move_to([0.,3.8,0.])
        pgeo = MarkupText('Probabilidade Geométrica',gradient=(RED, YELLOW), font='Sans', weight='NORMAL',font_size = 20)
        pgeo.move_to([0.,3.8,0.])
    
        arroba = Text('@thiagosilva.fisica', font='Sans', weight='BOLD',font_size=14)
        arroba.set_opacity(0.2)
        arroba.to_edge(4*DOWN)
        moeda = Circle(radius=0.5, color = YELLOW)
        moeda.set_fill(color=YELLOW, opacity=1)
        moeda.shift(UP*2.3)
        m_text = always_redraw(lambda : Text('C', font_size= 25).move_to(moeda.get_center()).set_color(BLACK))
        
        self.play(Write(title),Write(arroba))
        self.wait(5)
        self.play(Create(moeda),Create(m_text))
        self.wait(0.1)
        self.play(moeda.animate.shift(DOWN*1).rotate_about_origin(PI, axis=UP), m_text.animate.rotate_about_origin(2*PI, axis=UP))
        self.wait(2)

        mg1 = VGroup(moeda, m_text)

        m1 = Circle(radius=0.3, color = YELLOW)
        m1.set_fill(color=YELLOW, opacity=1)
        m1.shift(LEFT)
        m_text1 =  Text('K', font_size= 20).move_to(m1.get_center()).set_color(BLACK)
        m2 = Circle(radius=0.3, color = YELLOW)
        m2.set_fill(color=YELLOW, opacity=1)
        m2.shift(RIGHT)
        m_text2 =  Text('C', font_size= 20).move_to(m2.get_center()).set_color(BLACK)

        mg2 = VGroup(m1,m2,m_text1, m_text2)
        mg2.next_to(mg1, DOWN, buff=0.5)
        
        s1 = Arrow(moeda.get_bottom(), m1.get_top())
        s2 = Arrow(moeda.get_bottom(), m2.get_top())
    
        self.play(Create(mg2),Create(s1), Create(s2))
        self.wait(4)

        pr1 = MathTex(r'P(C)', r'=', r' \frac{\text{Casos favoráveis}}{\text{Casos possíveis}}', tex_environment="align*", font_size= 30)
        pr1.next_to(mg2,DOWN, buff=0.5)
        pr2 = MathTex(r'P(C)', r'=', r'\frac{1}{2}', font_size= 30).next_to(mg2,DOWN, buff=0.5)
        pr3 = MathTex(r'P(C)', r'=', r'50 \%', font_size= 30).next_to(mg2,DOWN, buff=0.5)

        self.play(Write(pr1))
        self.wait(3)
        self.play(TransformMatchingTex(pr1,pr2))
        self.wait(2)
        self.play(TransformMatchingTex(pr2,pr3))
        self.wait(4)
        self.play(Unwrite(pr3), Uncreate(mg1), Uncreate(mg2), Uncreate(s1),Uncreate(s2))
        self.wait()
        
    
        circ = Circle(radius=1, color= YELLOW)
        circ.set_fill(color=YELLOW, opacity=1)

        y = Line(circ.get_bottom(), circ.get_top())
        x = Line(circ.get_left(), circ.get_right())

        p =Dot(radius=0.09).set_color(PURE_RED)
        p.next_to(circ.get_right()+0.4*UP, buff= -0.5)

        

        self.play(Create(circ),Create(p),Create(x), Create(y))
        self.wait(0.1)
        rotations = 4
        self.play(Rotate(p,angle=rotations*2*PI, about_point=circ.get_center()),rate_func=linear, run_time = 4)
        mg3 = VGroup(p,circ,x, y)
        self.wait(3)
        self.play(Uncreate(mg3), Transform(title, pgeo))
        self.wait(0.3)

        ra = Ellipse(width=4.0, height=2, color=YELLOW)
        ra.set_fill(color=YELLOW, opacity=1)
        rb = Ellipse(width=2, height=1, color=PURE_RED)
        rb.move_to(ra.get_center())
        rb.set_fill(color=PURE_RED, opacity=1)
        original_width = rb.width
        original_height = rb.height

        self.play(Create(ra), Create(rb))
        self.wait(10)
        self.play(rb.animate.scale_to_fit_width(ra.width), run_time =3)
        self.play(rb.animate.scale_to_fit_height(ra.height), run_time =3)

        mg4 = VGroup(ra,rb)
        mg4.generate_target()
        mg4.target.shift(1.7*UP)
        # Espere por mais 10 segundos
        self.wait(5)
        p1 = MathTex(r'P',r'(',r'A', r')', r'\propto', r'A', font_size = 30)
        p1[2].set_color(PURE_RED)
        p1[5].set_color(PURE_RED)

        self.play(MoveToTarget(mg4))
        self.wait(0.1)
       

        self.play(Write(p1))
        self.wait(0.1)
        self.play(rb.animate.scale_to_fit_width(original_width))
        self.play(rb.animate.scale_to_fit_height(original_height))
        self.wait(0.1)
        
        aa = MathTex(r'A',font_size = 30)
        aa.set_color(YELLOW)
        aa.next_to(ra, UP, buff= 0.5)

        av = MathTex(r'A',font_size = 30)
        av.set_color(PURE_RED)
        av.next_to(rb, UP, buff= 0.06)
        self.play(Write(aa), Write(av))
        self.wait(4)
        p2 =  MathTex(r'P',r'(',r'A', r')', r'=', r'\underline{A}',font_size = 30)
        p3= MathTex(r'A',font_size = 30)
        p2[2].set_color(PURE_RED)
        p2[5].set_color(PURE_RED)
        p3[0].set_color(YELLOW)
        p3.next_to(p2[5], DOWN, buff=0.1)
        self.play(TransformMatchingTex(p1,p2), Write(p3))
        self.wait(4)

        mg5 = VGroup(mg4,p2,p3,aa,av)
        self.play(FadeOut(mg5))
        self.wait()

        
        circ = Circle(radius=1, color= YELLOW)
        circ.set_fill(color=YELLOW, opacity=1)

        y = Line(circ.get_bottom(), circ.get_top())
        x = Line(circ.get_left(), circ.get_right())
        p =Dot(radius=0.09).set_color(PURE_RED)
        p.next_to(circ.get_right()+0.4*UP, buff= -0.5)
        
        quad = Sector(outer_radius=1, inner_radius=0, start_angle=0, angle=PI/2, color=PURE_RED)
        quad.set_fill(color=PURE_RED, opacity=1)

        quad.generate_target()
        quad.target.shift(1.4*UP + 1*RIGHT).scale(0.8)

        circ.generate_target()
        circ.target.shift(1.4*UP + 1*LEFT).scale(0.8)

        self.play(Create(circ), Create(x), Create(y), Create(p))
        self.wait(3)

        self.play(Uncreate(x), Uncreate(y), Uncreate(p))
        self.play(MoveToTarget(circ), MoveToTarget(quad))
        self.play(Rotate(quad, PI/4))
        self.wait()
        Aa = MathTex(r'A', r'=', r'\pi r^2', font_size=30)
        Aa[0].set_color(YELLOW)
        Aa.next_to(circ, DOWN, buff=0.3)
        Av = MathTex(r'A', r'=', r'\frac{\pi r^2}{4}', font_size=30)
        Av[0].set_color(PURE_RED)
        Av.next_to(quad, DOWN, buff=0.3)

        self.play(Write(Aa), Write(Av))
        self.wait()

        p4 = MathTex(r'P', r'(', r'A', r')', r'=',r'\frac{\frac{\pi r^2}{4}}{\pi r^2}', font_size=30)
        p4[2].set_color(PURE_RED)
        p4.shift(1*DOWN)

        p5 = MathTex(r'P', r'(', r'A', r')', r'=',r'\frac{1}{4}', font_size=30)
        p5.shift(1*DOWN)
        p6 =MathTex(r'P', r'(', r'A', r')', r'=',r'25 \%', font_size=30)
        p6.shift(1*DOWN)
        self.play(Write(p4))
        self.wait()
        self.play(TransformMatchingTex(p4,p5))
        self.wait()
        self.play(TransformMatchingTex(p5,p6))
        self.wait()

        mg6 = VGroup(p6,circ,quad,Aa, Av)
        self.play(FadeOut(mg6),  FadeOut(pgeo), FadeOut(arroba))
        call = Text('Me siga', font='Sans', weight='BOLD',font_size=14)
        call_1 = Text('para mais conteúdos de Matemática', font='Sans', weight='BOLD',font_size=14).next_to(call, DOWN, buff=0.5)
        call_2 = Text('@thiagosilva.fisica', font='Sans', weight='BOLD',font_size=14).next_to(call_1, DOWN, buff=0.5)
        self.play(Write(call), Write(call_1), Write(call_2))

        self.wait(2)
