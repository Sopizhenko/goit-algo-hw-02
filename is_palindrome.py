from collections import deque

def is_palindrome(input_string):
	# Перетворення рядка у вигляд без пробілів та з нижнім регістром
	processed_string = input_string.replace(" ", "").lower()
	
	# Створення deque з обробленого рядка
	char_queue = deque(processed_string)
	
	# Порівняння символів з обох кінців черги
	while len(char_queue) > 1:
		if char_queue.popleft() != char_queue.pop():
			return False
	
	return True


if __name__ == "__main__":

	# Приклади використання функції is_palindrome():
	input_str1 = "Racecar"
	input_str2 = "hello"

	print(is_palindrome(input_str1))
	print(is_palindrome(input_str2))
