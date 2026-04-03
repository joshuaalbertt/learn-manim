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

#3. Updaters
