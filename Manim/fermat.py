from manim import *


SCALE_FACTOR = 0.8

tmp_pixel_height = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = tmp_pixel_height

config.frame_height = config.frame_height/SCALE_FACTOR
config.frame_width = config.frame_height * 9/16

FRAME_HEIGHT = config.frame_height
FRAME_WIDTH = config.frame_width


class fermat(MovingCameraScene):
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
            title = MarkupText('Princípio de Fermat',gradient=(YELLOW, ORANGE), font='Sans', weight='NORMAL',font_size = 30)
            title.move_to([0.0,3.5,0.])
            title1 = MarkupText('Lei da Reflexão',gradient=(YELLOW, ORANGE), font='Sans', weight='NORMAL',font_size = 30)
            title1.move_to([0.0,3.8,0.])
            
            arroba = Text('@thiagosilva.fisica', font='Sans', weight='BOLD',font_size=14)
            arroba.set_opacity(0.2)
            arroba.to_edge(3*DOWN)

            self.play(Write(title), Write(arroba))
            self.wait(3)

            a = Dot(radius = 0.05, color = WHITE).move_to([-2.0,-1.5,0.0])
            a_flash = Dot(radius = 0.05, color = WHITE).move_to([-2.0,-1.5,0.0]).set_z_index(-1)

            b = Dot(radius = 0.05, color = WHITE).move_to([2.0,1.5,0.0])

            b_down = b.copy()
            b_down.move_to([2.0,-1.5,0.0])

            a_t = MathTex(r'A', font_size =25)
            a_t.next_to(a,UP, buff=0.3)
            b_t = MathTex(r'B', font_size =25)
            b_t.next_to(b,UP, buff=0.3)

            b_down_t = MathTex(r'B_{1}', font_size =25)
            b_down_t.next_to(b_down,RIGHT, buff= 0.1)



            light = Line(a.get_center(), b.get_center(), color = RED)
        

            # Definindo os pontos de controle
            control_1 = Dot(radius = 0.1, color = WHITE).move_to([-1.0, -3.0, 0.0])
            control_2 = Dot(radius = 0.1, color = WHITE).move_to([-2.0, 1.0, 0.0])

            bezier = CubicBezier(a.get_center(), control_1.get_center(), control_2.get_center(), b.get_center(), color= YELLOW)


            caminho_I = MathTex(r'I', font_size = 25, color = YELLOW)
            caminho_I.next_to(bezier, UP, buff= - 0.5)

            caminho_II = MathTex(r'II', font_size = 25, color= RED)
            caminho_II.next_to(light, DOWN, buff= - 1.2)
            
            self.play(Create(a), Write(a_t),Create(b), Write(b_t), Create(a_flash))
            self.wait(3)
            self.play(Flash(a_flash, color= RED), Create(light), Create(bezier), Write(caminho_I), Write(caminho_II))
            self.wait(5)

            a_t.add_updater(lambda m: m.next_to(a,UP, buff=0.3))
            a.generate_target()
            a.target.move_to([-2.0,1.5,0.0])


            espelho = Rectangle(height=0.05, width=5, color=BLUE_A)
            espelho.set_fill(color=BLUE_A, opacity=0.5)

            self.play(Unwrite(caminho_I), Unwrite(caminho_II), Uncreate(bezier), Uncreate(light), Uncreate(a_flash),MoveToTarget(a), Create(espelho))
            self.wait(5)

            light1 = Line(start=a.get_center(), end= [-1.0,0.0,0.0], color = PURE_RED)
            reflected1 = Line(start=[-1.0,0.0,0.0], end= b.get_center(), color = PURE_RED)

            n_1 = DashedLine(start=[-1.0,0.0,0.0], end= [-1.0,1.3,0.0], color = WHITE)

            angle1 = Angle(n_1, light1, radius=0.6, quadrant=(1,-1))
            angle1_t = MathTex(r'\theta_i', font_size = 25)
            angle1_t.next_to(angle1, UP, buff= 0.1)
            angle2 = Angle(reflected1, n_1, radius=0.6, color = YELLOW_A)
            angle2_t = MathTex(r'\theta_r', color=YELLOW_A, font_size = 25)
            angle2_t.next_to(angle2, UP, buff= 0.1)

            eq = MathTex(r'\theta_i', r'\neq', r'\theta_r', font_size= 25).next_to(espelho,DOWN, buff= 0.3)

            self.play(Flash(a, color = RED), Create(light1))
            self.wait(0.001)
            self.play(Create(reflected1), Create(n_1), Create(angle1), Create(angle1_t), Create(angle2), Create(angle2_t), Write(eq))
            self.wait(3)

            
            
            bb = DashedLine(start = b.get_center(), end = b_down.get_center())

            long_line = DashedLine(start = b_down.get_center(), end = [2.0,-5.0,0.0])

            prolo1 = DashedLine(start = light1.get_end(), end = [2.0,-4.5,0.0], color = RED)

            self.play(Create(b_down), Create(b_down_t), Create(bb), Unwrite(eq))
            self.wait(2)

            self.play(Create(long_line), Create(prolo1))
            self.wait(5)

            self.play(Uncreate(light1), Uncreate(reflected1), Uncreate(n_1), Uncreate(angle1), Uncreate(angle2), Unwrite(angle1_t), Unwrite(angle2_t), Uncreate(prolo1), Uncreate(long_line), Uncreate(bb))
            self.wait()

            light2 = Line(start=a.get_center(), end= b_down.get_center()*0.009, color = PURE_RED)
            reflected2 = Line(start=light2.get_end(), end= b.get_center(), color = PURE_RED)

            n_2 = DashedLine(start=light2.get_end(), end= [0.0, 2.0,0.0], color = WHITE)

            self.play(Flash(a, color=RED),Create(light2))
            self.wait(0.001)
            self.play(Create(reflected2), Create(n_2))
            self.wait()

            prolo2 = DashedLine(start = light2.get_end(), end = b_down.get_center(), color = RED)
            
            angle3 = Angle(n_2, light2, radius=0.6, quadrant=(1,-1))
            angle3_t = MathTex(r'\theta_i', font_size = 25)
            angle3_t.next_to(angle3, UP, buff= 0.1)
            angle4 = Angle(reflected2, n_2, radius=0.6, color = YELLOW_A)
            angle4_t = MathTex(r'\theta_r', color=YELLOW_A, font_size = 25)
            angle4_t.next_to(angle4, UP, buff= 0.1)

            eq1 = MathTex(r'\theta_i', r'=', r'\theta_r', font_size= 30).next_to(espelho,DOWN, buff= 1)

            self.play(Create(prolo2))
            self.wait(2)
            self.play(Create(angle3), Create(angle3_t), Create(angle4), Create(angle4_t))
            self.wait(3)

            rec = SurroundingRectangle(eq1)

            self.remove(title)
            self.play(Uncreate(prolo2), Uncreate(b_down), Unwrite(b_down_t), Write(eq1), Create(rec), Transform(title,title1))
            self.wait(2)
            
            self.remove(title, title1)

            self.play(Unwrite(angle3_t), Uncreate(angle3), Unwrite(angle4_t), Uncreate(angle4), Uncreate(n_2), Uncreate(espelho), Uncreate(b), Uncreate(a), Unwrite(b_t), Unwrite(a_t), Uncreate(light2), Uncreate(reflected2), Uncreate(rec), Unwrite(eq1), FadeOut(title1))
            
            

            call = Text('Me siga', font='Sans', weight='BOLD',font_size=14)
            call_1 = Text('para mais conteúdos de Física', font='Sans', weight='BOLD',font_size=14).next_to(call, DOWN, buff=0.5)
            call_2 = Text('@thiagosilva.fisica', font='Sans', weight='BOLD',font_size=14).next_to(call_1, DOWN, buff=0.5)

            self.play(Write(call), Write(call_1), Write(call_2))
            self.wait()
