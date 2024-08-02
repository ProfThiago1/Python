

from manim import *
import numpy as np

class Fibonacci(MovingCameraScene):
    def construct(self):
        fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        phi = (1 + np.sqrt(5)) / 2  # O número de ouro
        r = 0.01  # Raio inicial
        theta = 0  # Ângulo inicial
        points = [np.array((r * np.cos(theta), r * np.sin(theta), 0))]

        desired_turns = 4
        total_angle_change = desired_turns * 2 * np.pi
        angle_increment = total_angle_change / (1000 / len(fibonacci_sequence))
        theta = 0  # Zere o theta no início de cada iteração

        for i in range(len(fibonacci_sequence)):
            q_i = Square(side_length=fibonacci_sequence[i])
            self.play(Create(q_i), run_time=2)

            if i < len(fibonacci_sequence) - 1:
                for _ in range(1000):  # Agora, fazemos 1000 iterações para cada volta desejada
                    theta += angle_increment
                    r = 0.01 * np.exp(0.306349 * theta)  # Corrigindo o cálculo do raio
                    points.append(np.array((r * np.cos(theta), r * np.sin(theta), 0)))

                spiral = VMobject().set_points_smoothly(points).rotate(PI/2)
                self.play(Create(spiral), run_time=2)

        self.camera.frame.animate.scale(1.5).move_to([0., 2., 0.])





#Meu código
        
    '''self.play(Create(q_1))
    self.wait()
    self.play(Create(q_2))
    qg_1 = VGroup(q_1,q_2)
    self.wait()
    self.play(Create(q_3.next_to(qg_1,LEFT, buff =0)), self.camera.frame.animate.scale(1.5).move_to(q_3))
    qg_2 = VGroup(qg_1,q_3)
    self.wait()
    self.play(Create(q_4.next_to(qg_2,DOWN, buff=0)), self.camera.frame.animate.scale(0.8).move_to(q_4))
    qg_3 = VGroup(qg_2,q_4)
    self.wait()
    self.play(Create(q_5.next_to(qg_3,RIGHT,buff=0)), self.camera.frame.animate.scale(1.5).move_to(q_5))
    qg_4 = VGroup(qg_3,q_5)
    self.wait()
    self.play(Create(q_6.next_to(qg_4,UP, buff=0)), self.camera.frame.animate.scale(1.8).move_to(q_6))
    qg_5 =VGroup(qg_4,q_6)
    self.wait()
    self.play(Create(q_7.next_to(qg_5,LEFT,buff=0)), self.camera.frame.animate.scale(1.5).move_to(q_7))
    qg_6 =VGroup(qg_5,q_7)
    self.wait()
    self.play(Create(q_8.next_to(qg_6,DOWN,buff=0)), self.camera.frame.animate.scale(1.5).move_to(q_8))
    qg_7 = VGroup(qg_6,q_8)
    self.wait()
    self.play(Create(q_9.next_to(qg_7,RIGHT,buff=0)), self.camera.frame.animate.scale(1.5).move_to(q_9))'''