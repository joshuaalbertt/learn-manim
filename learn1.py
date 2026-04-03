from manim import *
from matplotlib.pyplot import box

#1. Mobject1
class NameOfMobject(Scene):
	def construct(self):

		box = Rectangle(stroke_color = GREEN_C, stroke_opacity = 0.7,
		fill_color = RED_B, fill_opacity = 0.5, height = 1, width = 1)

		self.add(box)
		self.play(box.animate.shift(RIGHT*2), run_time = 2)
		self.play(box.animate.shift(UP*3), run_time = 2)
		self.play(box.animate.shift(DOWN*5+LEFT*5), run_time = 2)
		self.play(box.animate.shift(UP*1.5+RIGHT*1.5), run_time = 2)

#2. Mobject2
class FittingObjects(Scene):
	def construct(self):

		axes = Axes(x_range = [-3, 3], y_range = [-3, 3],
		x_length = 6, y_length = 6)
		axes.to_edge(LEFT, buff=0.5)

		self.add(axes)

		circle = Circle(stroke_width = 5, stroke_color = YELLOW,
		fill_color = GREY, fill_opacity = 0.8)
		circle.set_width(2).to_edge(DR, buff=0.5)

		triangle = Triangle(stroke_width = 5, stroke_color = ORANGE,
		fill_color = GREY, fill_opacity = 0.8)
		triangle.set_height(2).shift(DOWN*3+RIGHT*3)

		self.play(Write(axes), run_time = 2)
		self.play(DrawBorderThenFill(circle), run_time = 2)
		self.play(circle.animate.set_width(1), run_time = 2)
		self.play(Transform(circle, triangle), run_time = 3)

#3. Updaters1
class Updaters(Scene):
	def construct(self):

		rectangle = RoundedRectangle(stroke_color = WHITE, stroke_width = 8,
		fill_color = BLUE_B, width = 4.5, height = 2).shift(UP*3+LEFT*4)

		mathtext = MathTex("\\frac{3}{4} = 0.75").set_color_by_gradient(GREEN, PINK).set_height(1.5)
		mathtext.move_to(rectangle.get_center())
		mathtext.add_updater(lambda x: x.move_to(rectangle.get_center()))

		self.play(FadeIn(rectangle), run_time = 2)
		self.play(Write(mathtext), run_time = 2)
		self.play(rectangle.animate.shift(RIGHT*1.5+DOWN*5), run_time = 3)
		self.wait(1)
		mathtext.clear_updaters()
		self.play(rectangle.animate.shift(RIGHT*2+UP*3), run_time = 2)

#4. Updaters2
class Updaters2(Scene):
	def construct(self):
    # Tracks the value of the radius
		r = ValueTracker(0.5)

		circle = always_redraw(lambda:
			Circle(radius = r.get_value(), stroke_color = YELLOW, stroke_width = 5)
		)

		line_radius = always_redraw(lambda:
			Line(start = circle.get_center(), end = circle.get_bottom(), stroke_color = RED_B, stroke_width = 10)
		)

		line_circumference = always_redraw(lambda:
			Line(stroke_color = WHITE, stroke_width = 5
			).set_length(2 * r.get_value() * PI).next_to(circle, DOWN, buff=0.2)
		)

		triangle = always_redraw(lambda:
			Polygon(circle.get_bottom(), circle.get_left(), circle.get_right(), fill_color = GREEN_C)
		)

		self.play(LaggedStart(
			Create(circle), DrawBorderThenFill(line_radius), DrawBorderThenFill(triangle),
			run_time = 4, lag_ratio = 0.75
		))

		self.play(ReplacementTransform(circle.copy(), line_circumference), run_time = 2)
		self.play(r.animate.set_value(3), run_time = 3)

