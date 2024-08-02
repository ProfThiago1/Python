from manim import *

class Qsm(Scene):
    CONFIG = {
        "camera_config": {
            "frame_height": 16,
            "frame_width": 9,
            "pixel_height": 1920,
            "pixel_width": 1080,
        }
    }
    def construct(self):
        tex_1 = Text('Quadrado da soma', color=YELLOW, font_size=30).to_edge(ORIGIN)
        tex_2 =MathTex(r'(a+b)^2 = a^2 + 2ab + b^2', font_size = 30)
        square_1 = Square().scale(0.10).next_to(tex_1, 1*UP, buff= 0.3).rotate(PI / 4)
        latex_text = MathTex(r'(1+2)^2= 1^2 + 2.1.2 + 2^2 = 9', font_size = 27)
        # Posiciona o texto no centro do retângulo
    

        self.play(Write(tex_2))
        self.wait(0.1)
        rect = SurroundingRectangle(tex_2, color=YELLOW, buff = SMALL_BUFF, stroke_width = 1)
        gp_1 = VGroup(tex_2, rect)

        self.play(Create(rect), gp_1.animate.shift(1.8*UP))
        self.wait(2)
        self.play( Write(latex_text))
        self.wait(5)
        self.play(Write(tex_1), Create(square_1), tex_1.animate.shift(UP*2.5), square_1.animate.shift(UP*2.5).next_to(latex_text, 1*RIGHT))
        self.play(Rotate(square_1, angle=PI))
        self.play(square_1.animate.rotate(-PI / 4))
        self.wait(0.3)
        self.play(square_1.animate.scale(0.3))  
        self.wait()
        self.play(ShrinkToCenter(square_1), ShrinkToCenter(latex_text))
        self.wait(0.2)
        saida_1 =[
            FadeOut(rect, shift =RIGHT),
            FadeOut(tex_2, shift =RIGHT),
            FadeOut(tex_1, shift =RIGHT)
        ]
        self.wait(8)
        self.play(AnimationGroup(*saida_1))

        line_1 = Line(start=[-1.,0.,0.], end = [1.,0.,0.])
        line_1.set_color(PURE_GREEN).set_opacity(0.8)
        line_2 =Line(start =[1.,0.,0.], end=[2.,0.,0.])
        line_2.set_color(YELLOW)
        line_3 = Line(start=[-1.,0.,0.], end = [-1.,-2.,0.])
        line_3.set_color(PURE_GREEN).set_opacity(0.8)
        line_4 =Line(start =[-1.,-2.,0.], end=[-1.,-3.,0.])
        line_4.set_color(YELLOW)
        tex_3 = Text ('a', font_size= 20).next_to(line_1, UP, buff=0.3)
        tex_4 = Text ('b', font_size= 20).next_to(line_2,UP, buff = 0.3)
        line_5 = Line(start=[-1.,-3.,0.], end = [1.,-3.,0.])
        line_5.set_color(PURE_GREEN).set_opacity(0.8)
        line_6 =Line(start =[1.,-3.,0.], end=[2.,-3.,0.])
        line_6.set_color(YELLOW)

        line_8 = Line(start=[2.,-2.,0.], end = [2.,0.,0.])
        line_8.set_color(PURE_GREEN).set_opacity(0.8)
        line_7 =Line(start =[2.,-3.,0.], end=[2.,-2.,0.])
        line_7.set_color(YELLOW)


        #Criação do grupo

        lines_and_texts = VGroup(line_1, line_2, tex_3, tex_4, line_3, line_4, line_5, line_6, line_7, line_8)
        lines_and_texts.next_to(tex_1, DOWN, buff=1)
        lines_right = VGroup(line_7, line_8)
        slines = VGroup (line_1, line_2, line_3,line_4, line_5, line_6, line_7, line_8)
        
        # Criar a brace acima do grupo
        brace_1 = Brace(lines_and_texts, UP, buff=SMALL_BUFF)
        brace_2 = Brace(lines_right, RIGHT, buff=0.08)
        brace_text_1 = brace_1.get_text(r"$a+b$").scale(0.7)
        brace_text_2 = brace_2.get_text(r"$a+b$").scale(0.7).rotate(-PI/2).next_to(brace_2, RIGHT,buff= 0.09)
        cs =[
            *list(map(Create, lines_and_texts)),

        ]
        
        self.play(AnimationGroup(*cs))
        self.wait(4)
        self.play(Create(brace_1), Create(brace_2),
            Write(brace_text_1), Write(brace_text_2),)
        self.wait(2)
        
        fade_braces =[
            FadeOut(brace_1),
            FadeOut(brace_text_1),
            FadeOut(brace_2),
            FadeOut(brace_text_2),
            FadeOut(tex_3),
            FadeOut(tex_4),
        ]
        self.play(AnimationGroup(*fade_braces))
        self.wait(3)
         #Retângulos e quadrados e alguns textos
        rect_1 = Rectangle(color=YELLOW, height=2.0, width=1.0).set_fill(color=YELLOW, opacity=0.7)
        rect_1.align_to(line_2, RIGHT).shift(DOWN*0.22)
        rect_2 = Rectangle(color=YELLOW, height=2.0, width=1.0)
        rect_2.align_to(line_4, RIGHT).shift(DOWN*1.7 + 1.5*RIGHT).set_fill(color=YELLOW, opacity=0.7).rotate(PI/2)
        square_2 = Rectangle(color=PURE_GREEN, width= 2, height=2).set_fill(PURE_GREEN).set_opacity(0.7)
        square_2.align_to(line_3,RIGHT).shift(0.21*DOWN + 2*RIGHT)
        square_3 = Rectangle(color=PURE_BLUE, width=1, height=1).set_opacity(0.6)
        square_3.align_to(line_7,LEFT).shift(1.71*DOWN + 1*LEFT)
        square_4 = Rectangle(color=YELLOW, width=1, height=1, fill_opacity = 0)
        square_4.align_to(line_7,LEFT).shift(1.71*DOWN + 1*LEFT)
        square_5 = Rectangle(width=3, height= 3, color=YELLOW).move_to(slines.get_center()).set_opacity(0.20)
        tex_5 = MathTex(r'A_T = (a+b)^2', font_size = 30).move_to(square_5.get_center())
       
       #linhas
        
        width_line_1 = Line(start=[-1.,-2.,0.], end = [1.,-2.,0.], color=PURE_GREEN).set_opacity(0.7).shift(0.8*UP + 0.5*LEFT)
        width_line_2 = Line(start=[-1.,-3.,0.], end = [1.,-3.,0.], color=PURE_GREEN).set_opacity(0.7).shift(0.8*UP + 0.5*LEFT)

        width_line_3 = Line(rect_1.get_corner(UR), rect_1.get_corner(DR), color=PURE_GREEN).set_opacity(0.7).align_to(rect_1, LEFT)
        width_line_4 = Line(rect_1.get_corner(UR), rect_1.get_corner(DR), color=PURE_GREEN).set_opacity(0.7).align_to(rect_1, RIGHT)
       
      

        #grupos gerais
       
        GG = VGroup(rect_1, rect_2, width_line_1, width_line_2, width_line_3, width_line_4, square_2, square_3, square_4, square_5)
        blink_animation = AnimationGroup(
            Flash(square_5, flash_radius=0.5, line_length=0.2, num_flashes=1),
            lag_ratio=0.5
        )
       
        slines.generate_target()
        GG.generate_target()
        
        
        #preenchimento 01 = área (a+b)^2
        self.play(Create(square_5), Write(tex_5),blink_animation)
        self.wait(8)
        self.play(ShrinkToCenter(tex_5),ShrinkToCenter(square_5))
        self.wait(4)
        
        #preenchimento 02: novas figuras
        self.play(Create(rect_2),Create(width_line_1), Create(width_line_2), Create(rect_1), Create(width_line_3), Create(width_line_4), Create(square_2), Create(square_3), Create(square_4))
        self.wait(2)

        #Subindo e descendo: mostrando encaixe
        self.play(slines.animate.shift(2*UP), GG.animate.shift(1.2*DOWN))
        self.wait(4)
        self.play(slines.animate.shift(2*DOWN), GG.animate.shift(1.2*UP))
        self.wait(2)

        #novos grupos (python e suas manias)
        rec_group_1 = VGroup(rect_1, width_line_3, width_line_4)
        rec_group_1.shift(1*LEFT)
        rec_group_2 = VGroup(rect_2, width_line_1, width_line_2)
        rec_group_2.rotate(-PI/2)
        

        brace_3 = Brace(square_2, UP, buff=SMALL_BUFF)
        brace_4 = Brace(square_2, RIGHT, buff=0.08)
        brace_text_3 = brace_3.get_text(r"$a$").scale(0.7)
        brace_text_4 = brace_4.get_text(r"$a$").scale(0.7).rotate(-PI/2).next_to(brace_4, RIGHT,buff= 0.09)

        brace_5 = Brace(rec_group_1, UP, buff=SMALL_BUFF)
        brace_6 = Brace(rec_group_1, RIGHT, buff=0.08)
        brace_text_5 = brace_5.get_text(r"$b$").scale(0.7)
        brace_text_6 = brace_6.get_text(r"$a$").scale(0.7).rotate(-PI/2).next_to(brace_6, RIGHT,buff= 0.09)

        brace_7 = Brace(rec_group_2, UP, buff=SMALL_BUFF)
        brace_8 = Brace(rec_group_2, RIGHT, buff=0.08)
        brace_text_7 = brace_7.get_text(r"$b$").scale(0.7)
        brace_text_8 = brace_8.get_text(r"$a$").scale(0.7).rotate(-PI/2).next_to(brace_8, RIGHT,buff= 0.09)

        brace_9 = Brace(square_3, UP, buff=SMALL_BUFF)
        brace_10 = Brace(square_3, RIGHT, buff=0.08)
        brace_text_9 = brace_9.get_text(r"$b$").scale(0.7)
        brace_text_10 = brace_10.get_text(r"$b$").scale(0.7).rotate(-PI/2).next_to(brace_10, RIGHT,buff= 0.09)
        
        braces_a =[
            Create(brace_3),
            Create(brace_4),
            Write(brace_text_3),
            Write(brace_text_4),
            Create(brace_5),
            Create(brace_6),
            Write(brace_text_5),
            Write(brace_text_6),
            Create(brace_7),
            Create(brace_8),
            Write(brace_text_7),
            Write(brace_text_8),
            Create(brace_9),
            Create(brace_10),
            Write(brace_text_9),
            Write(brace_text_10),
        ]
        fade_braces_1 =[
            FadeOut(brace_3),
            FadeOut(brace_4),
            FadeOut(brace_text_3),
            FadeOut(brace_text_4),
            FadeOut(brace_5),
            FadeOut(brace_6),
            FadeOut(brace_text_5),
            FadeOut(brace_text_6),
            FadeOut(brace_7),
            FadeOut(brace_8),
            FadeOut(brace_text_7),
            FadeOut(brace_text_8),
            FadeOut(brace_9),
            FadeOut(brace_10),
            FadeOut(brace_text_9),
            FadeOut(brace_text_10),
        ]
        tex_6 = MathTex(r"A_1 = a^2",r"A_2 = a.b",r"A_3 = a.b", r"A_4 = b^2", font_size = 30)
        text_a =[
        Write(tex_6[0].move_to(square_2.get_center())),
        Write(tex_6[1].move_to(rect_1.get_center())),
        Write(tex_6[2].move_to(rect_2.get_center())),
        Write(tex_6[3].move_to(square_3.get_center())),
        ]

        #Desaparecendo o quadrado em linhas e mostrando o Quadrado verde A_1
        self.play(FadeOut(slines, shift = UP),FadeOut(GG, shift =RIGHT))
        self.wait(0.1)
        self.play(square_2.animate.set_fill(color =PURE_GREEN, opacity = 0.6).align_to([0.,0.,0.]), Create(brace_3),
            Create(brace_4),
            Write(brace_text_3),
            Write(brace_text_4), Write(tex_6[0].move_to(square_2.get_center())))
        self.wait(3)
        #Desaparecendo o quadrado Quadrado verde A_1, mostrando o retângulo amarelo e sumindo
        self.play(FadeOut(square_2, shift= LEFT), FadeOut(brace_3),
            FadeOut(brace_4),
            FadeOut(brace_text_3),
            FadeOut(brace_text_4),tex_6[0].animate.move_to([-2,2.5,0.]).scale(0.8))
        self.wait(0.1)
        self.play(rec_group_1.animate,Write(tex_6[1].move_to(rect_1.get_center()).scale(0.7)),Create(brace_5),
            Create(brace_6),
            Write(brace_text_5),
            Write(brace_text_6), )
        self.wait(3)
        self.play(FadeOut(rec_group_1, shift =RIGHT),FadeOut(brace_5),
            FadeOut(brace_6),
            FadeOut(brace_text_5),
            FadeOut(brace_text_6),tex_6[1].animate.move_to([-1.,2.5,0]).scale(1.2) )
        #Próximo retâgulo amarelo e sumindo
        self.wait(0.1)
        self.play(rec_group_2.animate.shift(0.02*LEFT),Write(tex_6[2].move_to(rect_2.get_center()).scale(0.7)),Create(brace_7),
        Create(brace_8),
        Write(brace_text_7),
        Write(brace_text_8))
        self.wait(3)
        self.play(FadeOut(rec_group_2, shift =RIGHT),FadeOut(brace_7),
            FadeOut(brace_8),
            FadeOut(brace_text_7),
            FadeOut(brace_text_8),tex_6[2].animate.move_to([0.1,2.5,0]).scale(1.2) )
        self.wait(0.1)
        #Próximo Quadrado azul com borda amarela entrando e saindo
        
        self.play(square_3.animate, square_4.animate, Create(brace_9),
            Create(brace_10),
            Write(brace_text_9),
            Write(brace_text_10),Write(tex_6[3].move_to(square_3.get_center()).scale(0.7)),)
        self.wait(3)
        self.play(FadeOut(square_3, shift =RIGHT),FadeOut(square_4, shift= RIGHT),FadeOut(brace_9),
            FadeOut(brace_10),
            FadeOut(brace_text_9),
            FadeOut(brace_text_10),tex_6[3].animate.move_to([1.2,2.55,0]).scale(1.2) )
        self.wait(0.1)
        text_f = MathTex(r'A_T = A_1 + A_2 + A_3 + A_4', font_size = 30)
        self.play(FadeOut(tex_6[0]),FadeOut(tex_6[1]),FadeOut(tex_6[2]),FadeOut(tex_6[3]), Write(text_f))
        self.wait(0.1)

        rect_1 = Rectangle(color=YELLOW, height=2.0, width=1.0).set_fill(color=YELLOW, opacity=0.7)
        rect_1.align_to(line_2, RIGHT).shift(DOWN*0.22)
        rect_2 = Rectangle(color=YELLOW, height=2.0, width=1.0)
        rect_2.align_to(line_4, RIGHT).shift(DOWN*1.7 + 1.5*RIGHT).set_fill(color=YELLOW, opacity=0.7).rotate(PI/2)
        square_2 = Rectangle(color=PURE_GREEN, width= 2, height=2).set_fill(PURE_GREEN).set_opacity(0.7)
        square_2.align_to(line_3,RIGHT).shift(0.21*DOWN + 2*RIGHT)
        square_3 = Rectangle(color=PURE_BLUE, width=1, height=1).set_opacity(0.6)
        square_3.align_to(line_7,LEFT).shift(1.71*DOWN + 1*LEFT)
        square_4 = Rectangle(color=YELLOW, width=1, height=1, fill_opacity = 0)
        square_4.align_to(line_7,LEFT).shift(1.71*DOWN + 1*LEFT)
        square_5 = Rectangle(width=3, height= 3, color=YELLOW).move_to(slines.get_center()).set_opacity(0.20)
        tex_5 = MathTex(r'A_T = (a+b)^2', font_size = 30).move_to(square_5.get_center())
       
       #linhas
        
        width_line_1 = Line(start=[-1.,-2.,0.], end = [1.,-2.,0.], color=PURE_GREEN).set_opacity(0.7).shift(0.8*UP + 0.5*LEFT)
        width_line_2 = Line(start=[-1.,-3.,0.], end = [1.,-3.,0.], color=PURE_GREEN).set_opacity(0.7).shift(0.8*UP + 0.5*LEFT)

        width_line_3 = Line(rect_1.get_corner(UR), rect_1.get_corner(DR), color=PURE_GREEN).set_opacity(0.7).align_to(rect_1, LEFT)
        width_line_4 = Line(rect_1.get_corner(UR), rect_1.get_corner(DR), color=PURE_GREEN).set_opacity(0.7).align_to(rect_1, RIGHT)
        slines = VGroup (line_1, line_2, line_3,line_4, line_5, line_6, line_7, line_8)
        GG = VGroup(rect_1, rect_2, width_line_1, width_line_2, width_line_3, width_line_4, square_2, square_3, square_4, square_5)

        tex_7 = MathTex(r"A_1",r"A_2",r"A_3", r"A_4", font_size = 27)
        text_b =[
        Write(tex_7[0].move_to(square_2.get_center())),
        Write(tex_7[1].move_to(rect_1.get_center())),
        Write(tex_7[2].move_to(rect_2.get_center())),
        Write(tex_7[3].move_to(square_3.get_center())),
        ]
        text_bf =[
       FadeOut(tex_7[0].move_to(square_2.get_center())),
        FadeOut(tex_7[1].move_to(rect_1.get_center())),
        FadeOut(tex_7[2].move_to(rect_2.get_center())),
        FadeOut(tex_7[3].move_to(square_3.get_center())),
        ]
        text_f2 = MathTex(r'A_T = a^2 + a.b + a.b + b^2', font_size = 30)
        text_f3 = MathTex(r'A_T = a^2 + 2a.b + b^2', font_size = 30)
        text_f4 = MathTex(r'(a+b)^2 = a^2 + 2a.b + b^2', font_size = 30)
        self.play(text_f.animate.shift(2.5*UP), Create(slines), Create(GG), AnimationGroup(*text_b))
        self.wait(0.5)
        self.play(Write(text_f2.shift(2*UP)))
        self.play(Write(text_f3.shift(1.5*UP)))
        self.wait(2)
        self.play(AnimationGroup(*text_bf),FadeOut(slines),FadeOut(GG),FadeOut(text_f),FadeOut(text_f2),FadeOut(text_f3), Write(text_f4))
        self.wait()
        self.play(Uncreate(text_f4))
        self.wait(2)