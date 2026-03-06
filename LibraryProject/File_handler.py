from models.book import Book

def save_books_to_file(library):
    try:
        with open("books_temp.txt","w") as f:
            for book in library.values():
                f.write(f"{book.book_id},{book.title},{book.author},{book.is_issued}\n")

        import os
        os.replace("books_temp.txt","books.txt")

    except Exception as e:
        print("Error while saving:", e)


def load_books_from_file(library):
    try:
        with open("books.txt","r") as f:
            for line in f:
                data = line.strip().split(",")

                if len(data) != 4:
                    print("Skipping corrupted line:", line)
                    continue

                try:
                    book_id = int(data[0])
                except ValueError:
                    print("Invalid ID:", line)
                    continue

                title = data[1]
                author = data[2]
                is_issued = data[3] == "True"

                library[book_id] = Book(book_id,title,author)
                library[book_id].is_issued = is_issued

    except FileNotFoundError:
        print("No previous records found. Starting fresh.")
