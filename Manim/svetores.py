from manim import *


SCALE_FACTOR = 0.8

tmp_pixel_height = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = tmp_pixel_height

config.frame_height = config.frame_height/SCALE_FACTOR
config.frame_width = config.frame_height * 9/16

FRAME_HEIGHT = config.frame_height
FRAME_WIDTH = config.frame_width

#NEM SEMPRE 1+1 =2

class sv(Scene):
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
         title = MarkupText('1+1=2?',gradient=(RED, YELLOW), font='Sans', weight='NORMAL',font_size = 30)
         title.move_to([0.,3.8,0.])
         title2 = MarkupText('Soma usual',gradient=(RED, YELLOW), font='Sans', weight='NORMAL',font_size = 30)
         title2.move_to([0.,3.8,0.])
         title3 = MarkupText('Soma escalar',gradient=(RED, YELLOW), font='Sans', weight='NORMAL',font_size = 30)
         title3.move_to([0.,3.8,0.])

         title4 = MarkupText('Soma vetorial',gradient=(RED, YELLOW), font='Sans', weight='NORMAL',font_size = 30)
         title4.move_to([0.,3.8,0.])
         
         arroba = Text('@thiagosilva.fisica', font='Sans', weight='BOLD',font_size=14)
         arroba.set_opacity(0.2)
         arroba.to_edge(4*DOWN)

         self.play(Write(title), Write(arroba))
         self.wait(4)
         self.remove(title)
         self.play(Transform(title, title2))

         l_e = Line(start=[-1.,0.,0], end =[-1.,-2,0.])
         l_d = Line(start=[1.,0.,0], end =[1.,-2,0.])
         c   = Line(start=[-1.,0.,0], end =[1.,0.,0.])
         b   = Line(l_e.get_bottom(), end =[1.,-2,0.])

         caixa = VGroup(l_e,l_d,c,b).shift(LEFT + UP).scale(0.7)
         
         l_e1 = Line(start=[-1.,0.,0], end =[-1.,-2,0.])
         l_d1 = Line(start=[1.,0.,0], end =[1.,-2,0.])
         c1   = Line(start=[-1.,0.,0], end =[1.,0.,0.])
         b1   = Line(l_e1.get_bottom(), end =[1.,-2,0.])
         
         caixa1 = VGroup(l_e1,l_d1,c1,b1).scale(0.7)
         caixa1.next_to(caixa, RIGHT, buff=0.3)
        
         caixas= VGroup(caixa,caixa1)

         l = Circle(radius=0.2,color= ORANGE)
         l.set_fill(color=ORANGE, opacity=1)
         l.set_sheen(0.3, DR)
         l.next_to(b.get_left() + 0.25*RIGHT,UP, buff=0.04)
         l1 = l.copy()
         l1.next_to(l, RIGHT, buff=0.049)
         l2 = l.copy()
         l2.next_to(l1.get_right(), buff=0.049)
         l3 =l.copy()
         l3.next_to(l,UP,buff=0.049)
         l4= l.copy()
         l4.next_to(l3,RIGHT,buff=0.049)
         l5=l.copy()
         l5.next_to(l4,RIGHT,buff=0.049)
         l6 = l.copy()
         l6.next_to(l3,UP,buff=0.049)
         l7 = l.copy()
         l7.next_to(l6,RIGHT, buff=0.049)
         l8 = l.copy()
         l8.next_to(l7,RIGHT,buff=0.049)

         ls =[l,l1,l2,l3,l4,l5,l6,l7,l8]

         l9 = Circle(radius=0.2,color= ORANGE)
         l9.set_fill(color=ORANGE, opacity=1)
         l9.set_sheen(0.3, DR)
         l9.next_to(b1.get_left() + 0.25*RIGHT,UP, buff=0.04)
         l10 = l9.copy()
         l10.next_to(l9, RIGHT, buff=0.049)
         l11 = l9.copy()
         l11.next_to(l10.get_right(), buff=0.049)
         l12 =l9.copy()
         l12.next_to(l9,UP,buff=0.049)
         l13= l9.copy()
         l13.next_to(l12,RIGHT,buff=0.049)
         l14=l9.copy()
         l14.next_to(l13,RIGHT,buff=0.049)
         l15 = l9.copy()
         l15.next_to(l12,UP,buff=0.049)
         l16 = l9.copy()
         l16.next_to(l15,RIGHT, buff=0.049)
         l17 = l9.copy()
         l17.next_to(l16,RIGHT,buff=0.049)

         ls1 =[l9,l10,l11,l12,l13,l14,l15,l16,l17]
         
         self.play(GrowFromCenter(caixas))
         self.wait(0.1)
        
         for i, j in zip(ls,ls1):
            self.play(GrowFromCenter(i), run_time = 0.02)
            self.wait(0.05)
            self.play(GrowFromCenter(j), run_time = 0.02)
            self.wait(0.05)
         
         lg  =  VGroup(*ls)
         lg1 =  VGroup(*ls1)

         mass = MathTex(r'1', r'\ kg', font_size= 27)
         mass.next_to(caixa, UP,buff= 0.5)
         mass1=mass.copy()
         mass1.next_to(caixa1,UP, buff=0.5)
         plus = MathTex(r'+', font_size= 27)
         plus.next_to(mass, RIGHT, buff=0.5)
         self.wait(0.1)
         self.play(Write(mass), Write(mass1))
         self.wait(5)
         self.play(Write(plus))
         result = MathTex(r'=', r'2',  r'\ kg', font_size= 27)
         result.next_to(mass1,RIGHT, buff=0.3)
         
         
         lg.generate_target()
         lg.target.shift(0.18*RIGHT)
         lg1.generate_target()
         lg1.target.shift(0.18*LEFT)

         slg =VGroup(lg,lg1)
         self.remove(caixas)
         rect = SurroundingRectangle(slg, color=WHITE)

         self.play(Write(result), MoveToTarget(lg), MoveToTarget(lg1), Transform(caixas, rect))
         self.wait(3)
         eqg =VGroup(mass, mass1, plus, result)
         eqg.generate_target()
         eqg.target.shift(0.5*LEFT)

         sg= VGroup(slg,rect)
         sg.generate_target()
         sg.target.shift(0.15*RIGHT)
         result1 =MathTex(r'2',  r'\ kg', font_size= 27)
         result1.next_to(sg,UP,buff=0.3)
         result1.add_updater(lambda q: q.next_to(sg, UP, buff=0.3))

         self.remove(caixas, rect)
         self.play(MoveToTarget(eqg), MoveToTarget(sg))
         self.remove(title,title2)
         self.play(Transform(title2, title3))
         self.wait(5)
         self.play(Indicate(mass[0]),Indicate(mass1[0]), Indicate(result[1]))
         self.wait()
         self.play(Indicate(mass[1]),Indicate(mass1[1]), Indicate(result[2]))
         self.wait()
         self.play(FadeOut(mass), FadeOut(mass1), FadeOut(result), FadeOut(plus),Write(result1))
         self.play(Rotate(sg, PI/2, about_point=ORIGIN))
         self.wait(3)
         self.play(Rotate(sg, -PI/2, about_point=ORIGIN))
         self.wait(5)
         self.play(FadeOut(sg, shift=DOWN), FadeOut(result1,shift=RIGHT))
         self.remove(title,title2,title3)
         plane = NumberPlane()
         plane.set_opacity(0.5)
         u = Vector([0,1],color=RED)
         u_label = MathTex(r'\vec{u}', color = RED, font_size = 30)
         u_label.next_to(u, LEFT, buff=0.1)
         v = Vector([1,0], color= YELLOW)
         v.shift(1*RIGHT + 2*UP)
         v_label = MathTex(r'\vec{v}', color = YELLOW, font_size = 30)
         v_label.next_to(v,UP,buff=0.1)
         v_label.add_updater(lambda f: f.next_to(v,UP,buff=0.1))
         v.generate_target()
         v.target.shift(1*DOWN + 1*LEFT)
         w = Vector([1,1], color = ORANGE)
         w_label =MathTex(r'\vec{u} + \vec{v}', color = ORANGE, font_size = 30)
         w_label.next_to(w,DOWN, buff=0.01)

         line = LabeledLine(label=Text('1', font_size =30),start=[-1,0.,0.], end=[-1,1,0.], label_frame =False, color= PURE_RED)
         self.play(Transform(title3, title4),Create(plane), Create(line),Create(u), Create(v), Create(u_label), Create(v_label))
         self.wait(5)
         self.play(MoveToTarget(v))
         self.wait(5)
         self.play(Create(w), Create(w_label))
         self.wait(2)

         wsum = MathTex(r'\left\|\vec{u} + \vec{v} \right\|' , r'=', r'\sqrt{1^2 + 1^2} =\sqrt{2}', font_size = 30)
         wsum.next_to(w_label,DOWN, buff= 0.3)
         wsum.shift(0.5*LEFT)
         self.play(Create(wsum), plane.animate.set_opacity(0.3))
         self.wait(10)
         self.play(Uncreate(plane), Uncreate(line), Uncreate(u), Uncreate(u_label), Uncreate(v), Uncreate(v_label), Uncreate(w_label), Uncreate(wsum))
         line1 = DashedLine([0.,0.,0.], [2.,0.,0.])
         angulo = Angle(line1, w)
         a_t = MathTex(r'\theta', font_size =30)
         a_t.next_to(angulo,RIGHT)
         self.play(Create(line1), Create(angulo), Create(a_t))
         self.wait(3)
         self.play(Uncreate(angulo), Uncreate(a_t), Rotate(w, angle=PI, about_point=ORIGIN))
         self.wait(5)
         self.play(Uncreate(w), Uncreate(line1))
         call = Text('Me siga', font='Sans', weight='BOLD',font_size=14)
         call_1 = Text('para mais conteúdos de Física', font='Sans', weight='BOLD',font_size=14).next_to(call, DOWN, buff=0.5)
         call_2 = Text('@thiagosilva.fisica', font='Sans', weight='BOLD',font_size=14).next_to(call_1, DOWN, buff=0.5)
         self.play(FadeOut(title4),Write(call), Write(call_1), Write(call_2))
         self.wait()
        






         