### robot_test_steps.py ###
import socket


def verify_network_is_connected(host="8.8.8.8", port=53, timeout=3):
    # do somethings to verify network has been connected.
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        print(ex)
        return False
    pass


def open_browser_to_medium_page():
    # open browser to Medium Page

    pass


def verify_browser_title(title):
    assert title == "Medium"
