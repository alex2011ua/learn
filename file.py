import os
import tempfile


class File():
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        if not os.path.exists(path_to_file):
            with open(self.path_to_file, 'w'):
                pass

    def read(self):
        with open(self.path_to_file, 'r') as file:
            line = file.readline()
            return line

    def write(self, line):
        with open(self.path_to_file, 'w') as file:
            return file.write(line)

    def __add__(self, other):
        storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
        new_file = File(storage_path)
    def __str__(self):
        return self.path_to_file


def main():
    path_to_file = "d:\\test\\1.txt"
    print(os.path.exists(path_to_file))

    f = File(path_to_file)
    print(os.path.exists(path_to_file))
    print(f.read())
    print(f.write('some text'))
    print(f)

if __name__ == '__main__':
    main()
