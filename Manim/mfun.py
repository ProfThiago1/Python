from manim import *

SCALE_FACTOR = 0.8

tmp_pixel_height = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = tmp_pixel_height

config.frame_height = config.frame_height/SCALE_FACTOR
config.frame_width = config.frame_height * 9/16

FRAME_HEIGHT = config.frame_height
FRAME_WIDTH = config.frame_width

class Fun(MovingCameraScene):
    def setup(self, add_border =False):
        if add_border:
            self.border = Rectangle(
                width=FRAME_WIDTH,
                height=FRAME_HEIGHT,
                    color = RED
            )
            self.border_1 = Rectangle(width=FRAME_WIDTH -1,
                height=FRAME_HEIGHT - 1,
                    color = YELLOW)
            self.add(self.border)
            self.add(self.border_1)
    def construct(self):
        self.camera.background_color = WHITE
        title = MarkupText('Função modular',color=BLACK, font_size=33)
        title.move_to([0.,3.5,0.0])

        arroba = Text('@thiagosilva.fisica', font='Open Sans SemiBold',color=BLACK,font_size=14)
        arroba.set_opacity(0.2)
        arroba.to_edge(3*DOWN)

        in_text =[
            Write(title), 
            Write(arroba),
        ]

        ax_x = Arrow([-1.5,0.0,0.0],[1.5,0.0,0.0], color = LOGO_BLACK, stroke_width=3, max_tip_length_to_length_ratio=0.05)
        ax_y = Arrow([0.0,-1.5,0.0],[0.0,1.5,0.0], color = LOGO_BLACK, stroke_width=3, max_tip_length_to_length_ratio=0.05)

        ax_x_label = MathTex(r'x', font_size = 20, color = BLACK)
        ax_x_label.next_to(ax_x.get_end(), UP, buff=0.1)
        ax_y_label = MathTex(r'y', font_size = 20, color = BLACK)
        ax_y_label.next_to(ax_y.get_end(), UP, buff= 0.1)
        axes = VGroup(ax_x, ax_y, ax_x_label, ax_y_label)
        

        modular_graph1 = Line([0.0,0.0,0.0],[1.0,1.0,0.0])
        modular_graph1.set_color_by_gradient(DARK_BLUE,PURE_BLUE)
        modular_graph2 = Line([-1.0,1.0,0.0],[0.0,0.0,0.0])
        modular_graph2.set_color_by_gradient(DARK_BLUE,PURE_BLUE)
        

        fun1 =VGroup(axes, modular_graph2, modular_graph1)
        fun1.scale(1.3)
        fun1_text=  MathTex(r'f(x)=|x|', color = BLACK, font_size = 30)
        fun1_text.next_to(axes, UP, buff= 0.05)

        #Animação de início

        self.play(*in_text,Create(fun1.shift(1*DOWN)),FadeIn(fun1_text, shift=DOWN))
        self.wait(1.5)
        self.play(Uncreate(fun1), FadeOut(fun1_text, shift=UP))

        # A presentação dos conceitos

        fun2_text = MathTex(r'g(x) =|sen(x)|', color = LOGO_BLACK, font_size = 30)
        fun3_text = MathTex(r'w(x) =|x^2 + 2x|', color = LOGO_BLACK, font_size = 30)
        fun4_text = MathTex(r'h(x) =|x + 1|', color = LOGO_BLACK, font_size = 30)
        fun5_text = MathTex(r'\eta(x) =\left \lvert\frac{x+1}{x}\right \rvert', color = LOGO_BLACK, font_size = 30)

      

        self.play(Succession(FadeIn(fun2_text, shift= DOWN),
            FadeIn(fun3_text.move_to([-1.3,1,0.0]), shift = LEFT),
            FadeIn(fun4_text.move_to([1,1,0.0]), shift = UP),
            FadeIn(fun1_text.move_to([-1,-1,0.0]), shift = RIGHT)),
            FadeIn(fun5_text.move_to([1,-1,0.0]), shift = RIGHT)
        )
        self.wait(3)
        self.play(Succession(FadeOut(fun2_text, shift= DOWN),
            FadeOut(fun3_text.move_to([-1.3,1,0.0]), shift = LEFT),
            FadeOut(fun4_text.move_to([1,1,0.0]), shift = UP),
           FadeOut(fun1_text.move_to([-1,-1,0.0]), shift = RIGHT),
            FadeOut(fun5_text.move_to([1,-1,0.0]), shift = RIGHT))
        )
        self.wait(3)

        title_trans = MarkupText('Módulo de um número',color=LOGO_BLACK, font_size=27)
        title_trans.to_corner(UP+LEFT)


        ####################################################/
        defi = Text(
            'Definimos o módulo de um número real x, \n simbolizado por |x| como:',
            font_size=17,
            color=BLACK, line_spacing=1.2)
        defi.move_to([0.0, 1.3, 0.0])

        
        mod1 = MathTex(r'\bullet \ |-2|', r'= 2', font_size = 30, color = LOGO_BLACK)
        mod2 = MathTex(r'\bullet \ |2|', r'= 2', font_size = 30, color = LOGO_BLACK)


        defmod = MathTex(r'|x| =', color = LOGO_BLACK, font_size=27)
        defmod.move_to([-1.5,0.0,0.0])
        fsent = MathTex(r'x, \ x \  \geq 0', color = LOGO_BLACK, font_size=27)
        ssent = MathTex(r'-x, \ x \ < 0', color = LOGO_BLACK, font_size=27)
        ssent.next_to(fsent, DOWN, buff= 0.4)

        sents = VGroup(fsent, ssent)
        sents.next_to(defmod, RIGHT, buff=0.5)
        brace = Brace(sents, LEFT, color = LOGO_BLACK, buff = 0.05, stroke_width=1)


        self.play(Transform(title,title_trans), Write(mod1[0].move_to([-1.3,2.0,0.0])))
        self.wait(2)
        self.play(Write(mod1[1].next_to(mod1[0], RIGHT, buff= 0.1)))
        self.wait(1.5)
        self.play(Write(mod2[0].move_to([-1.5,1.0,0.0])))
        self.wait(1)
        self.play(Write(mod2[1].next_to(mod2[0], RIGHT, buff= 0.1)))
        self.wait(3)
        self.play(Unwrite(mod1), Unwrite(mod2))
        self.wait(3)
        self.play(Succession(Write(defi),Write(defmod), FadeIn(sents, shift = RIGHT), FadeIn(brace)))
        self.wait(2)


        self.play(Unwrite(defmod),FadeOut(sents, shift = LEFT), FadeOut(brace), Unwrite(defi))
        self.wait(2)

        #função seno
        funcao = MarkupText('A imagem de uma função',color=LOGO_BLACK,font_size=27)
        funcao.to_corner(UP)
        
        ax_x2 = Arrow([-2.27,0.0,0.0],[2.5,0.0,0.0], color = LOGO_BLACK, stroke_width=3, max_tip_length_to_length_ratio=0.05)
        ax_y2 = Arrow([-2.0,-2,0.0],[-2.0,2,0.0], color = LOGO_BLACK, stroke_width=3, max_tip_length_to_length_ratio=0.05)

        ax_x_label2 = MathTex(r'x', font_size = 20, color = BLACK)
        ax_x_label2.next_to(ax_x2.get_end(), UP, buff=0.1)
        ax_y_label2 = MathTex(r'y', font_size = 20, color = BLACK)
        ax_y_label2.next_to(ax_y2.get_end(), UP, buff= 0.1)
        
        ax_y_label2.add_updater(lambda t: t.next_to(ax_y2.get_end(),UP,buff=0.1))
        axes2 = VGroup(ax_x2, ax_y2, ax_x_label2, ax_y_label2)

        
        sine_curve1 = VMobject(color=PURE_BLUE)  
        sine_curve1.set_points_smoothly(
            [
                np.array([x, np.sin((-PI/2)*x), 0]) for x in np.arange(-2, 0, 0.001)
            ]
        )
        sine_curve2 = VMobject(color=PURE_BLUE)  
        sine_curve2.set_points_smoothly(
            [
                np.array([x, np.sin((-PI/2)*x), 0]) for x in np.arange(0, 2, 0.001)
            ]
        )
        sine_curve3 = VMobject(color=GRAY)
        sine_curve3.set_points_smoothly(
            [
                np.array([x, np.sin((-PI/2)*x), 0]) for x in np.arange(0, 2, 0.001)
            ]
        )
        dotsin = DashedVMobject(sine_curve3)
        sine_curve4 = VMobject(color=PURE_BLUE)  
        sine_curve4.set_points_smoothly(
            [
                np.array([x, abs(np.sin((-PI/2)*x)), 0]) for x in np.arange(0, 2, 0.001)
            ]
        )


        sin_text = MathTex(r'f(x) = sen(x)', font_size=27, color = PURE_BLUE)
        sin_text.move_to([0.0,1.5,0.0])

        modsin_text = MathTex(r'g(x) = |sen(x)|', font_size=27, color = PURE_BLUE)
        modsin_text.move_to([0.0,1.5,0.0])

        v_max = MathTex(r'1', font_size = 25, color= LOGO_BLACK)
        v_max.move_to([-2.1,1.0,0.0])
        v_min = MathTex(r'-1', font_size = 25, color= LOGO_BLACK)
        v_min.move_to([-2.19,-1.0,0.0])

        v_maxline = DashedVMobject(Line([-2.0,1.0,0.0],[-1.0,1.0,0.0], color = GRAY))
        v_minline = DashedVMobject(Line([-2.0,-1.0,0.0],[1.0,-1.0,0.0], color = GRAY), num_dashes=25)
        

        self.remove(title,title_trans)
        self.play(Create(axes2))
        self.play(Transform(title_trans,funcao),Write(sin_text), Succession(Create(sine_curve1), Create(sine_curve2)),run_time=3)
        self.wait(2)
        self.play(Write(v_max), Create(v_maxline), Write(v_min),Create(v_minline))
        self.wait(5)
        self.remove(sin_text)
        self.play(Succession(Transform(sin_text, modsin_text), FadeTransform(sine_curve2, dotsin)), Uncreate(v_minline), Create(sine_curve4))
        self.wait(6)
        self.remove(sin_text,modsin_text,dotsin)
        self.play(Uncreate(v_maxline), Unwrite(v_max), Unwrite(v_min), FadeOut(dotsin), Uncreate(sine_curve1),Uncreate(sine_curve4))
        self.wait()

        self.play(ax_y2.animate.shift(2*RIGHT))
        self.wait() 

        ide_curve1 = VMobject(color=RED)
        ide_curve1.set_points_smoothly(
            [
                np.array([x, x, 0]) for x in np.arange(-1, 0, 0.001)
            ]
        )

        dashed_ide = VMobject(color=GRAY)
        dashed_ide.set_points_smoothly(
            [
                np.array([x, x, 0]) for x in np.arange(-1, 0, 0.001)
            ]
        )

        dashed_ide1 = DashedVMobject(dashed_ide, color= GRAY)

        ide_curve2 = VMobject(color=RED)
        ide_curve2.set_points_smoothly(
            [
                np.array([x, x, 0]) for x in np.arange(0, 1, 0.001)
            ]
        )

        ide_curve3 = VMobject(color = RED)
        ide_curve3.set_points_smoothly([np.array([x,abs(x),0]) for x in np.arange(-1,0,0.001)])

        id_text = MathTex(r'f(x) = x', color = LOGO_BLACK, font_size =25)
        id_text.next_to(ax_y_label2, UP)

        id_text2 = MathTex(r'f(x) = |x|', color = LOGO_BLACK, font_size =25)
        id_text2.next_to(ax_y_label2, UP)




        self.play(Create(ide_curve1), Create(ide_curve2), Write(id_text))
        self.wait(4)
        self.remove(id_text)
        self.play(FadeOut(ide_curve1),Write(id_text2),Create(dashed_ide1))
        self.wait(0.1)
        self.play(Create(ide_curve3))
        self.wait(4)
        self.play(Unwrite(id_text2), Uncreate(dashed_ide1),FadeOut(ide_curve2), Uncreate(ide_curve3))
        self.wait()

        pol = VMobject(color=RED)

        pol.set_points_smoothly(
            [np.array([x,x**2 + 2*x,0]) for x in np.arange(-2.5,-2.0,0.001)]
        )
        pol1 = VMobject(color=RED)

        pol1.set_points_smoothly(
            [np.array([x,x**2 + 2*x,0]) for x in np.arange(-2.0,0.5,0.001)]
        )

        mod_pol =VMobject(color= RED)
        mod_pol.set_points_smoothly(
            [np.array([x,abs(x**2 + 2*x),0]) for x in np.arange(-2.0,0.5,0.001)] 
        )
        pol_text = MathTex(r'f(x) = x^2 + 2x', color = LOGO_BLACK, font_size=25)
        pol_text.next_to(ax_y_label2,UP)
        pol_text1 = MathTex(r'f(x) = |x^2 + 2x|', color = LOGO_BLACK, font_size=25)
        pol_text1.next_to(ax_y_label2,UP)

        pol2 = VMobject(color= PURE_BLUE)
        pol2.set_points_smoothly(
            [np.array([x,x**2 - 6*x + 5,0]) for x in np.arange(-6,6,0.001)]
        )
        pol2.scale(0.3)
        pol2.shift(1.77*DOWN)


        pol3 = VMobject(color= PURE_BLUE)
        pol3.set_points_smoothly(
            [np.array([x,abs(x**2 - 6*abs(x) + 5),0]) for x in np.arange(-6,6,0.001)]
        )
        pol3.scale(0.3)
        pol3.shift(1.77*DOWN)

        pol_text2 = MathTex(r'f(x) = |x^2 - 6|x| + 5|', color = LOGO_BLACK, font_size=25)
        pol_text2.next_to(ax_y_label2,UP)


        self.play(Create(pol), Create(pol1), Write(pol_text))
        self.wait(2)
        self.remove(pol_text)
        self.play(Uncreate(pol1),Create(mod_pol), Transform(pol_text, pol_text1))        
        self.wait()
        self.remove(pol_text,pol_text1,title,title_trans, funcao)
        self.play(Uncreate(pol), Uncreate(mod_pol), FadeOut(pol_text1))
        self.wait()
        self.play(Create(pol2))
        self.wait(2)
        self.play(Uncreate(pol2), Create(pol3), Write(pol_text2))
        self.wait()
        self.play(Uncreate(axes2), Uncreate(pol3), Unwrite(pol_text2))
        self.wait()

        call = Text('Me siga', font='Sans', weight='BOLD',font_size=14, color = BLACK)
        call_1 = Text('para mais conteúdos de Matemática', font='Sans', weight='BOLD',font_size=14, color = BLACK).next_to(call, DOWN, buff=0.5)
        call_2 = Text('@thiagosilva.fisica', font='Sans', weight='BOLD',font_size=14, color = BLACK).next_to(call_1, DOWN, buff=0.5)

        self.play(Write(call), Write(call_1), Write(call_2))
        self.wait()


        
