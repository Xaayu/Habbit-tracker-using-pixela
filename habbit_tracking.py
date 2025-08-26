import requests
from datetime import datetime
import webbrowser

# ----------------- CONFIG -----------------
API = "https://pixe.la/v1/users"
TOKEN = "sgwieofndbsleixbndocb"   # keep secret in real projects
USERNAME = "xaayu"
GRAPH_ID = "graph1"

HEADERS = {"X-USER-TOKEN": TOKEN}
PIXEL_ENDPOINT = f"{API}/{USERNAME}/graphs/{GRAPH_ID}"

# ----------------- FUNCTIONS -----------------
def add_pixel():
    hours = input("How many hours did you code today? ")
    pixel_data = {
        "date": datetime.now().strftime("%Y%m%d"),
        "quantity": hours,
    }
    response = requests.post(PIXEL_ENDPOINT, json=pixel_data, headers=HEADERS)
    print("✅ Add Pixel Response:", response.text)


def update_pixel():
    hours = input("Enter new hours to update: ")
    today = datetime.now().strftime("%Y%m%d")
    pixel_update_endpoint = f"{PIXEL_ENDPOINT}/{today}"
    response = requests.put(pixel_update_endpoint, json={"quantity": hours}, headers=HEADERS)
    print("🔄 Update Pixel Response:", response.text)


def delete_pixel():
    today = datetime.now().strftime("%Y%m%d")
    pixel_delete_endpoint = f"{PIXEL_ENDPOINT}/{today}"
    response = requests.delete(pixel_delete_endpoint, headers=HEADERS)
    print("🗑️ Delete Pixel Response:", response.text)


def view_graph():
    graph_url = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}.html"
    print("🌐 Opening graph in browser:", graph_url)
    webbrowser.open(graph_url)

# ----------------- MENU -----------------
def menu():
    while True:
        print("\n--- PIXELA CODING TRACKER ---")
        print("1. Add today's pixel")
        print("2. Update today's pixel")
        print("3. Delete today's pixel")
        print("4. View coding graph")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_pixel()
        elif choice == "2":
            update_pixel()
        elif choice == "3":
            delete_pixel()
        elif choice == "4":
            view_graph()
        elif choice == "5":
            print("👋 Exiting Pixela Tracker. Keep coding!")
            break
        else:
            print("❌ Invalid choice, try again.")

# ----------------- RUN -----------------
if __name__ == "__main__":
    menu()