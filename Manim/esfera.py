from manim import *

class esfera(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Criação da esfera
        sphere = Sphere(radius=1, resolution=(30, 40)).set_opacity(0.3)

        # Definição dos vértices do triângulo esférico
        vertices = [
            sphere.local_to_sphere_coords(*coords)
            for coords in [(PI / 2, PI / 2), (PI / 2, PI), (PI / 4, 3 * PI / 4)]
        ]

        # Criação das arestas do triângulo esférico
        edges = [
            ArcBetweenPoints(vertices[i], vertices[(i + 1) % 3], radius=1)
            for i in range(3)
        ]

        triangle = VGroup(*edges)

        self.add(sphere, triangle)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(5)
