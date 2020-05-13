import asyncio


class ClientServerProtocol(asyncio.Protocol):
    def __init__(self):
        self.data = {}

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):

        resp = self.process_data(data.decode())

        resp = resp+"\n"
        self.transport.write(resp.encode())

    def process_data(self, tekst):

        try:
            command, load = tekst.split(" ", 1)
        except:
            return "error\nwrong command\n"
        load = load.strip()
        if not load:
            return "error\nwrong command\n"
        if command == "put":
            return self.put(load)
        elif command == "get":
            return self.get(load)
        else:
            return "error\nwrong command\n"

    def put(self, put_text):
        try:
            key, value, timestamp = put_text.split()

            if key not in self.data:
                self.data[key] = []
            self.data[key].append((float(value), int(timestamp)))
            return "ok\n"
        except:
            return "error\nwrong command\n"

    def get(self, put_text):
        if ' ' in put_text:
            return "error\nwrong command\n"
        answer = "ok\n"
        if put_text == "*":
            for key in self.data:
                answer = answer + self.text_dict(key, self.data[key])
            return answer
        else:
            if put_text in self.data:
                return answer + self.text_dict(put_text, self.data[put_text])
            else:
                return answer



    def text_dict(self, key, lis):
        text_key = ""
        for item in lis:
            f, s = item
            text_key = text_key + f"{key} {f} {s}\n"
        return text_key



def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

run_server('127.0.0.1', 8888)
'''
loop = asyncio.get_event_loop()
coro = loop.create_server(
    ClientServerProtocol,
    '127.0.0.1', 8181
)

server = loop.run_until_complete(coro)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()'''