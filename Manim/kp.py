from manim import *


SCALE_FACTOR = 0.8

tmp_pixel_height = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = tmp_pixel_height

config.frame_height = config.frame_height/SCALE_FACTOR
config.frame_width = config.frame_height * 9/16

FRAME_HEIGHT = config.frame_height
FRAME_WIDTH = config.frame_width


class kp(MovingCameraScene):
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
            title = MarkupText('Leis de Kepler',gradient=(BLUE, RED), font='Sans', weight='NORMAL',font_size = 30)
            title.move_to([0.,3.8,0.])
            title1 = MarkupText('Lei das áreas',gradient=(BLUE, RED), font='Sans', weight='NORMAL',font_size = 30)
            title1.move_to([0.,3.8,0.])
            title2 = MarkupText('Lei das órbitas',gradient=(BLUE, RED), font='Sans', weight='NORMAL',font_size = 30)
            title2.move_to([0.,3.8,0.])
            title3 = MarkupText('Lei dos períodos',gradient=(BLUE, RED), font='Sans', weight='NORMAL',font_size = 30)
            title3.move_to([0.,3.8,0.])


            
            arroba = Text('@thiagosilva.fisica', font='Sans', weight='BOLD',font_size=14)
            arroba.set_opacity(0.2)
            arroba.to_edge(4*DOWN)

            self.play(Write(title), Write(arroba))
            self.wait()

            
            earth = SVGMobject('earth.svg').scale(0.1).set_z_index(1)
            earth_s_orbit = Circle(radius =1, color= WHITE).next_to(earth,LEFT, buff=-0.1).set_z_index(0)
           
            


            mars = Circle(radius=0.08, color =RED).set_sheen(0.1)
            mars.set_fill(color=RED_A,opacity=1)
            mars_orbit = Ellipse(width=4, height=2).shift(0.3*LEFT)
            mars.next_to(mars_orbit,RIGHT, buff =-0.1)
            mars.set_z_index(3)


            sun = Circle(radius=0.25, color= YELLOW).set_sheen(0.5)
            sun.set_fill(color=YELLOW,opacity=1)
            sun.move_to(earth_s_orbit.get_center())

          
            self.play(Create(sun), Create(mars_orbit), Create(mars))
            self.wait(0.1)
            self.play(MoveAlongPath(mars, mars_orbit))
            self.wait()
            self.play(Create(earth), Create(earth_s_orbit))
            self.wait(0.1)
            self.play(MoveAlongPath(earth, earth_s_orbit))
            self.wait(2)
            
            circulo = Circle(radius =2, color= WHITE)
            linha = Line(circulo.get_top(), circulo.get_bottom())
            centro = LabeledDot(label='C', color = BLUE).set_z_index(3).scale(0.6)
            centro.next_to(linha.get_center(), buff=-0.19)
            equante = LabeledDot(label='E', color=GREEN).set_z_index(3).scale(0.6)
            equante.next_to(linha.get_bottom()*0.5, buff=-0.19)
            sun1 = LabeledDot(label='S', color = YELLOW).set_z_index(3).scale(0.6)
            sun1.next_to(linha.get_top()*0.5, buff=-0.19)

            mars.generate_target()
            mars.target.next_to(circulo, RIGHT, buff=-0.1)
            mars.set_z_index(3)

            peri = MarkupText('Periélio', font='Sans', weight='NORMAL',font_size = 20)
            peri.next_to(circulo,UP, buff=0.2)
            afe = MarkupText('Afélio', font='Sans', weight='NORMAL',font_size = 20)
            afe.next_to(circulo,DOWN, buff=0.2)

            anim =[
                 Create(circulo),
                 Create(linha),
                 Create(centro),
                 Create(equante),
                 Create(sun1),
            ]

            fade1 = [
                 FadeOut(earth),
                 FadeOut(earth_s_orbit),
                 FadeOut(mars_orbit),
                 FadeOut(sun)
            ]
            self.play(AnimationGroup(*fade1))
            self.wait(2)
            self.play(AnimationGroup(*anim), MoveToTarget(mars))
            self.wait(4)
            self.play(Rotate(mars, angle=4*PI, about_point=ORIGIN), Write(peri),
                Write(afe), rate_func=linear, run_time = 3)
            self.wait(5)
            self.play(Unwrite(peri), Unwrite(afe), FadeOut(circulo), FadeOut(linha), FadeOut(centro), FadeOut(equante), FadeOut(sun1), FadeOut(mars))


            ne_orbit = Ellipse(width=4, height=3.8, color=WHITE)
            earth.next_to (ne_orbit,RIGHT, buff=-0.12)
            sun.next_to(ne_orbit.get_left()*0.7, buff= 0)

            self.play(Create(ne_orbit), Create(earth), Create(sun))
            self.wait()

            raio_v = Line(sun.get_center(), earth.get_center(), color = BLUE)

            def update_line(raio_v):
                 raio_v.become(Line(sun.get_center(), earth.get_center(), color = BLUE))
            raio_v.add_updater(update_line)

            self.play(Create(raio_v))
            self.wait()
            self.play(ChangeSpeed(MoveAlongPath(earth, ne_orbit, angle=PI),
            speedinfo={0:0, 0.5:1, 0.6:0.5, 1:0}), run_time =5)
            self.wait(0.01)
            self.play(ChangeSpeed(MoveAlongPath(earth, ne_orbit, angle=PI),
            speedinfo={0:0, 0.5:1, 0.6:0.5, 1:0}), run_time =5)
            self.wait(0.01)

            a1 = AnnularSector(inner_radius=0, outer_radius=3.08, angle=PI/20, color=BLUE, fill_opacity=0.5)
            a1.next_to(ne_orbit.get_left()*0.5, buff= 0).set_z_index(-1)

            a1.shift(0.25*UP + 0.1*LEFT)

            a2 = AnnularSector(inner_radius=0, outer_radius=0.7, angle=PI/3, color=BLUE, fill_opacity=0.5).rotate(angle=0.85*PI, about_point=ORIGIN)
            a2.next_to(ne_orbit.get_left()*0.5, buff= 0)
            a2.set_z_index(-1)
            a2.shift(1.03*LEFT)

            a1_t = MathTex(r'A_1', font_size=25)
            a1_t.move_to(a1.get_center()).shift(0.1*DOWN + 0.3*RIGHT)
            a2_t = MathTex(r'A_2', font_size=25)
            a2_t.move_to(a2.get_center()).shift(0.085*LEFT)

            v_a = MathTex(r'\frac{A_1}{\Delta t_1}=\frac{A_2}{\Delta t_2}',font_size=25)
            v_a.next_to(ne_orbit, UP, buff=0.3)

            self.play(Create(a1), Create(a2),Uncreate(raio_v))
            self.wait()
            self.play(Transform(title, title1), Write(a1_t), Write(a2_t))
            self.wait(2)
            self.play(Write(v_a))
            self.wait()
            self.play(Unwrite(v_a), ChangeSpeed(MoveAlongPath(earth, ne_orbit, angle=PI),
            speedinfo={0:0, 0.5:1, 0.6:0.5, 1:0}), run_time =5)
            self.wait()

            a11 = a1.set_color(RED_A)
            a22 = a2.set_color(RED_A)

            self.remove(earth)

            self.play(Transform(a1,a11), Transform(a2,a22))
            self.wait(0.1)

            mars.next_to (ne_orbit,RIGHT, buff=-0.12)

            self.play(ChangeSpeed(MoveAlongPath(mars, ne_orbit, angle=PI),
            speedinfo={0:0, 0.5:1, 0.6:0.5, 1:0}), run_time =5)

            eixo_m = DashedLine(ne_orbit.get_left(), ne_orbit.get_right()).set_opacity(0.5)
            eixo_mn = DashedLine(ne_orbit.get_top(), ne_orbit.get_bottom()).set_opacity(0.5)

            f1 = Dot(radius=0.11, color=WHITE)
            f1.move_to(sun.get_center())
            f1_t = MathTex(r'F_1', font_size = 25)
            f1_t.next_to(sun,UP, buff=0.3)

            f2 = Dot(radius=0.11, color=WHITE)
            f2.next_to(ne_orbit.get_right()*0.5, buff= 0)
            f2_t = MathTex(r'F_2', font_size = 25)
            f2_t.next_to(f2,UP, buff=0.3)


            self.remove(title, title1, mars)

            self.play(Uncreate(a11), Uncreate(a22), Uncreate(mars), Unwrite(a1_t), Unwrite(a2_t), Create(eixo_m), Create(eixo_mn), Transform(title1, title2), Create(f1), Write(f1_t), Create(f2), Write(f2_t) )
        
            self.wait(3)

            self.play(Uncreate(eixo_m), Uncreate(eixo_mn),Uncreate(f1), Unwrite(f1_t), Uncreate(f2), Unwrite(f2_t))
            self.wait()
            
            earth.next_to (ne_orbit,RIGHT, buff=-0.12)

            self.play(Create(raio_v), Create(earth))
            self.wait()
            self.play(ChangeSpeed(MoveAlongPath(earth, ne_orbit, angle=PI),
            speedinfo={0:0, 0.5:1, 0.6:0.5, 1:0}), run_time =2)
            self.wait(0.001)
            self.play(ChangeSpeed(MoveAlongPath(earth, ne_orbit, angle=PI),
            speedinfo={0:0, 0.5:1, 0.6:0.5, 1:0}), run_time =2)
            self.wait(0.001)

            lei_p = MathTex(r'T^2 = k R^3', font_size =25)
            lei_p.next_to(ne_orbit,UP, buff=0.3)

            lei_pp = MathTex(r'T^2 = \left(\frac{4\pi ^2}{GM_{\odot}}\right) R^3', font_size =25)
            lei_pp.next_to(ne_orbit,UP, buff=0.3)
            
            self.remove(title, title1,title2)

            self.play(Write(lei_p), Transform(title2, title3))
            self.wait()
            self.play(TransformMatchingTex(lei_p, lei_pp))
            self.wait(2)

            call = Text('Me siga', font='Sans', weight='BOLD',font_size=14)
            call_1 = Text('para mais conteúdos de Física', font='Sans', weight='BOLD',font_size=14).next_to(call, DOWN, buff=0.5)
            call_2 = Text('@thiagosilva.fisica', font='Sans', weight='BOLD',font_size=14).next_to(call_1, DOWN, buff=0.5)
            
            fade_ou_in = [
                 Uncreate(ne_orbit),
                 Uncreate(raio_v),
                 Uncreate(earth),
                 Uncreate(sun),
                 Unwrite(lei_pp),
                 FadeOut(title3, shift = UP),
                 Write(call),
                 Write(call_1),
                 Write(call_2)
            ]
            
            self.remove(title, title1,title2, title3)

            self.play(AnimationGroup(*fade_ou_in))
            self.wait()

            
            

                        

