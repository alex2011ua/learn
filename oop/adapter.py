class System:
    def __init__(self):
        self.map = self.grid = [[0 for i in range(5)] for _ in range(2)]
        self.map[1][0] = 1  # Источники света
        self.map[0][2] = -1  # Стены


    def get_lightening(self, light_mapper):
        print (self.map)
        self.lightmap = light_mapper.lighten(self.map)
        print(self.lightmap)
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

sys = System()
light = Light((0, 0))
light_mapper = MappingAdapter(light)
sys.get_lightening(light_mapper)