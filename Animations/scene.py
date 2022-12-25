from manim import *

class Histogram(Scene):            
    def construct(self):

        values = [2,1,5,6,2,3]
        chart = BarChart(
            values=values,
            bar_names=["two", "one", "five", "six", "two", "three"],
            y_range=[-2, 10, 1],
            y_length=10,
            x_length=10,
            x_axis_config={"font_size": 36},            
        )

        c_bar_lbls = chart.get_bar_labels(
            color=WHITE, label_constructor=MathTex, font_size=36
        )

        y_axis = chart.get_y_axis()        
        x_axis = chart.get_x_axis()                                
        d_lines = []

        # Creating horizontal lines for reference

        for i in values:
            print(y_axis.number_to_point(i)[1])
            dashed_line = DashedLine(config.left_side, config.right_side)
            d_lines.append(dashed_line)
            left_point = y_axis.number_to_point(i)            
            right_point = y_axis.number_to_point(i)
            right_point[0] = config.right_side[0]
            dashed_line.put_start_and_end_on(left_point, right_point)
            

        group_lines = VGroup(*d_lines)

        # playing the different lines
        self.play(DrawBorderThenFill(chart))        
        self.add(chart, c_bar_lbls)
        self.play(Create(c_bar_lbls))           
        self.play(DrawBorderThenFill(group_lines))            
    

