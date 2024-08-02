from manim import *

SCALE_FACTOR = 0.8

tmp_pixel_height = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = tmp_pixel_height

config.frame_height = config.frame_height/SCALE_FACTOR
config.frame_width = config.frame_height * 9/16

FRAME_HEIGHT = config.frame_height
FRAME_WIDTH = config.frame_width

class mcu(MovingCameraScene):
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
        title = MarkupText('Movimento Circular Uniforme',gradient=(RED, YELLOW), font='Sans', weight='NORMAL',font_size = 25)
        title.move_to([0.,3.8,0.])
        sub_title = MarkupText('M.C.U',gradient=(RED, YELLOW), font='Sans', weight='NORMAL',font_size = 25)
        sub_title.move_to([0.,3.8,0.])
        arroba = Text('@thiagosilva.fisica', font='Sans', weight='BOLD',font_size=14)
        arroba.set_opacity(0.2)
        arroba.to_edge(4*DOWN)
        #self.play(Write(title), Write(arroba))
        #self.wait()

        circle = Circle(radius=1.5, color=WHITE)
        
        r = Line(circle.get_center(), circle.get_right())
        p1 = Dot(radius=0.09)
        p1.set_color(YELLOW)
        p1.next_to(r,RIGHT, buff=-0.09).set_z_index(2)

        def tangent_vector(obj, point, scale=1):
            
            direction = point - obj.get_center()
            
            tangent = rotate_vector(direction, PI/2)
            return scale * normalize(tangent)
        
        v_0 = always_redraw(lambda: Arrow(p1.get_center(), p1.get_center() + 0.5*tangent_vector(circle, p1.get_center(), scale=3), color=PURE_RED, stroke_width=4, max_tip_length_to_length_ratio=0.19, buff=0))
        
        vec_v = MathTex(r'\vec{v}', font_size = 30, color=PURE_RED)
        vec_v.add_updater(lambda m: m.next_to(v_0.get_end(), RIGHT))

        self.play(Write(title),Write(arroba),Create(circle), Create(r), Create(p1), Create(v_0), Create(vec_v))
        rotations = 6
        self.wait(0.1)

        self.play(Rotate(p1, rotations*2*PI, about_point=circle.get_center()), Rotate(r, rotations*2*PI, about_point=circle.get_center()), run_time=rotations*2, rate_func=linear)
        self.wait(0.1)
        g_1 = VGroup(circle, r, p1,v_0,vec_v)
        
        
        self.play(ShrinkToCenter(g_1))
        self.wait(0.1)
        self.play(FadeOut(g_1))


        u =  Arrow(start=[0.,0.,0.], end=[2.,0.,0.],color=PURE_RED, stroke_width=6, )
        u_1 =  Arrow(start=[0.,0.,0.], end=[3.,0.,0.],color=PURE_RED, stroke_width=6,).shift(1.2*LEFT)
     

        self.play(Create(u))
        self.wait()
        self.play(Transform(u,u_1))
        self.wait(0.5)
        self.play(Uncreate(u),Rotate(u_1, angle=PI/4))
        self.wait(0.5)
        self.play(Rotate(u_1, angle=PI))
        self.wait()
        self.play(Uncreate(u_1))

        circle = Circle(radius=1.5, color=WHITE)
        
        r = Line(circle.get_center(), circle.get_right())
        p1 = Dot(radius=0.09)
        p1.set_color(YELLOW)
        p1.next_to(r,RIGHT, buff=-0.09).set_z_index(2)

        def tangent_vector(obj, point, scale=1):
            
            direction = point - obj.get_center()
            
            tangent = rotate_vector(direction, PI/2)
            return scale * normalize(tangent)
        
        v_0 = always_redraw(lambda: Arrow(p1.get_center(), p1.get_center() + 0.5*tangent_vector(circle, p1.get_center(), scale=3), color=PURE_RED, stroke_width=4, max_tip_length_to_length_ratio=0.19, buff=0))
        
        vec_v = MathTex(r'\vec{v}', font_size = 30, color=PURE_RED)
        vec_v.add_updater(lambda m: m.next_to(v_0.get_end(), RIGHT))
        
        rotations = 6
        rotations_1 = 3
        self.wait(0.1)
        a_c = Arrow(circle.get_right(), circle.get_center(),stroke_width=4, max_tip_length_to_length_ratio=0.15, buff=0)
        a_c.set_color_by_gradient(PURE_GREEN)
        a_c_text = MathTex(r'\vec{a}_c', font_size= 30, color=PURE_GREEN)
        a_c_text.next_to(a_c.get_end(), UP, buff=0.5)
        a_c_text.add_updater(lambda t: t.next_to(a_c.get_end(),UP, buff = 0.3))


        self.play(Create(circle), Create(r), Create(p1), Create(v_0), Create(vec_v))
        self.play(Rotate(p1, rotations_1*2*PI, about_point=circle.get_center()), Rotate(r, rotations_1*2*PI, about_point=circle.get_center()), run_time=rotations_1*2, rate_func=linear)
        self.play(Create(a_c), Create(a_c_text))
        self.wait()
        self.play(Rotate(p1, rotations*2*PI, about_point=circle.get_center()), Rotate(r, rotations*2*PI, about_point=circle.get_center()),Rotate(a_c, rotations*2*PI, about_point=circle.get_center()),Rotate(a_c_text, rotations*2*PI, about_point=circle.get_center()), run_time=rotations*2, rate_func=linear)
        self.wait()

        posicao_original = self.camera.frame.get_center()
        
        update_func = lambda m, dt: m.move_to(v_0)
        self.camera.frame.add_updater(update_func)
        
        self.play(self.camera.frame.animate.scale(0.3).move_to(v_0),Rotate(p1, rotations*2*PI, about_point=circle.get_center()), Rotate(r, rotations*2*PI, about_point=circle.get_center()),Rotate(a_c, rotations*2*PI, about_point=circle.get_center()), run_time=rotations*2, rate_func=linear)

        self.camera.frame.remove_updater(update_func)

        g_2 =VGroup(circle, r, p1,v_0,vec_v, a_c, a_c_text)
        self.wait(2)
        call = Text('Me siga', font='Sans', weight='BOLD',font_size=14)
        call_1 = Text('para mais conteúdos de Física', font='Sans', weight='BOLD',font_size=14).next_to(call, DOWN, buff=0.5)
        call_2 = Text('@thiagosilva.fisica', font='Sans', weight='BOLD',font_size=14).next_to(call_1, DOWN, buff=0.5)
        self.play(self.camera.frame.animate.scale(2.5).move_to(posicao_original),FadeOut(g_2),FadeOut(title),Write(call), Write(call_1), Write(call_2))
        self.wait()


        

