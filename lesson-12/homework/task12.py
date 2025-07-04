# Exercise 1: Threaded Prime Number Checker

# Write a Python program that checks whether a given range of numbers contains prime numbers. Divide the range among multiple threads to parallelize the prime checking process. Each thread should be responsible for checking a subset of the range, and the main program should print the list of prime numbers found.
import threading

start = int(input('Give strating number of range: '))
end = int(input('Give ending number of range: '))
lock = threading.Lock()

#checking number is prime or not
def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

#append if the number is prime into prime_numbers list
def prime(start, end, prime_numbers):
    with lock:
        for i in range(start, end + 1):
            if is_prime(i):
                prime_numbers.append(i)

def main():
    num_threads = 4  
    prime_numbers = []
    threads = []

    total_numbers = end - start + 1
    chunk_size = total_numbers // num_threads
  
  #dividing range into chunks
    for i in range(num_threads):
        chunk_start = start + i * chunk_size
        chunk_end = start + (i + 1) * chunk_size - 1 if i != num_threads - 1 else end

        thread = threading.Thread(target=prime, args=(chunk_start, chunk_end, prime_numbers))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(prime_numbers)

main()


# Exercise 2: Threaded File Processing

# Write a program that reads a large text file containing lines of text. Implement a threaded solution to count the occurrence of each word in the file. Each thread should process a portion of the file, and the main program should display a summary of word occurrences across all threads.
import threading

lock = threading.Lock()

#reading text lines and cleaning them
with open('random.txt') as f:
    lines_list = f.readlines()
    cleaned_list = []
    symbols = [',', '.', '\n']

    for i in lines_list:
        for j in symbols:
            i = i.replace(j, '').lower()
        cleaned_list.append(i)

#finding each words occurence in the text and load them into words_count ditionary
words_count = {}

def count_words(start_index, end_index):
    local_count = {}

    with lock:
        for txt in cleaned_list[start_index:end_index+1]:
            for word in txt.split():
                if word in local_count:
                    local_count[word] += 1
                else:
                    local_count[word] = 1

        for word, count in local_count.items():
            if word in words_count:
                words_count[word] += count
            else:
                words_count[word] = count

def main():
    num_threads = 4  
    threads = []
    start = 0
    end = len(cleaned_list)
    chunk_size = end // num_threads

    for i in range(num_threads):
        chunk_start = start + i * chunk_size
        chunk_end = start + (i + 1) * chunk_size - 1 if i != num_threads - 1 else end

        thread = threading.Thread(target=count_words, args=(chunk_start, chunk_end))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


main()
print(words_count)

