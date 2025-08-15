#!/usr/bin/env python3
# QuickNotes – Minimal Command-Line Note Taking App

import os

NOTES_FILE = "quicknotes.txt"

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]

def save_notes(notes):
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        for note in notes:
            f.write(note + "\n")

def add_note():
    note = input("Enter your note: ").strip()
    if note:
        notes = load_notes()
        notes.append(note)
        save_notes(notes)
        print("Note added successfully!")
    else:
        print("Empty note discarded.")

def view_notes():
    notes = load_notes()
    if not notes:
        print("No notes found.")
        return
    print("\nYour Notes:")
    for idx, note in enumerate(notes, 1):
        print(f"{idx}. {note}")

def delete_note():
    notes = load_notes()
    if not notes:
        print("No notes to delete.")
        return
    view_notes()
    try:
        choice = int(input("Enter note number to delete: "))
        if 1 <= choice <= len(notes):
            removed = notes.pop(choice - 1)
            save_notes(notes)
            print(f"Deleted: {removed}")
        else:
            print("Invalid note number.")
    except ValueError:
        print("Please enter a valid number.")

def search_notes():
    keyword = input("Enter keyword to search: ").strip().lower()
    if not keyword:
        print("Empty keyword.")
        return
    notes = load_notes()
    matches = [note for note in notes if keyword in note.lower()]
    if matches:
        print("\nSearch Results:")
        for idx, note in enumerate(matches, 1):
            print(f"{idx}. {note}")
    else:
        print("No matching notes found.")

def menu():
    while True:
        print("\n=== QuickNotes Menu ===")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Search Notes")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            search_notes()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()
