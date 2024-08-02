from manim import *

class UnrollingArc(ParametricFunction):
    def __init__(self, arc_range, radius=1, **kwargs):
        self.arc_range = arc_range
        self.radius = radius
        super().__init__(self.func, t_range=[0, 1], **kwargs)

    def func(self, t):
        angle = interpolate(self.arc_range[0], self.arc_range[1], t)
        return self.radius * np.array([np.cos(angle), np.sin(angle), 0])

class UnrollingArcScene(Scene):
    def construct(self):
        # Definir o raio desejado
        radius = 2

        circle = Circle(radius=radius, color=YELLOW)
        circle.set_fill(color=YELLOW, opacity=0.6)
        
        r = Line(circle.get_center(), circle.get_bottom(), color = WHITE)
        r_text = MathTex(r'r', font_size = 35)
        a_text_i = Text('Área = ?', font_size = 30)
        a_text_i.next_to(circle, 0.5*UP)
        r_text.next_to(r, 1*UP)

    
        # Criar o primeiro arco
        arc1 = UnrollingArc(arc_range=[-PI/2, -3*PI/2], radius=radius, color=YELLOW)
        
        # Criar o segundo arco
        arc2 = UnrollingArc(arc_range=[-PI/2, PI/2], radius=radius, color=YELLOW)

        self.play(Create(circle))
        self.play(Create(r), Write(r_text), Write(a_text_i))
        self.wait(0.1)
        # Adicionar ambos os arcos à cena
        self.play(Create(arc1), Create(arc2))
        self.wait(1)

        # Desenrolar ambos os arcos ao mesmo tempo
        line1 = Line(arc1.get_start(), arc1.get_end(), color = YELLOW)
        line2 = Line(arc2.get_start(), arc2.get_end(), color = YELLOW)
        

        self.play(Transform(arc1, line1.rotate(PI/2, about_point=line1.get_start())),
                  Transform(arc2, line2.rotate(-PI/2, about_point=line2.get_start())),
          a_text_i.animate.shift(1*LEFT + 1.2*UP))
        
        group_lines = VGroup(line1, line2)
        brace = Brace(group_lines, DOWN, buff = 0.2)
        brace_text = brace.get_text(r"$2\pi r$").scale(0.7)
        self.wait(0.1)
        self.play(Create(brace), Write(brace_text))
        self.wait(1)
        self.add(circle)
        self.play(Uncreate(circle))
        self.wait(0.1)
        
        #loop
        for i in np.arange(radius, 0, -0.01)[::-1]:
            n_circle = Circle(radius= (radius - i), color=YELLOW)
            n_circle.set_fill(color=YELLOW, opacity=0.6)
            
            n_arc1 = UnrollingArc(arc_range=[-PI/2, -3*PI/2], radius=(radius - i), color=YELLOW)
            n_arc2 = UnrollingArc(arc_range=[-PI/2, PI/2], radius=(radius - i), color=YELLOW)
          
            self.add(n_circle)
            self.play(Create(n_arc1), Create(n_arc2))
            self.wait(0.01)

            n_line1 = Line(n_arc1.get_start(), n_arc1.get_end(), color = YELLOW)
            n_line2 = Line(n_arc2.get_start(), n_arc2.get_end(), color = YELLOW)
            
            
        
            self.play(Transform(n_arc1, n_line1.rotate(PI/2, about_point=n_line1.get_start())), Transform(n_arc2, n_line2.rotate(-PI/2, about_point=n_line2.get_start())),n_line1.animate.move_to(n_arc1, DOWN),
            n_line2.animate.move_to(n_arc2, DOWN))
            
            self.remove(n_circle)
            self.wait(0.01)
        self.wait()

        a_text_f_2 = MathTex(r'A =', r'\frac{1}{2} (2 . \pi . r). r', r'\frac{1}{2} 2 . \pi .r^2', r'\pi r^2', font_size = 30)

        a_text_f_3 = MathTex(r'A = \pi r^2', font_size =30)

        self.play(Create(r.set_z_index(2)), r_text.animate.next_to(r, LEFT, buff = 0.2).set_z_index(2), Unwrite(a_text_i), Write(a_text_f_2[0].shift(0.9*UP)),Write(a_text_f_2[1].next_to(a_text_f_2[0], RIGHT)) )
        self.wait(0.1)
        a_text_f_2[2].move_to(a_text_f_2[1])
        self.play(ReplacementTransform(a_text_f_2[1],a_text_f_2[2]))
        self.wait(0.1)
        a_text_f_2[3].move_to(a_text_f_2[2])
        self.play(ReplacementTransform(a_text_f_2[2], a_text_f_2[3]))
        self.wait(0.1)
        a_text_f_3.move_to([0.,1.1,0.])
        rect = SurroundingRectangle(a_text_f_3, color=YELLOW, buff = SMALL_BUFF, stroke_width = 1)
        self.play(FadeOut(a_text_f_2), Write(a_text_f_3))
        self.wait(0.1)
        self.play(Create(a_text_f_3), Create(rect))
        self.wait(3)