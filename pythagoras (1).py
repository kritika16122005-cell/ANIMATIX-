
from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        title = Text("Pythagorean Theorem", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        A = np.array([-1.5, -1.0, 0])
        B = np.array([ 2.5, -1.0, 0])
        C = np.array([-1.5,  2.0, 0])

        triangle = Polygon(A, B, C, color=WHITE)
        self.play(Create(triangle))
        self.wait(0.3)

        label_a = MathTex("a").next_to(Line(A, B), DOWN, buff=0.2)
        label_b = MathTex("b").next_to(Line(A, C), LEFT, buff=0.2)
        label_c = MathTex("c").next_to(Line(B, C), RIGHT, buff=0.2)
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait(0.5)

        ra = RightAngle(Line(B, A), Line(A, C), length=0.2, color=YELLOW)
        self.play(Create(ra))
        self.wait(0.3)

        sq_a = Polygon(
            A, B,
            B + np.array([0, -4.0, 0]),
            A + np.array([0, -4.0, 0]),
            color=RED, fill_color=RED, fill_opacity=0.4
        )
        label_a2 = MathTex("a^2", color=RED).move_to(sq_a.get_center())
        self.play(DrawBorderThenFill(sq_a))
        self.play(Write(label_a2))
        self.wait(0.5)

        sq_b = Polygon(
            A, C,
            C + np.array([-3.0, 0, 0]),
            A + np.array([-3.0, 0, 0]),
            color=BLUE, fill_color=BLUE, fill_opacity=0.4
        )
        label_b2 = MathTex("b^2", color=BLUE).move_to(sq_b.get_center())
        self.play(DrawBorderThenFill(sq_b))
        self.play(Write(label_b2))
        self.wait(0.5)

        c_vec = C - B
        c_len = np.linalg.norm(c_vec)
        c_unit = c_vec / c_len
        c_perp = np.array([-c_unit[1], c_unit[0], 0])

        D = B + c_perp * c_len
        E = C + c_perp * c_len
        sq_c = Polygon(B, C, E, D,
                       color=GREEN, fill_color=GREEN, fill_opacity=0.4)
        label_c2 = MathTex("c^2", color=GREEN).move_to(sq_c.get_center())
        self.play(DrawBorderThenFill(sq_c))
        self.play(Write(label_c2))
        self.wait(1.5)

        identity = MathTex(
            "a^2", "+", "b^2", "=", "c^2",
            tex_to_color_map={"a^2": RED, "b^2": BLUE, "c^2": GREEN}
        ).scale(1.2).to_edge(DOWN, buff=0.5)

        self.play(Write(identity))
        self.wait(2)
