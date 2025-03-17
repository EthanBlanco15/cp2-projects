import file
import time

def main(): #Main interface.

    file_name = input("Enter the file name: ")
    try:
        content = file.read_file(file_name)
        word_count = file.count_words(content)
        times = time.time()

        #Updates
        updated_content = file.append_metadata(content, word_count, times)
        file.write_file(file_name, updated_content)

        #Results
        print(f"Updated {file_name} with word count: {word_count} and timestamp: {times}")

    except FileNotFoundError: #Error checking.
        print("Error: File not found. Please check the file name and try again.")

if __name__ == "__main__": #To check if the function can run and is true.

    main()

#C:\Users\ethan.blanco\Documents\test.txt