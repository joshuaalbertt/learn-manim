from manim import *

config.pixel_width = 2560
config.pixel_height = 1440
config.frame_width = 16.0
config.frame_height = 9.0

class Banner(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        grid = NumberPlane(
            x_range=[-10, 10, 0.5],
            y_range=[-10, 10, 0.5],
            background_line_style={
                "stroke_color": WHITE,
                "stroke_width": 1.0,
                "stroke_opacity": 0.2,
            }
        )
        grid.get_axes().set_opacity(0.5)

        axes_3d = ThreeDAxes()
        surface = axes_3d.plot_surface(
            lambda u, v: 0.5 * (u**2 - v**2),
            u_range=[-4, 4],
            v_range=[-4, 4],
            colorscale=[BLUE_E, GREEN_E],
            fill_opacity=0.3,
            stroke_width=0.2,
            stroke_color=WHITE
        )

        title = Text(
            "It's Always About Patterns!",
            font_size=38,
            color=WHITE
        )

        self.add_fixed_in_frame_mobjects(title)

        self.add(grid, surface)
