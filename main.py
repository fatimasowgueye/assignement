#Fatimata SOW option Data Science
# main.py

import os

def create_directory_structure():
    try:
        os.mkdir("data")
        os.mkdir("data/cleaned")
        os.mkdir("data/raw")
        os.mkdir("docs")
        os.mkdir("models")
        os.mkdir("notebooks")
        os.mkdir("reports")
        os.mkdir("src")
    except FileExistsError:
        print("Les dossiers existent déjà.")

def commit_changes(message):
    os.system(f'git add . && git commit -m "{message}"')

def main():
    # Créer l'arborescence de dossiers
    create_directory_structure()
    commit_changes("Créer l'arborescence de dossiers")

if __name__ == "__main__":
    main()
