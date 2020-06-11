class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, grid):
        self.grid = grid
        l = len(self.grid[0])
        h = len(self.grid)
        self.adaptee.set_dim((l, h))

        obstacles = []
        lights = []
        for i in range(h):
            for j in range(l):
                if self.grid[i][j] == 1:
                    lights.append((j, i))
                if self.grid[i][j] == -1:
                    obstacles.append((j, i))
        self.adaptee.set_lights(lights)
        self.adaptee.set_obstacles(obstacles)

        map_list = self.adaptee.generate_lights()

        return map_list