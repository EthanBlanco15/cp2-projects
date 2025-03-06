import file
import time

def main():
    file_name = input("Enter the file name: ")

    try:
        content = file.read_file(file_name)
        word_count = file.count_words(content)
        timestamp = time.get_timestamp()

        updated_content = file.append_metadata(content, word_count, timestamp)
        file.write_file(file_name, updated_content)

        print(f"Updated {file_name} with word count: {word_count} and timestamp: {timestamp}")

    except FileNotFoundError:
        print("Error: File not found. Please check the file name and try again.")
if __name__ == "__main__":
    main()

#word_counter\file.py
#word_counter\time.py