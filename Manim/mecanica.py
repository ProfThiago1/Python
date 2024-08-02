from manim import *
import pymunk
import numpy as np
from typing import Tuple


class Space(Mobject):
    def __init__(self, gravity: Tuple[float, float] = (0, -9.81), **kwargs):
        super().__init__(**kwargs)
        self.space = pymunk.Space()
        self.space.gravity = gravity
        self.space.sleep_time_threshold = 5

class SpaceScene(ThreeDScene):
    GRAVITY: Tuple[float, float] = (0, -9.81)

    def __init__(self, **kwargs):
        self.space = Space(gravity=self.GRAVITY)
        super().__init__(**kwargs)

    def setup(self):
        self.add(self.space)
        self.space.add_updater(lambda space, dt: self._step(dt))

    def add_body(self, body: Mobject):
        if body.body != self.space.space.static_body:
            self.space.space.add(body.body)
        self.space.space.add(body.shape)

    def make_rigid_body(
        self,
        *mobs: Mobject,
        elasticity: float = 0.8,
        density: float = 1,
        friction: float = 0.8,
    ):
        for mob in mobs:
            if not hasattr(mob, "body"):
                self.add(mob)
                mob.body = pymunk.Body()
                mob.body.position = mob.get_x(), mob.get_y()
                self.get_angle(mob)
                if not hasattr(mob, "angle"):
                    mob.angle = 0
                mob.body.angle = mob.angle
                self.get_shape(mob)
                mob.shape.density = density
                mob.shape.elasticity = elasticity
                mob.shape.friction = friction
                mob.spacescene = self

                self.add_body(mob)
                mob.add_updater(self._simulate)

            else:
                if mob.body.is_sleeping:
                    mob.body.activate()

    def make_static_body(
        self, *mobs: Mobject, elasticity: float = 1, friction: float = 0.8
    ) -> None:
        for mob in mobs:
            if isinstance(mob, VGroup) or isinstance(mob, Group):
                return self.make_static_body(*mob)
            mob.body = self.space.space.static_body
            self.get_shape(mob)
            mob.shape.elasticity = elasticity
            mob.shape.friction = friction
            self.add_body(mob)

    def stop_rigidity(self, *mobs: Mobject) -> None:
        for mob in mobs:
            if isinstance(mob, VGroup) or isinstance(mob, Group):
                self.stop_rigidity(*mob)
            if hasattr(mob, "body"):
                mob.body.sleep()

    def _step(self, dt):
        self.space.space.step(dt)

    def _simulate(self, b):
        x, y = b.body.position
        b.move_to(x * RIGHT + y * UP)
        b.rotate(b.body.angle - b.angle)
        b.angle = b.body.angle

    def get_shape(self, mob: VMobject) -> None:
        if isinstance(mob, Circle):
            mob.shape = pymunk.Circle(body=mob.body, radius=mob.radius)
        elif isinstance(mob, Line):
            mob.shape = pymunk.Segment(
                mob.body,
                (mob.get_start()[0], mob.get_start()[1]),
                (mob.get_end()[0], mob.get_end()[1]),
                mob.stroke_width - 3.95,
            )
        elif issubclass(type(mob), Rectangle):
            width = np.linalg.norm(mob.get_vertices()[1] - mob.get_vertices()[0])
            height = np.linalg.norm(mob.get_vertices()[2] - mob.get_vertices()[1])
            mob.shape = pymunk.Poly.create_box(mob.body, (width, height))
        elif issubclass(type(mob), Polygram):
            vertices = [(a, b) for a, b, _ in mob.get_vertices() - mob.get_center()]
            mob.shape = pymunk.Poly(mob.body, vertices)
        else:
            mob.shape = pymunk.Poly.create_box(mob.body, (mob.width, mob.height))

    def get_angle(self, mob: VMobject) -> None:
        if issubclass(type(mob), Polygon):
            vec1 = mob.get_vertices()[0] - mob.get_vertices()[1]
            vec2 = type(mob)().get_vertices()[0] - type(mob)().get_vertices()[1]
            mob.angle = angle_between_vectors(vec1, vec2)
        elif isinstance(mob, Line):
            mob.angle = mob.get_angle()

"""class TwoObjectsFalling(SpaceScene):
    def construct(self):
        circle = Circle().shift(UP)
        circle.set_fill(RED, 1)
        circle.shift(DOWN + RIGHT)

        rect = Square().shift(UP)
        rect.rotate(PI / 4)
        rect.set_fill(YELLOW_A, 1)
        rect.shift(UP * 2)
        rect.scale(0.5)

        ground = Line([-4, -3.5, 0], [4, -3.5, 0])
        wall1 = Line([-4, -3.5, 0], [-4, 3.5, 0])
        wall2 = Line([4, -3.5, 0], [4, 3.5, 0])
        walls = VGroup(ground, wall1, wall2)
        self.add(walls)

        self.play(
            DrawBorderThenFill(circle),
            DrawBorderThenFill(rect),
        )
        self.make_rigid_body(rect, circle)  # Mobjects will move with gravity
        self.make_static_body(walls)  # Mobjects will stay in place
        self.wait(5)"""
