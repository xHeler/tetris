from copy import deepcopy
from os import walk
from csv import reader
from random import choice

class Shape:
    def __init__(self, path):
        # path to shapes direcory
        self.path = path
        
        # list of figures position
        self._figures_positions = []
        
        # Get figures from path
        self.collect_shape_positions()
        
    def get_random_shape(self):
        position = choice(self._figures_positions)
        return deepcopy(position)
    
    def get_shape_by_index(self, index):
        return deepcopy(self._figures_positions[index])
    
    def collect_shape_positions(self):
        list = self._get_shapes_file_list()
        self._figures_positions = []
        for index, file in enumerate(list):
            self._figures_positions.append(self._create_shape_positions(file))

    def _get_shapes_file_list(self):
        list = []
        for _, __, figures_file in walk(self.path):
            for file in figures_file:
                full_path = self.path + "/" + file
                list.append(full_path)
        return list

    def _create_shape_positions(self, file):
        positions = []
        list = self._read_file_names(file)
        
        for i in range(len(list)):
            for j in range(len(list[i])):
                if list[i][j] == '#':
                    positions.append([j, -i - 1])
        return positions
    
    def _read_file_names(self, file):
        list = []
        with open(file, 'r') as read_file:
            csv_read = reader(read_file)
            for row in csv_read:
                list.append(row)
        list.reverse()
        return list

