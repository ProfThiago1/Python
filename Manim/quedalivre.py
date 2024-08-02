from manim import *


SCALE_FACTOR = 0.8

tmp_pixel_height = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = tmp_pixel_height

config.frame_height = config.frame_height/SCALE_FACTOR
config.frame_width = config.frame_height * 9/16

FRAME_HEIGHT = config.frame_height
FRAME_WIDTH = config.frame_width

class ql(Scene):
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
         title = MarkupText('Queda Livre',gradient=(RED, YELLOW), font='Sans', weight='NORMAL',font_size = 30)
         title.move_to([0.,3.8,0.])
         
         
         arroba = Text('@thiagosilva.fisica', font='Sans', weight='BOLD',font_size=14)
         arroba.set_opacity(0.2)
         arroba.to_edge(4*DOWN)


         # Parâmetro 'a' controla o tamanho da cardióide
         a = 0.1

        
         def x_func(t):
            return a * (2 * np.cos(t) - np.cos(2 * t))

         def y_func(t):
            return a * (2 * np.sin(t) - np.sin(2 * t))

        # Crie a cardióide
         maca = ParametricFunction(lambda t: np.array([x_func(t), y_func(t), 0]), t_range=[0, 2 * PI], fill_opacity=1, color=PURE_RED)
         maca.rotate_about_origin(angle=PI/2)

         b = 0.1

        # Funções paramétricas para x e y
         def x1_func(t):
            return b * np.sin(2 * t)

         def y1_func(t):
            return b * np.sin(t)


         marca_maca = ParametricFunction(lambda t: np.array([x1_func(t), y1_func(t), 0]), t_range=[0, PI], fill_opacity=1, color=RED)

         c=0.1
         def x2_func(t):
            return c*np.sin(2*t)

         def y2_func(t):
            return c*np.sin(t) 

    
         petala = ParametricFunction(lambda t: np.array([x2_func(t), y2_func(t), 0]), t_range=[0, PI], fill_opacity=1, color=PURE_GREEN)
         petala.next_to(marca_maca.get_left(), buff=-0.2).rotate_about_origin(angle=-PI/2)
        
         haste=Arc(angle=PI/8, color=DARK_BROWN)
         haste.next_to(petala.get_right(), buff=-0.18).set_z_index(-1)

         macag =VGroup(maca,marca_maca,petala,haste)
         macag.move_to([0.,6.0,0.])
         maca_path = TracedPath(maca.get_top, dissipating_time=0.3, stroke_opacity=[0,1])
         maca_path1 =  TracedPath(maca.get_right, dissipating_time=0.3, stroke_opacity=[0,1])
         maca_path2 =  TracedPath(maca.get_left, dissipating_time=0.3, stroke_opacity=[0,1])
         
         self.add(maca, macag, maca_path, maca_path1, maca_path2)

                

         self.play(Create(title), Write(arroba))
         self.wait(0.1)
         self.play(macag.animate.shift(10*DOWN))
         self.wait()
         self.play(FadeOut(macag, shift=DOWN))
         self.remove(maca_path,maca_path1, maca_path2)
         self.wait()
         ground_level = -2.8
         ground = Line([-2, ground_level, 0], [2, ground_level, 0])
         bala = Circle(radius=0.5, color=GRAY)
         bala.set_fill(GREY,1).shift(LEFT)
         
         
         path_bala = TracedPath (bala.get_top, dissipating_time=0.5, stroke_opacity=[0, 1])
         maca_path = TracedPath(maca.get_top, dissipating_time=0.5, stroke_opacity=[0,1])
         macag.move_to([1.5,0.,0.])
         self.add(bala, path_bala,maca,maca_path, macag)
        
         l = Line(bala.get_center(),end = [-1.0,-2.29,0.])
         l.set_opacity(0)
         l1 = Line(macag.get_center(), end= [1.5,-2.47,0.])
         l1.set_opacity(0)
         lines =VGroup(l,l1)


         res =Text('Com resistência do ar', font='Sans', font_size= 25)
         res.shift(1*UP)
         sres = Text('Sem resistência do ar', font='Sans', font_size= 25)
         sres.shift(1*UP)
         self.play(Create(ground), Create(lines))
         self.wait(5)
         self.play(Write(res))
         self.play(MoveAlongPath(bala,l,rate_func=rate_functions.ease_out_sine), MoveAlongPath(macag,l1, rate_func=rate_functions.ease_in_out_sine), run_time = 3)
         self.remove(path_bala,maca_path, bala, maca, macag)
         self.wait(5)
         self.play(Create(bala), Create(maca))
         self.wait(5)
         self.play(Transform(res,sres),MoveAlongPath(bala,l,rate_func=linear), MoveAlongPath(macag,l1, rate_func=linear), run_time = 2)
        
         self.wait(10)
         self.remove(res)
         self.play(Unwrite(sres), FadeOut(bala), FadeOut(ground), FadeOut(maca), FadeOut(macag))
         call = Text('Me siga', font='Sans', weight='BOLD',font_size=14)
         call_1 = Text('para mais conteúdos de Física', font='Sans', weight='BOLD',font_size=14).next_to(call, DOWN, buff=0.5)
         call_2 = Text('@thiagosilva.fisica', font='Sans', weight='BOLD',font_size=14).next_to(call_1, DOWN, buff=0.5)
         self.play(FadeOut(title),Write(call), Write(call_1), Write(call_2))
         self.wait()
         

         