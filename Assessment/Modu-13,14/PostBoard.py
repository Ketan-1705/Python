from datetime import datetime


users = []
posts = []

def register():
    print("\n--- Register User ---")
    
    username = input("Enter username: ").strip()
    
    if username == "":
        print("Username cannot be empty!")
        return
    
    if username in users:
        print("Username already exists!")
        return
    
    users.append(username)
    print("Registration successful!")

def login():
    print("\n--- Login ---")
    
    attempts = 3
    
    while attempts > 0:
        username = input("Enter username: ").strip()
        
        if username in users:
            print("Login successful!")
            return username
        else:
            attempts -= 1
            print(f"Invalid username. Attempts left: {attempts}")
    
    print("Too many failed attempts!")
    return None

def create_post(username):
    print("\n--- Create Post ---")
    
    title = input("Enter title: ").strip()
    description = input("Enter description: ").strip()
    
    if title == "" or description == "":
        print("Title and Description cannot be empty!")
        return
    
    date = datetime.now().strftime("%d-%m-%Y %H:%M")
    
    post = {
        "author": username,
        "title": title,
        "description": description,
        "date": date
    }
    
    posts.append(post)
    
    print("Post created successfully!")

def view_posts():
    print("\n--- All Posts ---")
    
    if len(posts) == 0:
        print("No posts available.")
        return
    
    for i, post in enumerate(posts, start=1):
        print("\n-------------------------")
        print(f"Post #{i}")
        print("Author:", post["author"])
        print("Title:", post["title"])
        print("Date:", post["date"])
        print("Description:", post["description"])
        print("-------------------------")

def search_posts():
    print("\n--- Search Posts by Username ---")
    
    username = input("Enter username: ").strip()
    
    found = False
    
    for post in posts:
        if post["author"] == username:
            print("\n-------------------------")
            print("Author:", post["author"])
            print("Title:", post["title"])
            print("Date:", post["date"])
            print("Description:", post["description"])
            print("-------------------------")
            found = True
    
    if not found:
        print("No posts found for this user.")


def user_menu(username):
    while True:
        print(f"\n--- Welcome {username} ---")
        print("1. Create Post")
        print("2. View All Posts")
        print("3. Search Posts by Username")
        print("4. Logout")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            create_post(username)
        
        elif choice == "2":
            view_posts()
        
        elif choice == "3":
            search_posts()
        
        elif choice == "4":
            print("Logging out...")
            break
        
        else:
            print("Invalid choice!")


def main():
    while True:
        print("\n==== PostBoard ====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            register()
        
        elif choice == "2":
            user = login()
            if user:
                user_menu(user)
        
        elif choice == "3":
            print("Exiting PostBoard...")
            break
        
        else:
            print("Invalid choice!")
main()
