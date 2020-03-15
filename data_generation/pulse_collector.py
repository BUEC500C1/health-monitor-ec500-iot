from data_socket import FakeDataSender

try:
    s = FakeDataSender("pulse.socket", 60, 150, 1)
    s.get_connection()
except KeyboardInterrupt:
    s.close()
