from manim import *

SCALE_FACTOR = 0.8

tmp_pixel_height = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = tmp_pixel_height

config.frame_height = config.frame_height/SCALE_FACTOR
config.frame_width = config.frame_height * 9/16

FRAME_HEIGHT = config.frame_height
FRAME_WIDTH = config.frame_width


class work(Scene):
    def setup(self, add_border = False):
        if add_border:
            self.border = Rectangle(
                width=FRAME_WIDTH,
                height=FRAME_HEIGHT,
                    color = WHITE
            )
            self.add(self.border)
    
    def construct(self):
        text_title = Text('Teorema Trabalho-Energia', font_size = 25)
        text_title.to_edge([0.,1.,0.]).set_color(ORANGE)

        text_i = Text('Você consegue resolver em 5 s ?', font_size=25)
        text_i.to_edge([0.,1., 0.]).set_color(ORANGE)

        a = Text('@thiagosilva.fisica', font='Sans', weight='BOLD',font_size=14)
        a.set_opacity(0.2)
        a.to_edge(1*DOWN)


        bloco = Rectangle(height=0.8, width=0.8, color=ORANGE)
        bloco.set_fill(color=ORANGE, opacity=0.6).to_edge(0.5*LEFT)

        text_m = Text('m', font_size= 25, color=WHITE).set_z_index(2)
        text_m.add_updater(lambda m: m.move_to(bloco.get_center()))
        bloco_path_c = TracedPath(bloco.get_center, dissipating_time=0.5, stroke_opacity=[0,1])
        bloco_path_l1 = TracedPath(bloco.get_left, dissipating_time=0.5, stroke_opacity=[0,1])

        line_d = Line(LEFT, [5.5,0.,0.])
        line_d.to_edge(0.5*LEFT)
        line_d.next_to(bloco,DOWN, buff=0)

        v_0 = MathTex(r'v_0 = 10 \ m/s', font_size = 25)
        v_0.next_to(bloco, UP, buff=0.2).shift(0.5*RIGHT)
        v_1 = MathTex(r'v_1 = 0 \ m/s', font_size = 25)
        v_1.shift(1.2*RIGHT + 0.79*UP)
        mass = MathTex(r'm= 2\  kg', font_size = 25)
        desloc = MathTex(r'd', font_size = 25)
        
        work_j = MathTex(r'W =  ?', font_size = 25)
        work_ec = MathTex(r'W=', r'\Delta E_c', font_size =25)    
        d_ec = MathTex(r'\Delta E_c =', r'\frac{mv_f^2}{2} - \frac{mv_i^2}{2}', font_size =25)
        vals = MathTex(r'\frac{(2 kg)(0 m/s)^2}{2} - \frac{(2 kg)(10 m/s)^2}{2}', r'- 100 \ J', font_size = 25)
        work = MathTex(r'W = - 100 \ J', font_size = 25)


        self.play(Write(text_i))
        self.wait(1)

        self.add(bloco, bloco_path_c, bloco_path_l1,text_m, a)

        self.play(bloco.animate.shift(3.5*RIGHT).set_z_index(2), Create(line_d.set_z_index(0)))
        self.wait(1)

        self.play(Write(desloc.next_to(line_d, DOWN, buff=0.4).shift(1.5*RIGHT)))
        self.wait(1)
        self.play(Write(v_0), Write(v_1))
        self.wait(1.5)
        self.play(Write(mass.to_edge([0.,6.,0])))
        self.wait(2)
        self.play(Create(work_j.to_edge([0.,5.,0.])))
        self.wait(7)
        self.play(Transform(text_i, text_title))
        self.play(work_j.animate.shift(1*UP + 1.9*LEFT).scale(0.9), mass.animate.shift(1.5*UP + 1*LEFT).scale(0.9), v_0.animate.shift(2.68*UP+1.9*RIGHT).scale(0.9), v_1.animate.shift(2.6*UP + 0.4*RIGHT).scale(0.9))
        self.wait(2)
        self.play(Write(work_ec.shift(1.5*UP)))
        self.wait(2)
        self.play(Unwrite(work_ec), Write(d_ec.shift(1.5*UP+1.1*LEFT)))
        self.wait()
        self.play(Unwrite(d_ec[1]), Write(vals[0].shift(1.5*UP+0.5*RIGHT).scale(0.8)))
        self.wait()
        self.play(Unwrite(vals[0]), Write(vals[1].shift(1.5*UP+2.8*LEFT)))
        self.wait(2)
        self.play(Write(work.shift(1*UP+1.7*LEFT)))
        self.wait(3)

        g_1 = VGroup(d_ec, vals, work, line_d, bloco, text_m, desloc)
        self.play(g_1.animate.shift(1.4*UP))
        self.wait(0.1)

        bloco_1 = bloco.copy()

        force = Vector([-1,0])
        force.set_color(PURE_RED)
        force.shift(0.6*DOWN)

        label_1 = MathTex(r'\vec{F}', font_size=25, color=RED)
        label_1.next_to(force, DOWN, buff=0.2)
        v_desloc = Vector([1,0])
        v_desloc.shift(0.6*DOWN)
        label_2 = MathTex(r'\vec{d}', font_size=25, color=WHITE)
        label_2.next_to(v_desloc, DOWN, buff=0.2)


        self.play(Create(bloco_1.shift(1.59*DOWN + 1.3*LEFT)), Create(force), Create(v_desloc),Write(label_1), Write(label_2))
        self.wait(4)

        w_f = MathTex(r'W = F.d.cos(\theta)', font_size=25)
        w_f.shift(2.1*DOWN)
        cos = MathTex(r'cos(\theta) =-1 \ \Rightarrow \ W = - F.d', font_size=25)
        cos.shift(2.5*DOWN)

        f = MathTex(r'W < 0', font_size=25).shift(3*DOWN )
        
      
        self.play(Write(w_f), Write(cos))
        self.wait(2)
        self.play(Write(f))
        self.wait(3)