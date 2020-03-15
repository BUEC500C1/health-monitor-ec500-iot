from data_socket import FakeDataSender

try:
    s = FakeDataSender("bp.socket", 80, 200, 1)
    s.get_connection()
except KeyboardInterrupt:
    s.close()
