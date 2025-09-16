M=str(input("Enter age"))
class Book:
    def __init__(book,title,pages,author):
        book.title = title
        book.pages = pages
        book.author = author

    def info(book):
     print("The book title is :" + book.title + "The book pages:" + book.pages + "The author is :" + book.author," your age is "+M)
    # def info(book):
    #     print("hsdfhsdflksd")
        
bookP = Book("Fotball","72","CR7")
# bookP.info()
bookP.info()