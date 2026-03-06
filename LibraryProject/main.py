from services.library import *

while(True):
    print("\n***********LMS******************")
    print("1. To Add Book")
    print("2. View Books ")
    print("3. Issue a Book ")
    print("4. Return a Book")
    print("5. Exit LMS")

    choice = int(input("Enter your choice : "))
    
    if choice == 1:
        add_book()

    elif choice == 2:
        view_all_books()

    elif choice == 3:
        issue_book()

    elif choice == 4:
        return_book()

    elif choice == 5:
        save_books_to_file(library)   # 🔥 FINAL SAVE
        print("Exiting LMS...")
        break
    else:
        print("Invalid choice.")