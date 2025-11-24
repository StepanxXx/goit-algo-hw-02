from queue import Queue

class Application:
    _number = 0
    def __init__(self, ):
        self.nama = "application-"+ str(Application._number)
        Application._number += 1

queue = Queue()


def generate_request():
    app = Application()
    queue.put(app)
    

def process_request():
    if not queue.empty():
        app = queue.get()
        print(f"Processing {app.nama}")
    else:
        print("Queue is empty")


if __name__ == "__main__":
    while True:
        generate_request()
        process_request()
