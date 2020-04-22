import csv
import os


class CarBase:

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)


    @staticmethod
    def compare(name_file):
        _, ext = os.path.splitext(name_file)
        pict = ['.jpg', '.jpeg', '.png', '.gif']
        if ext in pict:
            return True
        else:
            return False


    def get_photo_file_ext(self):
        _, ext = os.path.splitext(self.photo_file_name)
        return ext


class Car(CarBase):
    car_type = 'car'
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    car_type = 'truck'
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        try:
            self.body_length, \
                self.body_width, \
                self.body_height = body_whl.split("x")
            self.body_length, self.body_width, self.body_height = \
                float(self.body_length), \
                float(self.body_width), \
                float(self.body_height)

        except:
            self.body_length, self.body_width, self.body_height = 0.0, 0.0, 0.0

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    car_type = 'spec_machine'
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra

def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter = ';')
        next(reader)  # пропускаем заголовок
        for row in reader:

            try:
                a = row[0]
            except:
                continue

            if row[0] == 'car':
                try:
                    if not CarBase.compare(row[3])\
                            or row[1] == '' or row[5] == '' or row[2] == '':
                        continue
                    car = Car(row[1], row[3], float(row[5]), int(row[2]))
                except:
                    print('errorExept_car')
                car_list.append(car)
            if row[0] == 'truck':
                try:
                    if not CarBase.compare(row[3])\
                            or row[1] == '' or row[5] == '':
                        continue
                    truck = Truck(row[1], row[3], float(row[5]), row[4])
                except:
                    print('errorExept_truck')
                car_list.append(truck)
            if row[0] == 'spec_machine':
                try:
                    if not CarBase.compare(row[3])\
                            or row[1] == '' or row[5] == '' or row[6] == '':
                        continue
                    spec_machine = SpecMachine(row[1], row[3], float(row[5]), row[6])
                except:
                    print('errorExept_SpecMachine')
                car_list.append(spec_machine)

    return car_list
