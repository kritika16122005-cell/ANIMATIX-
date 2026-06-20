
from manim import *
import numpy as np

HARMONIC_COLORS = [RED, ORANGE, YELLOW, GREEN, BLUE]

def square_wave_partial(x, n_terms):
    result = 0
    for n in range(1, n_terms + 1):
        k = 2 * n - 1
        result += np.sin(k * x) / k
    return (4 / np.pi) * result

class FourierSeries(Scene):
    def construct(self):
        title = Text("Fourier Series: Square Wave Decomposition", font_size=32).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        axes = Axes(
            x_range=[0, 2 * np.pi, np.pi / 2],
            y_range=[-1.6, 1.6, 0.5],
            x_length=9,
            y_length=4.5,
            tips=False,
        ).shift(DOWN * 0.3)

        x_label = axes.get_x_axis_label(MathTex("x"), direction=RIGHT)
        y_label = axes.get_y_axis_label(MathTex("y"), direction=UP)
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.3)

        cumulative_graph = None
        prev_sum_label = None

        for i in range(5):
            n_term = i + 1
            k = 2 * n_term - 1
            color = HARMONIC_COLORS[i]

            harmonic_func = lambda x, k=k: (4 / np.pi) * np.sin(k * x) / k
            harmonic_graph = axes.plot(
                harmonic_func,
                x_range=[0, 2 * np.pi],
                color=color,
                stroke_width=2,
            )

            term_label = MathTex(
                f"n={n_term}", color=color, font_size=28
            ).to_corner(UR).shift(DOWN * (0.5 + i * 0.4))

            self.play(Create(harmonic_graph), Write(term_label), run_time=0.8)
            self.wait(0.3)

            partial_func = lambda x, n=n_term: square_wave_partial(x, n)
            new_cum_graph = axes.plot(
                partial_func,
                x_range=[0, 2 * np.pi],
                color=WHITE,
                stroke_width=2.5,
            )

            new_sum_label = MathTex(
                f"S_{{{n_term}}}(x)", color=WHITE, font_size=26
            ).to_edge(DOWN, buff=0.6)

            if cumulative_graph is None:
                self.play(Create(new_cum_graph), Write(new_sum_label))
            else:
                self.play(
                    Transform(cumulative_graph, new_cum_graph),
                    Transform(prev_sum_label, new_sum_label)
                )
                self.remove(cumulative_graph)
                self.remove(prev_sum_label)
                self.add(new_cum_graph)
                self.add(new_sum_label)

            cumulative_graph = new_cum_graph
            prev_sum_label = new_sum_label
            self.wait(0.8)

        final_label = MathTex(
            r"f(x) = \frac{4}{\pi} \sum_{n=1}^{\infty} \frac{\sin((2n-1)x)}{2n-1}",
            font_size=28, color=YELLOW
        ).to_edge(DOWN, buff=0.15)

        self.play(Transform(prev_sum_label, final_label))
        self.wait(2)
