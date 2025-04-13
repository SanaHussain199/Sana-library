import json
import os

data_file = 'library.txt'

def load_library():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    return []  

def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library, file, indent=4) 

def add_book(library):
    title = input('Enter the title of the book: ')
    author = input('Enter the author of the book: ')
    year = input('Enter the year of the book: ')
    genre = input('Enter the genre of the book: ')
    read = input('Have you read the book? (yes/no): ').lower() == 'yes'

    new_book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }
    
    library.append(new_book)
    save_library(library)
    print(f'Book "{title}" added successfully.')

def remove_book(library):
    title = input('Enter the title to remove from the library: ').strip().lower()
    updated_library = [book for book in library if book['title'].strip().lower() != title]

    if len(updated_library) < len(library):
        save_library(updated_library)
        print(f'Book "{title}" removed successfully.')
        return updated_library 
    else:
        print(f'Book "{title}" not found in the library.')
        return library

def search_books(library):
    search_by = input("Search by title or author: ").strip().lower()
    if search_by not in ['title', 'author']:
        print("Invalid choice! Please search by 'title' or 'author'.")
        return
    
    search_term = input(f"Enter the {search_by}: ").strip().lower()
    results = [book for book in library if search_term in book[search_by].strip().lower()]

    if results:
        print("\nSearch Results:")
        for book in results:
            status = 'Read' if book['read'] else 'Unread'
            print(f"{book['title']} by {book['author']}, {book['year']}, {book['genre']}, {status}")
    else:
        print(f"No books found matching '{search_term}' in the {search_by} field.")

def display_all_books(library):
    if library:
        print("\nLibrary Books:")
        for book in library:
            status = 'Read' if book['read'] else 'Unread'
            print(f"{book['title']} by {book['author']}, {book['year']}, {book['genre']}, {status}")
    else:
        print('Library is empty.')

def display_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book['read'])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0
    
    print(f'\nTotal Books: {total_books}')
    print(f'Read Books: {read_books}')
    print(f'Percentage of Read Books: {percentage_read:.2f}%')

def main():
    library = load_library()
    while True:
        print('\nLibrary Management System')
        print('1. Add a book')
        print('2. Remove a book')
        print('3. Search books')
        print('4. Display all books')
        print('5. Display statistics')
        print('6. Exit')

        choice = input('Enter your choice: ').strip()
        if choice == '1':
            add_book(library)
        elif choice == '2':
            library = remove_book(library)
        elif choice == '3':
            search_books(library)
        elif choice == '4':
            display_all_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            print('Goodbye!')
            break
        else:
            print('Invalid choice! Please try again.')

if __name__ == '__main__':
    main()
