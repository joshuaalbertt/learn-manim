from manim import *

#1. Graphing movement
class GraphingMovement(Scene):
    def construct(self):

        axes = Axes(x_range = [0, 5], y_range = [0, 3],
            x_length = 5, y_length = 3,
            axis_config = {"include_tip": True, "numbers_to_exclude": [0]}
        ).add_coordinates()
        axes.to_edge(UR)
        axis_labels = axes.get_axis_labels(x_label = "x", y_label = "f(x)")

        graph = axes.plot(lambda x : x**0.5, x_range = [0, 4], color = YELLOW)
        graphing_stuff = VGroup(axes, graph, axis_labels)

        self.play(DrawBorderThenFill(axes), Write(axis_labels))
        self.play(Create(graph))
        self.play(graphing_stuff.animate.shift(DOWN*4))
        self.play(axes.animate.shift(LEFT*3), run_time = 3)

#2. Number plane
class Graphing(Scene):
    def construct(self):

        my_plane = NumberPlane(x_range = [-6, 6], x_length=5,
                               y_range = [-10, 10], y_length=5,)
        my_plane.add_coordinates()
        my_plane.shift(RIGHT*3)
        
        my_function = my_plane.plot(lambda x : 0.1*x*(x-5)*(x+5), x_range = [-6, 6],
                                    color = YELLOW)

        area = my_plane.get_area(my_function, x_range = [-5, 5], color = [GREEN, BLUE])

        label = MathTex("f(x) = 0.1(x-5)x(x+5)").next_to(my_plane, UP, buff=0.2)

        horizontal_line = Line(start=my_plane.c2p(0, my_function.underlying_function(-2)),
                               end=my_plane.c2p(-2, my_function.underlying_function(-2)),
                               stroke_color=RED, stroke_width=5)

        self.play(DrawBorderThenFill(my_plane), run_time=2)
        self.play(Create(my_function), run_time=2)
        self.play(FadeIn(area), run_time=2)
        self.play(Write(label), run_time=2)
        self.play(Create(horizontal_line), run_time=2)
