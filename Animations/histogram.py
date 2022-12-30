from manim import *
from manim.utils.color import Colors

class Histogram(Scene):            
    def construct(self):

        heights = [2,1,5,6,2,3]
        labels = ["two", "one", "five", "six", "two", "three"]
        chart = BarChart(
            values=heights,
            bar_names=labels,
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
        for i in heights:
            #print(y_axis.number_to_point(i)[1])
            dashed_line = DashedLine(config.left_side, config.right_side)
            d_lines.append(dashed_line)
            left_point = y_axis.number_to_point(i)            
            right_point = y_axis.number_to_point(i)
            right_point[0] = config.right_side[0]
            dashed_line.put_start_and_end_on(left_point, right_point)
            

        group_lines = VGroup(*d_lines)

        # Display the animations
        self.play(DrawBorderThenFill(chart))        
        self.add(chart, c_bar_lbls)
        self.play(Create(c_bar_lbls))           

               
        # Scene 2 - depict largest area algorithm    
        
        # Init stack                        
        stack_title = Text("Stack :", font_size=DEFAULT_FONT_SIZE//2).set_coord(config.top[1] - 0.25, 1)                       
        max_area_title = Text("Max area:", font_size=DEFAULT_FONT_SIZE//2).next_to(stack_title, DOWN)
        max_area_text = Text("0", font_size=DEFAULT_FONT_SIZE//2).next_to(max_area_title, RIGHT)
        area_title = Text("Area:", font_size=DEFAULT_FONT_SIZE//2).next_to(max_area_title, DOWN)
        area_text = Text("0", font_size=DEFAULT_FONT_SIZE//2).next_to(area_title, RIGHT)

        self.play(Write(stack_title))
        self.play(Write(max_area_title))
        self.play(Write(max_area_text))
        self.play(Write(area_title))
        self.play(Write(area_text))

        values_grp = VGroup()
        values_grp.next_to(stack_title, RIGHT)

        stack = list()
        max_area = 0
        i = 0
        index_text = Text("[i]", color=Colors.blue_e.value, font_size=DEFAULT_FONT_SIZE//2)       
        prev_text = stack_title         

        while i < len(heights):      
            
            index_text.next_to(c_bar_lbls[i], UP)
            self.play(Write(index_text))
                                    
            while stack and (heights[i] < heights[stack[-1]]):
                top_index = stack.pop()
                
                self.play(Unwrite(values_grp[-1]))                
                values_grp.remove(values_grp[-1]) 
                
                if len(values_grp) == 0:
                    prev_text = stack_title
                else:
                    prev_text = values_grp[-1]               

                prev_area = heights[top_index] * ((i - stack[-1] - 1) if stack else i)
                self.play(Unwrite(area_text))
                area_text = Text(str(prev_area), font_size=DEFAULT_FONT_SIZE//2).next_to(area_title, RIGHT)
                self.play(Write(area_text))

                # Drawing the arrow to represent area calculated
                bar1 = chart.bars[stack[-1] + 1] if len(stack)!=0 else chart.bars[0]
                bar2 = chart.bars[i - 1]
                
                arrow_end = bar2.get_right()
                arrow_end[1] = bar1.get_left()[1]

                white_arrow = DoubleArrow(color="WHITE", start=bar1.get_left(), end=arrow_end)                                                                

                self.play(Create(white_arrow))
                
                if prev_area > max_area:
                    self.play(Unwrite(max_area_text))
                    max_area_text = Text(str(prev_area), font_size=DEFAULT_FONT_SIZE//2).next_to(max_area_title, RIGHT)
                    self.play(Write(max_area_text))

                max_area = max(max_area, prev_area)                

            stack.append(i)
            stack_item = Text(str(heights[i]), font_size=DEFAULT_FONT_SIZE//2)
            stack_item.next_to(prev_text, RIGHT)            
            prev_text = stack_item
            values_grp.add(stack_item)            
            self.play(Write(stack_item))

            i += 1                        
        
        # emptying the stack
        while stack:
            top_index = stack.pop()
            
            self.play(Unwrite(values_grp[-1]))
            values_grp.remove(values_grp[-1])
            
            prev_area = heights[top_index] * ((i - stack[-1] - 1) if stack else i)
            
            self.play(Unwrite(area_text))
            area_text = Text(str(prev_area), font_size=DEFAULT_FONT_SIZE//2).next_to(area_title, RIGHT)
            self.play(Write(area_text))

            bar1 = chart.bars[stack[-1] + 1] if len(stack)!=0 else chart.bars[0]
            bar2 = chart.bars[i - 1]

            arrow_end = bar2.get_right()                        
            arrow_end[1] = chart.bars[top_index].get_left()[1]             
            arrow_start = bar1.get_left()
            arrow_start[1] = chart.bars[top_index].get_left()[1]

            white_arrow = DoubleArrow(color="WHITE", start=arrow_start, end=arrow_end)                                                                
            self.play(Create(white_arrow))
            
            if prev_area > max_area:
                    self.play(Unwrite(max_area_text))
                    max_area_text = Text(str(prev_area), font_size=DEFAULT_FONT_SIZE//2).next_to(max_area_title, RIGHT)
                    self.play(Write(max_area_text))

            max_area = max(prev_area, max_area)

        return max_area

