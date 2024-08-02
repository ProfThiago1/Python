from manim import *

SCALE_FACTOR = 0.8

tmp_pixel_height = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = tmp_pixel_height

config.frame_height = config.frame_height/SCALE_FACTOR
config.frame_width = config.frame_height * 9/16

FRAME_HEIGHT = config.frame_height
FRAME_WIDTH = config.frame_width

class dp(MovingCameraScene):
    def setup(self, add_border = False):
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
        title = MarkupText('Efeito Doppler',gradient=(RED, YELLOW), font='Sans', weight='NORMAL',font_size = 30)
        title.move_to([0.,3.8,0.])
        
        arroba = Text('@thiagosilva.fisica', font='Sans', weight='BOLD',font_size=14)
        arroba.set_opacity(0.2)
        arroba.to_edge(4*DOWN)

        self.play(Write(title), Write(arroba))
        self.wait()
       
       # fonte e det parados

        f = Circle(radius= 5, color = WHITE)
        f.move_to([-1.5,0.0,0.0])
        f_1 = Circle(radius = 0.15, color = WHITE)
        f_1.set_fill(opacity=1)
        f_1.move_to([-1.5,0.0,0.0])
        fonte = MathTex(r'F', font_size = 32)
        fonte.next_to(f_1, UP, buff=0.3)

        det = SVGMobject('Orelha.svg').set_z_index(3)
        det.scale(0.3)
        det.move_to([1.5,0.0,0.0])   
        detector = MathTex(r'D', font_size = 32)
        detector.next_to(det, UP, buff=0.2)

        eq = MathTex(r'f_d', r'= ', r'f_e', font_size =32)
        eq1 = MathTex(r'f_d = \frac{v_s}{\lambda}', font_size =32)

        self.play(Create(f_1), Write(fonte), Create(det), Write(detector))
        self.wait(5)
        self.play(Broadcast(f, focal_point= [-1.5,0.0,0.0], n_mobs= 10, remover =False, run_time = 5))
        self.wait()

        self.play(Write(eq))
        self.wait(3)
        self.play(TransformMatchingTex(eq,eq1))
        self.remove(eq)
        self.wait(3)
        self.play(Unwrite(eq1))
        self.wait()

        #detector se movendo
        detector.add_updater(lambda d: d.next_to(det, UP, buff=0.2))
        det.generate_target()
        det.target.move_to(f_1, RIGHT)
        
        v_d=Arrow(start=[0.,0.,0.], end=[-0.8,0.,0.], stroke_width=5, max_tip_length_to_length_ratio=0.2, buff=0).next_to(det,LEFT,buff=0)
        v_d.add_updater(lambda v: v.next_to(det, LEFT, buff=0))
        
        vd_text =MathTex(r'v_d', font_size =30)
        vd_text.next_to(v_d,UP,buff= 0.2)
        vd_text.add_updater(lambda v_t: v_t.next_to(v_d, UP, buff=0.2))

        self.play(LaggedStart(Broadcast(f, focal_point= [-1.5,0.0,0.0], n_mobs= 10, remover =False, run_time = 5), Create(v_d), Write(vd_text),ChangeSpeed(MoveToTarget(det),
        speedinfo={0:0.4, 1:0.4}, rate_func=linear), lag_ratio=0.25))
        self.wait()

        eq2 = MathTex(r'f_d = \frac{v}{\lambda}', font_size =32)
        eq3 = MathTex(r'f_d = \frac{v_s + v_d}{\lambda}', font_size =32)
        eq4 = MathTex(r'f_d = f_e \left(\frac{v_s + v_d}{v_s}\right)', font_size =32)
        eq5 = MathTex(r'f_d > f_e ', font_size =32)

        self.play(Write(eq2))
        self.wait(2)
        self.remove(eq2)
        self.play(TransformMatchingTex(eq2,eq3))
        self.wait(2)
        self.remove(eq2, eq3)
        self.play(TransformMatchingTex(eq3,eq4.shift(0.2*RIGHT)))
        self.wait(2)
        self.remove(eq2, eq3, eq4)
        self.play(TransformMatchingTex(eq4,eq5))
        self.wait(2)
        self.remove(eq2, eq3, eq5)

        # Afastamento de D

        f = Circle(radius= 20, color = WHITE)
        f.move_to([-1.5,0.0,0.0])

        det.target.move_to([-10.0,0.0,0.0])
        
        posicao_original = self.camera.frame.get_center()
        update_func = lambda m: m.move_to(det)
        self.camera.frame.add_updater(update_func)

        self.play(
            LaggedStart(Broadcast(f, focal_point= [-1.5,0.0,0.0], n_mobs= 10, remover =False, run_time = 5),self.camera.frame.animate.scale(0.8).move_to(det),arroba.animate.move_to([-10.,-2.,0.]).scale(0.8),ChangeSpeed(MoveToTarget(det),
        speedinfo={0:0.3, 1:1}, rate_func=linear), lag_ratio=0.25)
        )

        self.wait(2)
        eq6 = MathTex(r'f_d < f_e', font_size =28).move_to([-10.,2.,0.])
        eq7 = MathTex(r'f_d = f_e \left(\frac{v_s - v_d}{v_s}\right)', font_size =28).move_to([-10.,2.,0.])

        eq8 = MathTex(r'f_d = f_e \left(\frac{v_s \pm v_d}{v_s}\right)', font_size =28).move_to([-10.,2.,0.])

        self.play(Write(eq6))
        self.wait()
        self.remove(eq2, eq3, eq5,eq6)
        self.play(TransformMatchingTex(eq6,eq7))
        self.wait()
        self.remove(eq2, eq3, eq5,eq6, eq7)
        self.play(TransformMatchingTex(eq7,eq8))
        self.wait()

        self.camera.frame.remove_updater(update_func)
        self.remove(v_d,vd_text,arroba)
        
        arroba = Text('@thiagosilva.fisica', font='Sans', weight='BOLD',font_size=14)
        arroba.set_opacity(0.2)
        arroba.to_edge(4*DOWN)

        self.play(det.animate.move_to([1.5,0.0,0.0]),self.camera.frame.animate.move_to(posicao_original).scale(1.25), Write(arroba))
        self.wait(2)

        # fonte se movendo

       
        v_f=Arrow(start=[0.,0.,0.], end=[0.8,0.,0.], stroke_width=5, max_tip_length_to_length_ratio=0.2, buff=0).next_to(f_1,RIGHT,buff=0)
        
        v_f.add_updater(lambda v: v.next_to(f_1, RIGHT, buff=-0.1))
        
        vf_text =MathTex(r'v_f', font_size =30)
        vf_text.next_to(v_d,UP,buff= 0.2)
        vf_text.add_updater(lambda v_t: v_t.next_to(v_f, UP, buff=0.2))

        #f = Circle(radius= 5, color = WHITE)
        #f.move_to([-1.5,0.0,0.0])
        
        fonte.add_updater(lambda o: o.next_to(f_1, UP, buff=0.5))
       
       
        self.play(Create(v_f), Write(vf_text))
              
        x_0 = -1.5
        x_f= 1.5
        x_fti =-1.5
        x_ftf = 0.9
        r_0 = 5
        step = 0.1
        r_step = 0.2

        frentes_de_onda = []

        while x_0 < x_f and x_fti < x_ftf:
            x_0 +=step
            x_fti+=step
            r_0 -= r_step
            if r_0 < 0:
                r_0 =0
            
            f_s = Circle(radius=r_0, color=WHITE).move_to([x_0, 0, 0])
            frentes_de_onda.append(f_s)
            f_1.generate_target()
            f_1.target.move_to([x_fti,0.0,0.0])
            self.play(ChangeSpeed(AnimationGroup(MoveToTarget(f_1),Broadcast(f_s, focal_point=f_1.get_center(), n_mobs=1), Create(f_s)),
            speedinfo={0:1, 1:1}, rate_func=linear ))
        self.wait()

        posicao_original = self.camera.frame.get_center()
    
        self.play(self.camera.frame.animate.scale(2))
        self.wait(2)
        self.play(*[FadeOut(f_s) for f_s in frentes_de_onda])
        
        self.play(self.camera.frame.animate.move_to(posicao_original).scale(0.5))
        self.wait()

        eq9 = MathTex(r'f_d > f_e', font_size =28).move_to([0.0,2.0,0.0])
        eq10 = MathTex(r'f_d =f_e \left(\frac{v_s}{v_s-v_f}\right)', font_size =28).move_to([0.0,2.0,0.0])
        eq11 = MathTex(r'f_d =f_e \left(\frac{v_s}{v_s \pm  v_f}\right)', font_size =28).move_to([0.0,2.0,0.0])
        
        self.play(Write(eq9))
        self.wait()
        self.remove(eq9)
        self.play(TransformMatchingTex(eq9,eq10))
        self.wait(2)
        self.remove(eq9,eq10)
        self.play(TransformMatchingTex(eq10,eq11))
        self.wait(2)
        self.remove(eq9,eq10)
        self.play(FadeOut(eq11))
        
        
        #movimento dos dois

        self.play(f_1.animate.move_to([-1.5,0.0,0.0]))
        self.wait()
        
        x_0 = -1.5
        x_f= 1.5
        x_fti =-1.5
        x_ftf = 0.0
        x_di = 1.5
        r_0 = 5
        step = 0.1
        r_step = 0.2

        frentes_de_onda = []
        self.play(Create(v_d), Write(vd_text))

        while x_0 < x_f and x_fti < x_ftf:
            x_0 +=step
            x_fti+=step
            r_0 -= r_step
            x_di -=step
            if r_0 < 0:
                r_0 =0
            
            f_s = Circle(radius=r_0, color=WHITE).move_to([x_0, 0, 0])
            frentes_de_onda.append(f_s)
            f_1.generate_target()
            f_1.target.move_to([x_fti,0.0,0.0])

            self.play(ChangeSpeed(AnimationGroup(MoveToTarget(f_1),det.animate.move_to([x_di,0.0,0.0]),Broadcast(f_s, focal_point=f_1.get_center(), n_mobs=1), Create(f_s)),
            speedinfo={0:1, 1:1}, rate_func=linear ))


        eq12 = MathTex(r'f_d =f_e \left(\frac{v_s \pm v_d}{v_s \pm  v_f}\right)', font_size =30).move_to([0.0,2.0,0.0])

        self.play(*[FadeOut(f_s) for f_s in frentes_de_onda], Write(eq12))

        self.wait(4)
        
        call = Text('Me siga', font='Sans', weight='BOLD',font_size=14)
        call_1 = Text('para mais conteúdos de Física', font='Sans', weight='BOLD',font_size=14).next_to(call, DOWN, buff=0.5)
        call_2 = Text('@thiagosilva.fisica', font='Sans', weight='BOLD',font_size=14).next_to(call_1, DOWN, buff=0.5)

        posicao_original = self.camera.frame.get_center()
        self.play(Unwrite(eq12),Write(call_1), Write(call_2))
        self.play(self.camera.frame.animate.scale(2.5))


        x_0 = 0
        x_f= 5
        x_fti =0
        x_ftf = 5
        x_di = 0
        r_0 = 5
        step = 0.1
        r_step = 0.2

        frentes_de_onda = []
        while x_0 < x_f and x_fti < x_ftf:
            x_0 +=step
            x_fti+=step
            r_0 -= r_step
            x_di -=step
            if r_0 < 0:
                r_0 =0
            
            f_s = Circle(radius=r_0, color=WHITE).move_to([x_0, 0, 0])
            frentes_de_onda.append(f_s)
            f_1.generate_target()
            f_1.target.move_to([x_fti,0.0,0.0])

            self.play(ChangeSpeed(AnimationGroup(MoveToTarget(f_1),det.animate.move_to([x_di,0.0,0.0]),Broadcast(f_s, focal_point=f_1.get_center(), n_mobs=1), Create(f_s)),
            speedinfo={0:1, 1:1}, rate_func=linear ))
        

