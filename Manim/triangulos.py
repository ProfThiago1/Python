from manim import *

SCALE_FACTOR = 0.8

tmp_pixel_height = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = tmp_pixel_height

config.frame_height = config.frame_height/SCALE_FACTOR
config.frame_width = config.frame_height * 9/16

FRAME_HEIGHT = config.frame_height
FRAME_WIDTH = config.frame_width

class triangulos(MovingCameraScene):
    def setup(self, add_border =False    ):
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
        
        title = MarkupText('Geometria Esférica',color=BLACK, font_size=33)
        title.move_to([0.,3.5,0.0])

        title1 = MarkupText('Geometria Plana',color=BLACK, font_size=33)
        title1.move_to([0.,3.5,0.0])
        title2 = MarkupText('Triângulo Esférico',color=BLACK, font_size=33)
        title2.move_to([0.,3.5,0.0])

        arroba = Text('@thiagosilva.fisica', font='Open Sans SemiBold',color=BLACK,font_size=14)
        arroba.set_opacity(0.2)
        arroba.to_edge(3*DOWN)

        # Triângulo
        base = Line(start = [-1.0,0.0,0.0], end = [1.0,0.0,0.0], color = BLACK)
        ld = Line(start = base.get_end(), end = [0.0,1.5,0.0], color = BLACK)
        le = Line(start = base.get_left(), end = [0.0,1.5,0.0], color = BLACK)

        triangulo = VGroup(base,ld,le)

        #ângulos e suas transformações
        alpha = AnnularSector(inner_radius=0, outer_radius=0.5, angle=PI/3, color=RED).set_z_index(-1)
        alpha.move_to([-1.22,-0.15,0.0])

        alpha_text = MathTex(r'\alpha', color = BLACK, font_size = 27)
        alpha_text.next_to(alpha, RIGHT, buff=0.1)

        alpha_text.add_updater(lambda a: a.next_to(alpha, RIGHT, buff=0.1))


        beta = AnnularSector(inner_radius=0, outer_radius=0.5, angle=PI/3, color=BLUE).set_z_index(-1)
        beta.rotate(PI/1.5)
        beta.move_to([1.22,-0.15,0.0])

        beta_text = MathTex(r'\beta', color = BLACK, font_size = 27)
        beta_text.next_to(beta, LEFT, buff=0.1)

        beta_text.add_updater(lambda b: b.next_to(beta,LEFT, buff=0.1))


        teta = AnnularSector(inner_radius=0, outer_radius=0.5, angle=PI/3, color=GREEN).set_z_index(-1)
        teta.rotate(PI + 0.33*PI)
        teta.move_to([0.0,1.63,0.0])

        teta_text = MathTex(r'\theta', color = BLACK, font_size = 27)
        teta_text.next_to(teta, DOWN, buff=0.1)


        teta_text.add_updater(lambda t: t.next_to(teta, UP, buff = 0.1))

        eq = MathTex(r'\alpha +', r' \theta +', r'\beta = 180 ^{\circ}', color = BLACK, font_size = 27)
        eq.next_to(base, DOWN, buff = 1)


        teta.generate_target()
        teta.target.move_to([0.0,0.03,0.0]).rotate(PI)

        alpha.generate_target()
        alpha.target.move_to([0.245,0.0,0.0])

        beta.generate_target()
        beta.target.move_to([-0.245,0.0,0.0])





        # esfera e o triângulo esférico

        esfera = Circle(radius=2, color=BLACK)
        arc1 = ArcBetweenPoints(start=esfera.get_left(), end = esfera.get_right(), color = LOGO_BLACK)

        arc2 = DashedVMobject(ArcBetweenPoints(start=esfera.get_left(), end = esfera.get_right(), color = LOGO_BLACK))
        arc2.rotate_about_origin(angle=PI)

        cent = Dot(radius=0.5*DEFAULT_DOT_RADIUS, color=BLACK)

        a_p = Dot(color=PURE_RED)
        a_p.move_to(esfera.get_top())

        a_pt = MathTex(r'A', color= BLACK, font_size = 27)
        a_pt.next_to(a_p, UP, buff=0.1)

        b_p = Dot(color = PURE_RED)
        b_p.next_to(0.7*arc1.get_left(), buff=-0.35)
        
        b_pt = MathTex(r'B', color= BLACK, font_size = 27)
        b_pt.next_to(b_p, DOWN, buff=0.1)

        c_p = Dot(color = PURE_RED)
        c_p.next_to(0.7*arc1.get_right(), buff=0.22)
        
        c_pt = MathTex(r'C', color= BLACK, font_size = 27)
        c_pt.next_to(c_p, DOWN, buff=0.1)

        pesf=VGroup(cent,a_p,b_p,c_p,a_pt, b_pt, c_pt)

        arc_conf={'radius': 3, 'color': GRAY}
        poly_config ={'stroke_color':GRAY, 'fill_opacity':0.5, 'color':BLUE}

        a = [-1.7,-0.3,0]
        b = [1.7,-0.3,0]
        c = [0,2.0,0]

        arc_1 =ArcBetweenPoints(a,b, **arc_conf)
        arc_2 =ArcBetweenPoints(b,c, **arc_conf)
        arc_3 =ArcBetweenPoints(c,a, **arc_conf)

        spherical = ArcPolygonFromArcs(arc_1,arc_2,arc_3, **poly_config )
        

        self.play(Write(arroba), Create(triangulo.scale(1.5)), Create(alpha), Write(alpha_text), Create(beta), Write(beta_text), Create(teta), Write(teta_text))
        self.wait(0.5)
        self.play(Indicate(alpha), Indicate(beta), Indicate(teta))
        self.wait(5)

        self.play(Write(eq))
        self.wait()
        self.play(Write(title1))

        self.wait(4)

        self.play(FadeOut(triangulo),MoveToTarget(alpha), MoveToTarget(beta), MoveToTarget(teta))

        ang = VGroup(teta, beta, alpha)
        self.wait()
        self.play(Indicate(ang))
        self.wait()

        self.play(FadeOut(ang), Unwrite(alpha_text), Unwrite(teta_text), Unwrite(beta_text), Unwrite(eq))
        self.wait()
        self.play(Create(esfera), Create(arc1), Create(arc2), Create(pesf))
        self.wait(5)
    
        self.play(Create(spherical))
        self.wait(3)
        self.remove(title1)

        self.play(Transform(title1, title))
        self.wait(3)
        self.remove(title1, title)
        self.play(Transform(title, title2),FadeOut(esfera), FadeOut(arc1), FadeOut(arc2), FadeOut(cent), spherical.animate.set_fill(opacity=0))

        self.wait(3)

        alpha = AnnularSector(start_angle=-1.75*PI/10,inner_radius=0, outer_radius=0.5, angle=1.21*PI/2, color=RED).set_z_index(-3)
        alpha.move_to([-1.435,-0.17,0.0])

        alpha_text = MathTex(r'\alpha', color = BLACK, font_size = 27)
        alpha_text.next_to(alpha, RIGHT, buff=0.1)

        alpha_text.add_updater(lambda a: a.next_to(alpha, RIGHT, buff=0.1))


        beta = AnnularSector(start_angle=-1.14*PI/10, inner_radius=0, outer_radius=0.5, angle=0.62*PI, color=BLUE).set_z_index(-3)
        beta.rotate(PI/1.5)
        beta.move_to([1.425,-0.175,0.0])

        beta_text = MathTex(r'\beta', color = BLACK, font_size = 27)
        beta_text.next_to(beta, LEFT, buff=0.1)

        beta_text.add_updater(lambda b: b.next_to(beta,LEFT, buff=0.1))


        teta = AnnularSector(start_angle=-1.3*PI/10, inner_radius=0, outer_radius=0.5, angle=0.615*PI, color=GREEN).set_z_index(-5)
        teta.rotate(PI + 0.33*PI)
        teta.move_to([-0.01,1.770,0.0])

        teta_text = MathTex(r'\theta', color = BLACK, font_size = 27)
        teta_text.next_to(teta, DOWN, buff=0.1)


        #teta_text.add_updater(lambda t: t.next_to(teta, UP, buff = 0.1))

        esf_a = VGroup(alpha,alpha_text,beta,beta_text,teta,teta_text)

        self.play(Create(esf_a))
        self.wait()


        eq1 = MathTex(r'180^{\circ}< \alpha + \beta + \theta', color = BLACK, font_size = 27)
        eq1.next_to(spherical, DOWN, buff = 1)

        self.play(Write(eq1))
        self.wait(3)

        teta.generate_target()
        teta.target.move_to([0.0,0.03,0.0]).rotate(PI)

        alpha.rotate(-0.225*PI)
        alpha.generate_target()
        alpha.target.move_to([0.248,-0.293,0.0])

        beta.rotate(0.3*PI)
        beta.generate_target()
        beta.target.move_to([-0.216,-0.312,0.0])
        
        teta_text.add_updater(lambda t: t.next_to(teta, UP, buff = 0.1))
        
        
        self.play(FadeOut(spherical), FadeOut(pesf), MoveToTarget(beta), MoveToTarget(alpha), MoveToTarget(teta))
        self.wait(4)
        self.play(Indicate(esf_a))
        self.wait()
        self.remove(title,title1, title2)

        call = Text('Me siga', font='Sans', weight='BOLD',font_size=14, color = BLACK)
        call_1 = Text('para mais conteúdos de Matemática', font='Sans', weight='BOLD',font_size=14, color = BLACK).next_to(call, DOWN, buff=0.5)
        call_2 = Text('@thiagosilva.fisica', font='Sans', weight='BOLD',font_size=14, color = BLACK).next_to(call_1, DOWN, buff=0.5)
        
        self.play(FadeOut(esf_a), Unwrite(eq1), Unwrite(title2),FadeOut(arroba),Write(call), Write(call_1), Write(call_2))
        self.wait()
        

