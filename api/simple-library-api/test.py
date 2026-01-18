#Testing grounds
book = [{'book': "Test book", 'ID': 1}]
author = [{'Author': "Bingbong", 'ID': 1}]
user_book = input("INPUT BOOK: ")
user_author = input("INPUT AUTHOR: ")

def id_gen():
    if not book:
        return 1
    else:
        ids = [books['ID'] for books in book]
        return max(ids)+1
    
def id_author():
    if not author:
        return 1
    else:
        ids = [authors['ID'] for authors in author]
        return max(ids)+1

new_book = {'book': user_book, 'ID': id_gen()}
book.append(new_book)
new_author = {'Author': user_author, 'ID': id_author()}
author.append(new_author)
combine = list(zip(book,author))

ask = input("Which book do you want to see: ")
int_ask = int(ask)

if int_ask == 1:
    print(combine[0])
elif int_ask == 2:
    print(combine[1])