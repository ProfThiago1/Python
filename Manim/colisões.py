from manim import *


SCALE_FACTOR = 0.8

tmp_pixel_height = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = tmp_pixel_height

config.frame_height = config.frame_height/SCALE_FACTOR
config.frame_width = config.frame_height * 9/16

FRAME_HEIGHT = config.frame_height
FRAME_WIDTH = config.frame_width


class cl(MovingCameraScene):
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
        title = MarkupText('Colisões',gradient=(RED, YELLOW), font='Sans', weight='NORMAL',font_size = 30)
        title.move_to([0.,3.8,0.])
        title2 = MarkupText('Colisão Elástica',gradient=(RED, YELLOW), font='Sans', weight='NORMAL',font_size = 30)
        title2.move_to([0.,3.8,0.])
        title3 = MarkupText('Colisão parcialmente Elástica',gradient=(RED, YELLOW), font='Sans', weight='NORMAL',font_size = 27)
        title3.move_to([0.,3.8,0.])

        title4 = MarkupText('Colisão Inelástica',gradient=(RED, YELLOW), font='Sans', weight='NORMAL',font_size = 30)
        title4.move_to([0.,3.8,0.])
         
        arroba = Text('@thiagosilva.fisica', font='Sans', weight='BOLD',font_size=14)
        arroba.set_opacity(0.2)
        arroba.to_edge(4*DOWN)

        p1 = Dot(radius=0.15, color=ORANGE)
        p1.set_sheen(0.3)
        p1.move_to([-10,0.,0.])

        v_0 =Arrow(start=[0.,0.,0.], end=[0.5,0.,0.], stroke_width=4, max_tip_length_to_length_ratio=0.1, buff=0).next_to(p1,RIGHT,buff=0)

        v_0.add_updater(lambda v: v.next_to(p1, RIGHT, buff=0))
        


        p2 = Dot(radius=0.15, color=PURE_BLUE)
        p2.set_sheen(0.3)
        

        p1_path = TracedPath(p1.get_center, dissipating_time=0.5, stroke_opacity =[0,1])
        p2_path = TracedPath(p2.get_center, dissipating_time=0.5, stroke_opacity =[0,1])
        
        self.play(Write(title), Write(arroba))

        posicao_original = self.camera.frame.get_center()
        update_func = lambda m, dt: m.move_to(p1)
        self.camera.frame.add_updater(update_func)

        self.wait(5)
        self.add(p1,p1_path,v_0, p2, p2_path)
        self.wait(3)
        self.play(
            ChangeSpeed(
                AnimationGroup(
                    p1.animate(run_time=1).next_to(p2.get_left(),buff=-0.299),
                    self.camera.frame.animate.scale(0.3).move_to(p1),
                    arroba.animate.move_to([0.,-1.,0.]).scale(0.5),
                    
                    
                ),
                speedinfo={0:1, 1:0},
                rate_func=linear
            ), run_time =2
        )
        self.wait(3)
        self.camera.frame.remove_updater(update_func)

        self.play(self.camera.frame.animate.move_to(posicao_original).scale(3.3), arroba.animate.to_edge(4*DOWN).scale(1.5))

        self.wait(3)

        eq  = MathTex(r'\Delta E_c', font_size = 27).move_to([0.,1.5,0.])
        eq1 = MathTex(r'\Delta E_c', r'=', r'0', font_size = 27).move_to([0.,1.5,0.])
        eq2 = MathTex(r' E_{c_i}', r'=', r'E_{c_f}', font_size = 27).move_to([0.,1.5,0.])
        eq3 = MathTex(r' E_{c_f}', r'<', r'E_{c_i}', font_size = 27).move_to([0.,1.5,0.])

        eq4 = MathTex(r'Q_A', r'=', r'mv_0', font_size= 27).move_to([0.,1.0,0.])
        eq4[2].set_color(ORANGE)
        eq5 = MathTex(r'Q_d', r'=', r'mv_0', font_size= 27).move_to([0.,1.0,0.])
        eq5[2].set_color(PURE_BLUE)
        eq6 = MathTex(r'Q_d', r'=', r'mv_1', r'+',r'mv_2' ,font_size= 27).move_to([0.,1.0,0.])
        eq6[2].set_color(PURE_BLUE)
        eq6[4].set_color(ORANGE)

        eq7 = MathTex(r'Q_d', r'=', r'2',r'mv', font_size= 27).move_to([0.,1.0,0.])
        eq7[2].set_color(ORANGE)
        eq7[3].set_color(PURE_BLUE)

        self.play(Write(eq))
        self.wait(5)
        self.remove(eq)
        self.play(Transform(eq,eq1))
        self.wait(2)
        self.remove(eq,eq1)
        self.play(Transform(eq1,eq2))
        self.wait(2)
        self.remove(title)
        self.play(Transform(title, title2))

        self.play(Indicate(p1, scale_factor=1.5), Create(eq4))
        self.wait(2)
        self.remove(eq4)
        self.play(Indicate(p2, scale_factor=1.5), TransformMatchingTex(eq4,eq5))
        self.wait(3)
        
        v_0.add_updater(lambda v: v.next_to(p2, RIGHT, buff=0))
        update_func = lambda m, dt: m.move_to(p2)
        self.camera.frame.add_updater(update_func)
        self.play(
            ChangeSpeed(
                AnimationGroup(
                    p2.animate(run_time=2).move_to([10,0.,0.]),
                    self.camera.frame.animate.scale(0.3).move_to(p2),
                    arroba.animate.move_to([0.,-1.,0.]).scale(0.5),
                    
                    
                ),
                speedinfo={0:1, 1:0},
                rate_func=linear
            )
        )

        self.camera.frame.remove_updater(update_func)
        self.remove(p2,v_0)
        self.play(self.camera.frame.animate.move_to(posicao_original).scale(3.3), arroba.animate.to_edge(4*DOWN).scale(1.5))
        
        p3 = Dot(radius=0.15, color=PURE_BLUE)
        p3.set_sheen(0.3)
        p3_path =  TracedPath(p3.get_center, dissipating_time=0.5, stroke_opacity =[0,1])

        self.add(p3,p3_path)
        self.play(Create(p3))
        self.wait()
        self.remove(title,title2, eq, eq1, eq2, eq4, eq5)
        self.play(Transform(title2, title3),Transform(eq2, eq3),TransformMatchingTex(eq5,eq6))

        v_0 = Arrow(start=[0.,0.,0.], end=[0.4,0.,0.], stroke_width=4, max_tip_length_to_length_ratio=0.1, buff=0).next_to(p1,RIGHT,buff=0)

        v_0.add_updater(lambda v: v.next_to(p1, RIGHT, buff=0))
        update_func = lambda m, dt: m.move_to(p1)

        v_1 = Arrow(start=[0.,0.,0.], end=[0.5,0.,0.], stroke_width=4, max_tip_length_to_length_ratio=0.1, buff=0).next_to(p2,RIGHT,buff=0)

        v_1.add_updater(lambda v: v.next_to(p3, RIGHT, buff=0))
        update_func = lambda m, dt: m.move_to(p3)

        self.wait(3)

        self.add(v_1, v_0)
        self.play(
            ChangeSpeed(
                AnimationGroup(
                    p3.animate(run_time=1).move_to([2,0.,0.]),
                   p1.animate(run_time=2).move_to([2,0.,0.]),
                    
                    
                ),
                speedinfo={0:1, 1:0},
                rate_func=linear
            )
        )

        self.wait(2)

        self.play(
            ChangeSpeed(
                AnimationGroup(
                    p3.animate(run_time=1).move_to([0,0.,0.]),
                   p1.animate(run_time=1).move_to([-0.3,0.,0.]),
                    
                    
                ),
                speedinfo={0:1, 1:0},
                rate_func=linear
            )
        )
        self.wait()
        self.remove(v_0,eq4, eq5, eq6)
        self.remove(title,title2, title3)
        self.play(Transform(title3,title4), TransformMatchingTex(eq6, eq7))
        self.wait(5)
        
        g1 = VGroup(p1,p3,p3_path)
        
        v_1 = Arrow(start=[0.,0.,0.], end=[0.5,0.,0.], stroke_width=4, max_tip_length_to_length_ratio=0.1, buff=0).next_to(p3,RIGHT,buff=0)
        v_1.add_updater(lambda v: v.next_to(p3, RIGHT, buff=0))
        update_func = lambda m, dt: m.move_to(g1)
        self.camera.frame.add_updater(update_func)

        self.play(
            ChangeSpeed(
                AnimationGroup(
                    g1.animate(run_time=3).move_to([5,0.,0.]),
                    self.camera.frame.animate.scale(0.3).move_to(g1)
                                    
                    
                ),
                speedinfo={0:1, 1:0},
                rate_func=linear
            )
        )
        self.camera.frame.remove_updater(update_func)
        self.play(self.camera.frame.animate.move_to(posicao_original).scale(3.3))
        call = Text('Me siga', font='Sans', weight='BOLD',font_size=14)
        call_1 = Text('para mais conteúdos de Física', font='Sans', weight='BOLD',font_size=14).next_to(call, DOWN, buff=0.5)
        call_2 = Text('@thiagosilva.fisica', font='Sans', weight='BOLD',font_size=14).next_to(call_1, DOWN, buff=0.5)
        self.remove(title, title2, title3, title4, eq, eq1,eq2,eq3, eq4, eq5, eq6, eq7)
        self.play(FadeOut(title4),Write(call), Write(call_1), Write(call_2))
        self.wait()