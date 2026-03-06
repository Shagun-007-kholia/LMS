class Book:

    def __init__(self,book_id,title,author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False # Initially Book is avaliable or not given to anyone
    
    # False → Available
    # True  → Issued

    def issue_book(self):
        if self.is_issued:
            print(" Book is already issued!")
        else:
            self.is_issued = True
            print(f" Book {self.title} issued successfully")
    
    def return_book(self):
        if not self.is_issued:    # u can write/logic self.is_issused = True
            print(" Book was not issused to anyone")
        else:
            self.is_issued = False
            print(f" Book {self.title} returned successfully ")
    
    def show_details(self):
        if self.is_issued == True:
            status = "Issused"
        else:
            status = "Avaliable"
        
        print("\n--- Book Details ---")
        print(f"ID     : {self.book_id}")
        print(f"Title  : {self.title}")
        print(f"Author : {self.author}")
        print(f"Status : {status}")