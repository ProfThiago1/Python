from manim import *

SCALE_FACTOR = 0.8

tmp_pixel_height = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = tmp_pixel_height

config.frame_height = config.frame_height/SCALE_FACTOR
config.frame_width = config.frame_height * 9/16

FRAME_HEIGHT = config.frame_height
FRAME_WIDTH = config.frame_width

class gn(Scene):
    def setup(self, add_border = False):
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
        text_title = MathTex(r" \text{O número de Ouro} \  \Phi ", tex_environment="align*", font_size = 35, color = GOLD)
        arroba = Text('@thiagosilva.fisica', font='Sans', weight='BOLD',font_size=14)
        arroba.set_opacity(0.2)
        arroba.to_edge(2*DOWN)
        self.play(Write(text_title), Write(arroba))
        self.wait()
        self.play(text_title.animate.move_to([0.,3.8,0.]))
        self.wait()

        a = Dot([-2,0.,0.]).set_z_index(2)
        c = Dot([0.5,0.,0]).set_z_index(2)
        b=  Dot([1.5,0.,0.]).set_z_index(2)

        dots = [
            Create(a),
            Create(c),
            Create(b)
        ]

        line_1 = Line(a.get_center(),c.get_center()).set_color(PURE_RED)
        line_2 = Line(c.get_center(),b.get_center()).set_color(PURE_RED)

        lines = [
            Create(line_1),
            Create(line_2)
        ]
        
        at = Text('A', font_size =18).next_to(a,UP, buff= 0.1)
        bt = Text('B', font_size =18).next_to(b,UP, buff= 0.1)
        ct = Text('C', font_size =18).next_to(c,UP, buff= 0.1)
        g1 = VGroup(a,b,c,at,bt,ct,line_1, line_2).move_to([0.,0.,0.])
       
        self.play(Create(g1))
    

        b1 =Brace(g1).next_to(g1, UP).rotate(PI)
        b1_text = b1.get_text('1').scale(0.7).next_to(g1, 2.5*UP)
       
        self.play(Create(b1), Create(b1_text))

        d_arrow = DoubleArrow(start =[-2.4,0.5,0.], end= [0.6,0.5,0],stroke_width=1.5, tip_length = 0.1).next_to(line_1,DOWN, buff=0.1)
        d_arrow2 = DoubleArrow(start =[0.5,0.5,0.], end= [2.,0.5,0],stroke_width=1.5, tip_length = 0.1).next_to(line_2,DOWN, buff=0.1)
       
        x = MathTex('x', font_size =30)
        x.next_to(d_arrow,DOWN, buff=0.05)
        m_x = MathTex('1-x', font_size=30)
        m_x.next_to(d_arrow2,DOWN, buff=0.05)
        self.play(Create(d_arrow),Create(d_arrow2), Write(x), Write(m_x))
        self.wait()

        g2 =VGroup(g1,d_arrow,d_arrow2,x,m_x)

        ab =MathTex('{AB \over AC}', '=' '{AC \over CB}', font_size=20).next_to(g2,DOWN, buff=0.5)
        self.play(Write(ab))
        self.wait(1)

        self.play(Uncreate(b1_text),Uncreate(b1), Unwrite(ab), g2.animate.move_to([0.,2.5,0.]))

        eq = MathTex('{1 \over x}','=' ,'{x \over 1-x}', font_size =30)
        eq_1 = MathTex('{1-x}', '=' , '{x^2}', font_size=30)
        eq_2 = MathTex('{x^2 + x -1}', '=' , '{0}', font_size=30)
        self.play(Write(eq))
        self.wait(0.5)
        self.play(TransformMatchingTex(eq,eq_1))
        self.wait(0.5)
        self.play(TransformMatchingTex(eq_1,eq_2))
        self.wait()

        result = MathTex(r'x' ,r'=' ,r'\frac{\sqrt{5} - 1}{2}', font_size = 30)
        r_1 = MathTex(r'\frac{1}{x}', r'=', r'\frac{1}{\frac{\sqrt{5} - 1}{2}}', font_size = 30)
        r_2 = MathTex(r'\frac{1}{x}', r'=', r'\frac{2(\sqrt{5} + 1 )}{(\sqrt{5} - 1)(\sqrt{5} + 1)}}', font_size = 30)
        r_3 = MathTex(r'\frac{1}{x}', r'=', r'\frac{1+ \sqrt{5}}{2}', font_size = 30)
        self.play(TransformMatchingTex(eq_2, result))
        self.wait()
        self.play(TransformMatchingTex(result,r_1))
        self.wait()
        self.play(TransformMatchingTex(r_1, r_2))
        self.wait()
        self.play(TransformMatchingTex(r_2, r_3))
        self.wait()

        phi = MathTex(r'\Phi', r'=', r'\frac{1+ \sqrt{5}}{2}', font_size = 30)
        self.play(TransformMatchingTex(r_3, phi))
        self.wait()

        p1 = MathTex(r'\Phi', r'=', r'1,618',font_size = 30).move_to([-1,0.5,0.])
        algarismos = ["0", "3", "3", "9", "8", "8", "7", "4", "9", "8", "9","4","8","4","8","2","0","4","5"]
        
        textos = [MathTex(algarismo, font_size= 30) for algarismo in algarismos]

        # Posicione o primeiro algarismo no centro da tela
        textos[0].next_to(p1[2], RIGHT, buff=0.07).shift(0.005*UP)

        # Adicione o primeiro algarismo à cena
        self.play(TransformMatchingTex( phi, p1),Write(textos[0]))

        # Para cada algarismo restante...
        for i in range(1, len(textos)):
            # Mova o algarismo para a posição do algarismo anterior
            textos[i].next_to(textos[i-1], RIGHT, buff = 0.07)

            # Crie uma animação que move o algarismo em uma espiral
            

            # Adicione o algarismo à cena com a animação
            self.play(Write(textos[i]), run_time = 0.05)
            fade_group = VGroup(*textos)
        call = Text('Me siga', font='Sans', weight='BOLD',font_size=14)
        call_1 = Text('para mais conteúdos de Matemática', font='Sans', weight='BOLD',font_size=14).next_to(call, DOWN, buff=0.5)
        call_2 = Text('@thiagosilva.fisica', font='Sans', weight='BOLD',font_size=14).next_to(call_1, DOWN, buff=0.5)
        self.play(FadeOut(fade_group),FadeOut(p1),Write(call), Write(call_1), Write(call_2))
        self.wait(2)