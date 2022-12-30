from manim import *
from manim.utils.color import Colors

from histogram import Histogram

class Stack(Scene):

    def set_values(self, values:list) : 
        self.values = values
        
    def construct(self):
        values = [2,1,5,6,2,3]
        self.set_values(values)


        # Drawing title in appropriate position
        title_text = Text("Stack", color="Orange")        
        title_text.set_coord(config.top[0], 0)  # config.top is the center top point
        title_text.set_coord(config.top[1] - title_text.height - 1, 1) 
        
        self.play(DrawBorderThenFill(title_text))

        # Display the array list        
        arrays_text = list()
        indices_text = list()
        index = 0

        while index < len(values):

            val = Text(str(self.values[index]))            
            arrays_text.append(val)
            print(RIGHT)
            print(DOWN)
            val.set_coord(config.left_side[0] + (index * 1) + 1, 0) # setting x coord
            val.set_coord(config.left_side[1], 1) # setting y coord

            val_index = Text("[" + str(index) + "]", color=Colors.blue_c.value)            
            val_index.set_coord(config.left_side[0] + (index * 1) + 1, 0)
            val_index.set_coord(config.left_side[1] - 0.125, 1)
            indices_text.append(val_index)            
            val_index
            
            index += 1

        values_grp = VGroup(*arrays_text)
        indices_grp = VGroup(*indices_text)

        indices_grp.shift(DOWN)        
        self.play(Write(values_grp))
        self.play(Write(indices_grp))

