from data_socket import FakeDataSender

try:
    s = FakeDataSender("oxygen.socket", 80, 100, 1)
    s.get_connection()
except KeyboardInterrupt:
    s.close()
