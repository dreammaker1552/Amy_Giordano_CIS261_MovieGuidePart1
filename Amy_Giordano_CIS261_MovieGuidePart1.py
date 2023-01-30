def display_heading_and_menu():
    print("The Movie List Program")
    print("-------------------")
    print("COMMAND MENU")
    print("list - View the list of movies")
    print("add - Add a movie to the list")
    print("del - Delete a movie from the list")
    print("exit - Exit program")

def pre_populate_list():
    movie_list = ["Forest Gump", "Cars", "Tremors", "Finding Nemo", "Kill Bill"]
    return movie_list

def display_list(movie_list):
    print("\nMovie Titles")
    print("------------")
    for i, movie in enumerate(movie_list):
        print(f"{i+1}, {movie}")

def add_title(movie_list):
    movie = input("Enter a movie title: ")
    movie_list.append(movie)
    print(f"{movie} has been added to the list.")

def delete_title(movie_list):
    number = int(input("Enter the number of the movie to delete: "))
    if number > 0 and number <= len(movie_list):
        movie = movie_list.pop(number-1)
        print(f"{movie} has been deleted from the list.")
    else:
        print("Invalid movie number.")

def main():
    display_heading_and_menu()
    movie_list = pre_populate_list()
    while True:
        command = input("\nCommand: ")
        if command == "list":
            display_list(movie_list)
        elif command == "add":
            add_title(movie_list)
            display_list(movie_list)
        elif command == "del":
            delete_title(movie_list)
            display_list(movie_list)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.")

if __name__ == "__main__":
    main()