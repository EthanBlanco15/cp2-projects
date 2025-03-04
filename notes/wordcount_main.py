import wordcount_file
import wordcount__time

def main():
    file = input("Enter the file name: ")

    try:
        content = wordcount_file.read_file(file_name)
        word_count = wordcount_file.count_words(content)
        timestamp = wordcount_time.get_timestamp()

        updated_content = file_handler.append_metadata(content, word_count, timestamp)
        wordcount_file.write_file(file_name, updated_content)

        print(f"Updated {file_name} with word count: {word_count} and timestamp: {timestamp}")

    except FileNotFoundError:
        print("Error: File not found. Please check the file name and try again.")
    main()
