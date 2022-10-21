import socket

"""Gets the ip of the machine in the local network"""


class IP:
    local_ip: str

    def get_ip(self) -> str:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))

        self.local_ip = s.getsockname()[0]
        print(self.local_ip)
        s.close()
        return self.local_ip


ip = IP()
