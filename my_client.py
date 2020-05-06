import socket
import time


class Client:
    def __init__(self, ip, port, timeout=None):
        self.timeout = timeout
        self.sock = socket.create_connection((ip, int(port)))
        self.sock.settimeout(timeout)

    def put(self, key, value, timestamp=None):
        timestamp = timestamp or int(time.time())
        try:
            str_ = 'put ' + key + ' ' + str(value) + ' ' + str(timestamp) + '\n'
            self.sock.sendall(str_.encode("utf8"))
            data = self.sock.recv(1024)
            data_reed = data.decode("utf8")
            if 'error' in data_reed:
                raise ClientError

        except:
            raise ClientError

    def get(self, key):
        try:
            str_ = 'get ' + key + '\n'
            self.sock.sendall(str_.encode("utf8"))
            data = self.sock.recv(1024)
        except socket.timeout:
            raise ClientError

        data_reed = data.decode("utf8")
        my_list = data_reed.split("\n")
        if my_list.pop(0) != "ok":
            raise ClientError

        my_dict = {}
        for item in my_list:
            try:
                if item:
                    list_s = item.split()
                    if len(list_s) != 3:
                        raise ClientError

                    if list_s[0] in my_dict:
                        my_dict[list_s[0]].append((int(list_s[2]), float(list_s[1])))
                        my_dict[list_s[0]].sort()
                    else:
                        my_dict[list_s[0]] = [(int(list_s[2]), float(list_s[1]))]

            except:
                raise ClientError

        return my_dict

    def __del__(self):  # Деструктор
        self.sock.close()


class ClientError(BaseException):
    pass

'''def main():
    pass


if __name__ == '__main__':
    main()'''