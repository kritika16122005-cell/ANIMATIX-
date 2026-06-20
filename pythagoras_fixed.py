
from manim import *
import numpy as np

class PythagoreanTheoremFixed(Scene):
    def construct(self):

        # Parameters - easily changeable
        a, b = 3.0, 4.0
        c = np.sqrt(a**2 + b**2)

        title = Text("Pythagorean Theorem", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(0.8)

        # Triangle vertices - properly computed
        scale = 0.7
        A = np.array([-2.0, -1.5, 0])
        B = A + np.array([a * scale, 0, 0])
        C = A + np.array([0, b * scale, 0])

        triangle = Polygon(A, B, C, color=WHITE)
        self.play(Create(triangle))
        self.wait(0.5)

        # Right angle marker
        ra = RightAngle(Line(B, A), Line(A, C), length=0.2, color=YELLOW)
        self.play(Create(ra))
        self.wait(0.5)

        # Side labels at correct midpoints
        mid_ab = (A + B) / 2
        mid_ac = (A + C) / 2
        mid_bc = (B + C) / 2

        label_a = MathTex("a", font_size=36).move_to(mid_ab + DOWN * 0.3)
        label_b = MathTex("b", font_size=36).move_to(mid_ac + LEFT * 0.3)
        label_c = MathTex("c", font_size=36).move_to(mid_bc + RIGHT * 0.3)
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait(0.5)

        # Square on side a (RED) - outward direction is DOWN
        a_vec = B - A
        a_len = np.linalg.norm(a_vec)
        # Check outward direction
        perp_a = np.array([0, -1, 0])
        if np.dot(perp_a, C - A) > 0:
            perp_a = -perp_a
        sq_a = Polygon(
            A, B,
            B + perp_a * a_len,
            A + perp_a * a_len,
            color=RED, fill_color=RED, fill_opacity=0.4
        )
        label_a2 = MathTex("a^2", color=RED, font_size=32).move_to(sq_a.get_center())
        self.play(DrawBorderThenFill(sq_a))
        self.play(Write(label_a2))
        self.wait(0.8)

        # Square on side b (BLUE) - outward direction is LEFT
        b_vec = C - A
        b_len = np.linalg.norm(b_vec)
        perp_b = np.array([-1, 0, 0])
        if np.dot(perp_b, B - A) > 0:
            perp_b = -perp_b
        sq_b = Polygon(
            A, C,
            C + perp_b * b_len,
            A + perp_b * b_len,
            color=BLUE, fill_color=BLUE, fill_opacity=0.4
        )
        label_b2 = MathTex("b^2", color=BLUE, font_size=32).move_to(sq_b.get_center())
        self.play(DrawBorderThenFill(sq_b))
        self.play(Write(label_b2))
        self.wait(0.8)

        # Square on hypotenuse c (GREEN) - proper outward normal
        c_vec = C - B
        c_len = np.linalg.norm(c_vec)
        c_unit = c_vec / c_len
        c_perp = np.array([-c_unit[1], c_unit[0], 0])
        # Ensure outward
        if np.dot(c_perp, A - B) > 0:
            c_perp = -c_perp
        D = B + c_perp * c_len
        E = C + c_perp * c_len
        sq_c = Polygon(B, C, E, D,
                       color=GREEN, fill_color=GREEN, fill_opacity=0.4)
        label_c2 = MathTex("c^2", color=GREEN, font_size=32).move_to(sq_c.get_center())
        self.play(DrawBorderThenFill(sq_c))
        self.play(Write(label_c2))
        self.wait(1.5)

        # Identity at bottom
        identity = MathTex(
            "a^2", "+", "b^2", "=", "c^2",
            tex_to_color_map={"a^2": RED, "b^2": BLUE, "c^2": GREEN},
            font_size=48
        ).to_edge(DOWN, buff=0.4)
        self.play(Write(identity))
        self.wait(1.0)
        self.play(Flash(identity.get_center(), color=YELLOW, flash_radius=1.2))
        self.wait(1.5)
