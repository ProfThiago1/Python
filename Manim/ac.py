from manim import *

SCALE_FACTOR = 0.8

tmp_pixel_height = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = tmp_pixel_height

config.frame_height = config.frame_height/SCALE_FACTOR
config.frame_width = config.frame_height * 9/16

FRAME_HEIGHT = config.frame_height
FRAME_WIDTH = config.frame_width

class ac(MovingCameraScene):
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
        title = MarkupText('Aceleração Centrípeta',gradient=(RED, BLUE), font='Sans', weight='NORMAL',font_size = 25)
        title.move_to([0.,3.8,0.])
    
        arroba = Text('@thiagosilva.fisica', font='Sans', weight='BOLD',font_size=14)
        arroba.set_opacity(0.2)
        arroba.to_edge(4*DOWN)


        theta_tracker = ValueTracker(30)
        circle = Circle(radius=1.5, color=WHITE)
        
        r = DashedLine(circle.get_center(), circle.get_right())
        r2 = DashedLine(circle.get_center(), circle.get_right())
        line_ref = r2.copy()
        r2.rotate(theta_tracker.get_value() * DEGREES, about_point=circle.get_center())
        a = Angle(r,r2, radius=0.5, other_angle=False)
        text_a = MathTex(r"\theta", font_size = 20).move_to(
            Angle(
                r, r2, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )
        text_a1 = MathTex(r"\Delta \theta", font_size = 20).move_to(
            Angle(
                r, r2, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )

        p1 = Dot(radius=0.09)
        p1.set_color(YELLOW)
        p1.next_to(r,RIGHT, buff=-0.09).set_z_index(2)

        p2 = Dot(radius=0.09, color=YELLOW)
        p2.move_to(r2.get_end()).set_z_index(2)
        
        
        p3 = Dot(radius=0.02)
        p3.move_to(circle.get_center()).set_z_index(2)


        def tangent_vector(obj, point, scale=1):
            
            direction = point - obj.get_center()
            
            tangent = rotate_vector(direction, PI/2)
            return scale * normalize(tangent)
        
        v_0 = always_redraw(lambda: Arrow(p1.get_center(), p1.get_center() + 0.5*tangent_vector(circle, p1.get_center(), scale=3), color=PURE_RED, stroke_width=4, max_tip_length_to_length_ratio=0.19, buff=0))
        
        v_1 = always_redraw(lambda: Arrow(p2.get_center(), p2.get_center() + 0.5*tangent_vector(circle, p2.get_center(), scale=3), color=PURE_RED, stroke_width=4, max_tip_length_to_length_ratio=0.19, buff=0))


        vec_v = MathTex(r'\vec{v_1}', font_size = 30, color=PURE_RED)
        vec_v.add_updater(lambda m: m.next_to(v_0.get_end(), RIGHT))
        vec_v1 = MathTex(r'\vec{v_2}', font_size = 30, color=PURE_RED)
        vec_v1.add_updater(lambda n: n.next_to(v_1.get_end(), RIGHT, buff=0.5))


        r2.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=circle.get_center()
            )
        )

        
        p2.add_updater(
            lambda k: k.move_to(r2.get_end())
        )

        a.add_updater(
            lambda x: x.become(Angle(r, r2, radius=0.5, other_angle=False))
        )

        text_a.add_updater(
            lambda x: x.move_to(
                Angle(
                    r, r2, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
                ).point_from_proportion(0.5)
            )
        )

        self.play(Write(title),Write(arroba))
        self.wait(0.1)
        self.play(Create(circle), Create(r), Create(p1), Create(v_0), Create(vec_v), Create(p3))
        self.wait(0.1)
        self.play(Create(r2),Create(p2),Create(v_1),Create(vec_v1),Create(a), Write(text_a))
        self.wait(0.5)
        self.play(theta_tracker.animate.increment_value(30), p2.animate)
        self.play(TransformMatchingTex(text_a, text_a1), run_time = 0.5)
        self.wait()

        posicao_original = self.camera.frame.get_center()

        vr_t = MathTex(r'\vec{r}', font_size = 30)
        vr_t1 = vr_t.copy()
        vr_t1.next_to(r2, LEFT, buff=0.09)
        vr_t.next_to(r,DOWN, buff= 0.4)
        dr = DashedLine(start=[1.5,-1.,0.], end=[1.5,3.4,0.])
        dr.set_z_index(0)
        dr1 = DashedLine(start=[-1.,0.,0.], end=[3.4,0,0.])
        dr1.set_z_index(0)
        dr1.rotate(5*PI/6).shift(1.6*UP + LEFT)



        a2 = Angle(dr,dr1, radius=0.5, other_angle=False)
        text_a2 = MathTex(r"\Delta \theta", font_size = 20).move_to(
            Angle(
                dr, dr1, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )
        self.play(Create(vr_t), Create(vr_t1))
        self.wait(0.1)



        vr1 = Arrow(circle.get_center(), circle.get_right(),stroke_width=4, max_tip_length_to_length_ratio=0.19, buff=0)
        vr2 = Arrow(circle.get_center(), p2.get_center(),stroke_width=4, max_tip_length_to_length_ratio=0.19, buff=0)
        delta_r = Arrow(p2.get_center(), p1.get_bottom(), color =BLUE, stroke_width=4, max_tip_length_to_length_ratio=0.19, buff=0)
        delta_r_text =MathTex(r'\Delta \vec{r}', font_size= 30)
        delta_r_text.next_to(delta_r,RIGHT, buff=0.5)


        self.play(Create(dr), Create(dr1),self.camera.frame.animate.move_to(a2).scale(0.5),Create(a2), Create(text_a2), v_0.animate.set_opacity(0.1),v_1.animate.set_opacity(0.1) )
        self.wait()
        self.play(a2.animate.set_fill(BLUE, opacity=0.6))
        self.wait()
        self.play( v_0.animate.set_opacity(1),v_1.animate.set_opacity(1),a.animate.set_fill(BLUE, opacity=0.6),self.camera.frame.animate.scale(2).move_to(posicao_original),Create(vr1),Create(vr2),Create(delta_r),Create(delta_r_text), Uncreate(a2),Uncreate(text_a2), Uncreate(dr), Uncreate(dr1))
        self.wait(0.1)

       

        delta_r_text.add_updater(
            lambda j: j.move_to(delta_r.get_center(),3*DOWN)
            )
        vr_t.add_updater(
            lambda p: p.next_to(vr1.get_center(),RIGHT, buff= 0.3)
        )
        vr_t1.add_updater(
            lambda q: q.next_to(vr2.get_center(), LEFT, buff = 0.3)
        )

        g1 = VGroup(circle, r,r2,p1,p2,p3, a,text_a1, v_0, v_1,vec_v,vec_v1)
        g2 = VGroup(vr1, vr2, delta_r,delta_r_text,vr_t,vr_t1)
        

        v2 =Arrow(v_0.get_bottom(), v_0.get_end(), color=PURE_RED, stroke_width=4, max_tip_length_to_length_ratio=0.19, buff=0)
        v3 = Arrow(v2.get_bottom(), v2.get_end(), color=PURE_RED, stroke_width=4, max_tip_length_to_length_ratio=0.19, buff=0)
        v3.rotate(PI/6).shift(0.1*DOWN+0.35*LEFT)
        
        vec_v2 = MathTex(r'\vec{v_1}', font_size = 30, color=PURE_RED)
        vec_v2.add_updater(lambda m: m.next_to(v2.get_end(), RIGHT))
        vec_v3 = MathTex(r'\vec{v_2}', font_size = 30, color=PURE_RED)
        vec_v3.add_updater(lambda n: n.next_to(v3.get_end(),LEFT, buff=0.3))

        v4 =Arrow(v2.get_end(), v3.get_end(), color=PURE_RED, stroke_width=4, max_tip_length_to_length_ratio=0.19, buff=0)

        vec_v4= MathTex(r'\Delta \vec{v}', font_size = 30, color=PURE_RED)
        vec_v4.add_updater(lambda b: b.next_to(v4.get_center(), UP))

        a3 = Angle(v2, v3, radius=0.5, other_angle=False)
    
        

        a_34_n = MathTex(r'\Delta \theta', font_size =25).move_to(
            Angle(
                v2, v3, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )

        self.play(FadeOut(g1), g2.animate.rotate(PI/3).shift(2*LEFT), delta_r_text.animate.rotate(-PI/70).shift(1*UP), )
        self.wait(0.1)
        self.play(Create(v2), Create(v3), Create(vec_v2), Create(vec_v3),Create(v4),Create(vec_v4),Create(a3), Create(a_34_n ))
        self.wait(0.1)

        a4 =  Angle(vr1,vr2, radius=0.5, other_angle=False)
        text_a4 =  MathTex(r"\Delta \theta", font_size = 18).move_to(
            Angle(
                vr1, vr2, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )
        self.play(Create(a4), Create(text_a4))
        self.wait(0.1)

        g3 =VGroup(vr_t, vr_t1, vr1, vr2, delta_r,delta_r_text, a4, text_a4)
        g3.generate_target()
        g3.target.shift(2*UP)

        g4 = VGroup(v2,v3, vec_v2, vec_v3, a3, a_34_n, v4, vec_v4)
        g4.generate_target()
        g4.target.shift(1.3*UP)
        self.play(MoveToTarget(g3), MoveToTarget(g4))
        self.wait(0.5)

        eq = MathTex(r'\frac{\Delta v}{v}', r'=', r'\frac{\Delta r}{r}', font_size =30)
    
        eq1 = MathTex(r'\Delta v ', r'=', r'\frac{v}{r}',r'\Delta r', font_size =30)
    
        eq2 = MathTex(r'\frac{\Delta v}{\Delta t}', r'=', r'\frac{v}{r}', r'\frac{\Delta r}{\Delta t}', font_size =30)
        eq3 = MathTex(r'\frac{\Delta v}{\Delta t}', r'=', r'\frac{v}{r}', r'v', font_size =30)
        eq4 = MathTex(r'a_{cp}', r'=', r'\frac{v^2}{r}', font_size =30)

        self.play(Write(eq))
        self.wait(0.5)
        self.play(TransformMatchingTex(eq,eq1))
        self.wait(0.5)
        self.play(TransformMatchingTex(eq1,eq2))
        self.wait(0.5)
        self.play(TransformMatchingTex(eq2,eq3))
        self.wait(0.5)
        self.play(TransformMatchingTex(eq3,eq4))
        self.wait(0.5)

        self.play(FadeOut(g3), FadeOut(g4), eq4.animate.shift(2.6*UP).scale(0.8))
        rect = SurroundingRectangle(eq4)
        rect.set_color_by_gradient(RED,BLUE)

        self.play(Create(rect))
        self.wait()

        a_c = always_redraw(lambda: Arrow(p2.get_center(), circle.get_center(),stroke_width=4, max_tip_length_to_length_ratio=0.15, color=PURE_GREEN, buff=0))
    
       
        a_c_text = MathTex(r'\vec{a}_{cp}', font_size= 30, color=PURE_GREEN)
        a_c_text.next_to(a_c.get_end(), UP, buff=0.5)
        a_c_text.add_updater(lambda t: t.next_to(a_c.get_end(),UP, buff = 0.3))

        self.play(Create(circle), Create(r), Create(p1), Create(v_0), Create(vec_v), Create(p3))
        self.wait(0.1)
        self.play(Create(r2),Create(p2),Create(a_c),Create(a_c_text),Create(v_1),Create(vec_v1),Create(a), Write(text_a))
        self.wait(0.5)
        self.play(theta_tracker.animate.increment_value(330), p2.animate, Uncreate(p1), Uncreate(v_0), Uncreate(vec_v))
        self.play(TransformMatchingTex(text_a, text_a1), run_time = 0.5)
        self.wait()

        g5 = VGroup(a_c, a_c_text, rect, eq4, title, circle, p2,p3,a,text_a1, v_1, r, vec_v1, r2)
        call = Text('Me siga', font='Sans', weight='BOLD',font_size=14)
        call_1 = Text('para mais conteúdos de Física', font='Sans', weight='BOLD',font_size=14).next_to(call, DOWN, buff=0.5)
        call_2 = Text('@thiagosilva.fisica', font='Sans', weight='BOLD',font_size=14).next_to(call_1, DOWN, buff=0.5)
        self.play(FadeOut(g5))
        self.wait(0.1)
        self.play(Write(call), Write(call_1), Write(call_2))

        self.wait(2)