import requests

BASE_URL = 'http://localhost:8080'

def get_request():
    response = requests.get(BASE_URL)
    print(f"GET Response: {response.text}")

def post_request(data):
    response = requests.post(BASE_URL, data=data)
    print(f"POST Response: {response.text}")

def put_request(data):
    response = requests.put(BASE_URL, data=data)
    print(f"PUT Response: {response.text}")

def delete_request():
    response = requests.delete(BASE_URL)
    print(f"DELETE Response: {response.text}")

def main():
    while True:
        print("\nChoose an HTTP operation:")
        print("1: GET")
        print("2: POST")
        print("3: PUT")
        print("4: DELETE")
        print("q: Quit")

        choice = input("Enter your choice: ").strip().lower()

        if choice == '1':
            get_request()
        elif choice == '2':
            data = input("Enter data to POST: ")
            post_request(data)
        elif choice == '3':
            data = input("Enter data to PUT: ")
            put_request(data)
        elif choice == '4':
            delete_request()
        elif choice == 'q':
            print("Exiting client.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
