from manim import *

class UnrollingArc(ParametricFunction):
    def __init__(self, arc_range, radius=1, **kwargs):
        self.arc_range = arc_range
        self.radius = radius
        super().__init__(self.func, t_range=[0, 1], **kwargs)

    def func(self, t):
        angle = interpolate(self.arc_range[0], self.arc_range[1], t)
        return self.radius * np.array([np.cos(angle), np.sin(angle), 0])

class StackingCircles(Scene):
    def construct(self):
        # Definir raio inicial e número de iterações
        radius = 1.5
        num_iterations = 5

        # Definir altura máxima desejada
        max_height = 4.5

        # Inicializar previous_circle
        previous_circle = None

        # Iterar para criar círculos e arcos empilhados
        for i, radius_iter in enumerate(np.arange(radius, 0, -0.1)[::-1]):
            # Criar novo círculo
            n_circle = Circle(radius=radius_iter, color=YELLOW)
            n_circle.set_fill(color=YELLOW, opacity=0.6)

            # Posicionar círculo abaixo do anterior
            if previous_circle is not None:
                n_circle.next_to(previous_circle, DOWN)

            # Criar novo arco
            n_arc1 = UnrollingArc(arc_range=[-PI/2, -3*PI/2], radius=radius_iter, color=YELLOW)
            n_arc2 = UnrollingArc(arc_range=[-PI/2, PI/2], radius=radius_iter, color=YELLOW)

            # Desenrolar os arcos e transformar em linhas ao mesmo tempo
            self.play(
                FadeOut(n_circle),
                Transform(n_arc1, n_arc1.copy().rotate(PI/2, about_point=n_arc1.get_start())),
                Transform(n_arc2, n_arc2.copy().rotate(-PI/2, about_point=n_arc2.get_start()))
            )

            # Transformar os arcos em linhas
            n_line1 = Line(n_arc1.get_start(), n_arc1.get_end(), color=YELLOW)
            n_line2 = Line(n_arc2.get_start(), n_arc2.get_end(), color=YELLOW)

            # Ajustar a posição vertical das linhas
            n_line1.next_to(n_circle, UP, buff=0)
            n_line2.next_to(n_circle, UP, buff=0)

            # Adicionar as novas linhas à cena
            self.play(Transform(n_arc1, n_line1), Transform(n_arc2, n_line2))

            # Atualizar referência para o círculo atual
            previous_circle = n_line1

            self.wait(1)
