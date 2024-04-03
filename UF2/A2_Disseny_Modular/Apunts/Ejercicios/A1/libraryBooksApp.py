def main():
    # Introduir el nombre de llibres
    num_books = int(input("Introdueix el nombre de llibres: "))

    # Diccionari per emmagatzemar la informació dels llibres
    books = {}

    # Introduir la informació de cada llibre
    for _ in range(num_books):
        title = input("Introdueix el títol del llibre: ")
        author = input("Introdueix l'autor del llibre: ")
        pages = int(input("Introdueix el nombre de pàgines del llibre: "))
        books[title] = {'author': author, 'pages': pages}

    # Mostrar la llista de llibres
    print("\nLlibres\n------------")
    for title, info in books.items():
        print(f"{title} - {info['author']} - {info['pages']} pàgines")
    print("------------")

    # Calcular el total de llibres
    total_books = len(books)
    print(f"Total: {total_books} llibres")

    # Trobar el llibre més curt
    shortest_book_title = min(books, key=lambda x: books[x]['pages'])
    shortest_book_info = books[shortest_book_title]
    print(f"Llibre més curt: {shortest_book_title} - {shortest_book_info['author']} - {shortest_book_info['pages']} pàgines")

    # Trobar el llibre més llarg
    longest_book_title = max(books, key=lambda x: books[x]['pages'])
    longest_book_info = books[longest_book_title]
    print(f"Llibre més llarg: {longest_book_title} - {longest_book_info['author']} - {longest_book_info['pages']} pàgines")

if __name__ == "__main__":
    main()
