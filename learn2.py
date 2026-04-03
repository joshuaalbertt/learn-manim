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

#3. Murltiple Axes
class MultipleAxes(Scene):
    def construct(self):

        plane = NumberPlane(x_range = [-4, 4, 1], x_length=4,
                            y_range = [0, 20, 5], y_length=4).add_coordinates()
        plane.shift(DOWN*1.5+LEFT*4)
        plane_graph = plane.plot(lambda x : x**2, x_range=[-4, 4],
                                  color = GREEN)
        area = plane.get_riemann_rectangles(plane_graph, x_range=[-4, 4], dx=0.05,
                                            color=[YELLOW, BLUE])


        axes = Axes(x_range=[-4, 4, 1], y_range=[-20, 20, 5],
                    x_length=4, y_length=4).add_coordinates()
        axes.shift(DOWN*1.5+RIGHT*4)
        axes_graph = axes.plot(lambda x : x**2, x_range=[-4, 4],
                                color=RED)
        v_lines = axes.get_vertical_lines_to_graph(axes_graph, x_range=[-3, 3], num_lines=12,
										color=YELLOW)

        self.play(Write(plane), Create(axes))
        self.play(Create(plane_graph), Create(axes_graph), run_time = 2)
        self.play(Create(area), Create(v_lines), run_time = 2)

#4. Polar plane & updaters
class Tute2(Scene): #ILLUSTRATING POLAR PLANE WITH A SINE CURVE
    def construct(self):

        e = ValueTracker(0.01) #Tracks the end value of both functions

        plane = PolarPlane(radius_max=3).add_coordinates()
        plane.shift(LEFT*2)
        graph1 = always_redraw(lambda :
            ParametricFunction(lambda t : plane.polar_to_point(2*np.sin(3*t), t),
            t_range = [0, e.get_value()], color = GREEN)
        )
        dot1 = always_redraw(lambda : Dot(fill_color = GREEN, fill_opacity = 0.8).scale(0.5).move_to(graph1.get_end()))

        axes = Axes(x_range = [0, 4, 1], x_length=3, y_range=[-3,3,1], y_length=3).shift(RIGHT*4)
        axes.add_coordinates()
        graph2 = always_redraw(lambda :
            axes.plot(lambda x : 2*np.sin(3*x), x_range = [0, e.get_value()], color = GREEN)
        )
        dot2 = always_redraw(lambda : Dot(fill_color = GREEN, fill_opacity = 0.8).scale(0.5).move_to(graph2.get_end()))

        title = MathTex("f(\\theta) = 2\sin(3\\theta)", color = GREEN).next_to(axes, UP, buff=0.2)

        self.play(LaggedStart(
            Write(plane), Create(axes), Write(title),
            run_time=3, lag_ratio=0.5
        ))

        self.add(graph1, graph2, dot1, dot2)
        self.play(e.animate.set_value(PI), run_time = 10, rate_func = linear)
        self.wait() 
