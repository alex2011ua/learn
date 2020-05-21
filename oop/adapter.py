class System:
    def __init__(self):
        self.map = self.grid = [[0 for i in range(30)] for _ in range(20)]
        self.map[5][7] = 1  # Источники света
        self.map[5][2] = -1  # Стены

    def get_lightening(self, light_mapper):
        self.lightmap = light_mapper.lighten(self.map)
    pass


class Light:
    def __init__(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
        self.lights = []
        self.obstacles = []

    def set_dim(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]

    def set_lights(self, lights):
        self.lights = lights
        self.generate_lights()

    def set_obstacles(self, obstacles):
        self.obstacles = obstacles
        self.generate_lights()

    def generate_lights(self):
        return self.grid.copy()


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
                if j == 1:
                    self.adaptee.lights.append(j, i)
                if j == -1:
                    self.adaptee.obstacles.append(j, i)
        map_list1 = self.adaptee.generate_lights()
        light_map = self.grid.copy()
        for i in range(l):
            for j in range(h):
                light_map.append(j, i)

        return light_map



light_mapper = MappingAdapter()
