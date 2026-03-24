# @author Emaad Gafoor
from Book import Book

def main():
    bookList = getBooks()
    showBooks(bookList)
    
# getBooks reads books from a file and stores them into a list
# @return the list of books.
def getBooks():
    inFile = open("Books.txt", "r")
    books = []
    for line in inFile:
        (name, price, numPages) = line.rstrip().split(",")
        books.append(Book(name, float(price), int(numPages)))
    inFile.close()
    return books

# showBooks shows information for each bok
# @param books A list of books
def showBooks(books):
    for book in books:
        print(book)

main()