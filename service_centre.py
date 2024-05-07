import queue
import time
import random

# Створення черги заявок
request_queue = queue.Queue()

def generate_request():
	# Генерація нової заявки
	request_id = random.randint(1, 1000)  # Унікальний номер заявки (можна змінити)
	new_request = f"Request ID: {request_id}"
	
	# Додавання заявки до черги
	request_queue.put(new_request)
	print(f"New request generated: {new_request}")

def process_request():
	if not request_queue.empty():
		# Видалення заявки з черги для обробки
		request = request_queue.get()
		print(f"Processing request: {request}")
		# Імітація обробки заявки 
		time.sleep(2)
		print(f"Request {request} processed.")
	else:
		print("Queue is empty. No requests to process.")

# Головний цикл програми
if __name__ == "__main__":
	while True:
		# Генерація нових заявок
		generate_request()
		
		# Обробка заявок
		process_request()
		
		# Затримка перед наступною ітерацією (імітація постійної роботи)
		time.sleep(2)
