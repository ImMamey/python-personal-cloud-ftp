import socket

"""Gets the ip of the machine in the local network"""


class ip:
    local_ip: str

    @staticmethod
    def get_ip() -> str:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))

        local_ip = s.getsockname()[0]
        print(local_ip)
        s.close()
        return local_ip
