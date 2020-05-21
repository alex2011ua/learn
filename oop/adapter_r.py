
class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, grid):
        self.grid = grid
        l = len(self.grid[1])
        h = len(self.grid[0])
        self.adaptee.set_dim((l, h))

        for i in range(l):
            for j in range(h):

                if self.grid[i][j] == 1:
                    self.adaptee.lights.append(j, i)
                if self.grid[i][j] == -1:
                    self.adaptee.obstacles.append(j, i)
        map_list1 = self.adaptee.generate_lights()
        light_map = self.grid.copy()
        for i in range(l):
            for j in range(h):
                light_map.append(map_list1[j][i])

        return light_map
