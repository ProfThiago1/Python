from manim import *
import numpy as np

class oem(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle=Circle()
        self.set_camera_orientation(phi=80* DEGREES, theta=25* DEGREES, zoom=0.8)
        
        def param_wave1(t):
            return np.array([t, np.sin(3*t), 0])

        def param_wave2(t):
            return np.array([t, 0, np.sin(3*t)])

        wave1 = ParametricFunction(param_wave1, t_range=[-PI,1.335*PI],color=BLUE)
        wave2 = ParametricFunction(param_wave2,t_range=[-PI,1.335*PI], color=GREEN)

        self.add(axes.set_opacity(0.1))
        self.play(Create(wave1), Create(wave2), run_time = 3, rate_func = linear)
        self.wait(0.1)
        self.set_camera_orientation(phi=80* DEGREES, theta=-55* DEGREES, zoom=1.5)
        self.play(wave1.animate.set_fill(color=BLUE,opacity=0.1), wave2.animate.set_fill(color=GREEN,opacity=0.1))
        self.wait()
