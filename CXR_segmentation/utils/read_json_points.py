import json
import pandas as pd


class read_json_points():
    
    def __init__(self, json_file_path):
        
        self.path = json_file_path
        with open(self.path) as json_file:
            json_data = json.load(json_file)['shapes']
            
        self.data = json_data
        
    def print_labels(self):

        for i in range(len(self.data)):
            print(self.data[i]['label'])
            
            
    def read_points(self, label_name):
    
        name = str(label_name)
        data = self.data

        for i in range(len(data)):

            if (data[i]['label']) == name:
                print(name+"'s coordinates")
                return data[i]['points']
            
    def get_clavicle_r_coordinates(self, x_distance=15):
    
        """
        the input x,y means the initial coordinates from json file

        """
        initial_points = self.read_points('clavicle_r')
        
        x = []
        y = []
        
        for i in initial_points:
            x.append(i[0])
            y.append(i[1])
        
        
        df      = pd.DataFrame({'x':x, 'y':y})
        df_down = df.sort_values('x', ascending=True)        
        x_down_sort = list(df_down['x'])
        y_down_sort = list(df_down['y'])
        x_down_new = []
        y_down_new = []
        y_down_start = 0
        x_down_start = 0
        

        for i in range(len(x_down_sort)):

            # the new y values should be monotonous (y0 < y1 < y2 < ... < yn)
            # distance between the new x values should greater than "x_distance"

            if (y_down_sort[i] > y_down_start) & (abs(x_down_sort[i]-x_down_start) > x_distance):
                
                x_down_new.append(x_down_sort[i])
                y_down_new.append(y_down_sort[i])
                x_down_start = x_down_sort[i]
                y_down_start = y_down_sort[i]
                
        

        df      = pd.DataFrame({'x':x, 'y':y})
        df_up   = df.sort_values('x', ascending=False)
        x_up_sort   = list(df_up['x'])
        y_up_sort   = list(df_up['y'])
        x_up_new   = []
        y_up_new   = []
        y_up_start = 1024
        x_up_start = 1024
        
        for i in range(len(x_up_sort)):

            if (y_up_sort[i] < y_up_start) & (abs(x_up_sort[i]-x_up_start) > x_distance):

                x_up_new.append(x_up_sort[i])
                y_up_new.append(y_up_sort[i])
                y_up_start = y_up_sort[i]
                x_up_start = x_up_sort[i]

        return x_down_new, y_down_new, x_up_new, y_up_new