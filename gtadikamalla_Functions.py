import os
import json
import csv

def load_json_from_folder():
    while True:
        try:
            # Prompt the user for the folder path
            folder_name = input("Please enter the folder path where the 'gtadikamalla_adoptions.json' file is located: ")

            if folder_name in '':
                raise FileNotFoundError(f"The folder path should not be empty. Please try again.")

            # Build the file path
            file_path = os.path.join(folder_name, 'gtadikamalla_adoptions.json')

            # Check if the file exists
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"The file 'gtadikamalla_adoptions.json' was not found in the folder '{folder_name}'. Please try again.")

            # If the file exists, attempt to load the JSON data
            with open(file_path, 'r') as file:
                data = json.load(file)
                print("Successfully loaded the JSON data into a variable.")
            return data  # Return the data once it's successfully loaded

        except FileNotFoundError as fnf_error:
            print(f"Error: {fnf_error}")
        except json.JSONDecodeError as json_error:
            print(f"Error decoding JSON file: {json_error}. Please ensure the file contains valid JSON.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")


#Adoptions CSV
def export_adoptions_data(adoption_data):
    csv_path=os.getcwd()
    # File path
    csv_file = os.path.join(csv_path, 'adoptions.csv')

    # Open the CSV file for writing
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(['adoption_id', 'adoptions_id', 'date', 'quantity', 'book_id', 'isbn10', 'isbn13', 'title', 'category'])
        
        # Iterate over the adoption data and write each row
        for adoption in adoption_data:
            adoptions = adoption['adoptions']
            for record in adoptions:
                writer.writerow([
                    adoption.get('id',''),              
                    record.get('id',''),                 
                    record.get('date',''),
                    record.get('quantity',''),           
                    record['book'].get('id',''),
                    record['book'].get('isbn10',''),
                    record['book'].get('isbn13',''),  
                    record['book'].get('title',''),   
                    record['book'].get('category','')    
                ])
    
    print(f"Adoptions data exported to {csv_file}")

#Books
def export_books_data(adoption_data):
    csv_path=os.getcwd()
    # File path
    csv_file = os.path.join(csv_path, 'books.csv')

    # Open the CSV file for writing
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(['book_id','isbn10', 'isbn13', 'title', 'category'])
        
        # Iterate over the adoption data and write each row
        for adoption in adoption_data:
            adoptions = adoption['adoptions']
            for record in adoptions:
                writer.writerow([          
                    record['book'].get('id',''),         
                    record['book'].get('isbn10',''),     
                    record['book'].get('isbn13',''),     
                    record['book'].get('title',''),   
                    record['book'].get('category','')
                ])
    
    print(f"Books data exported to {csv_file}")





#universities.csv
def export_universities_data(adoption_data):
    
    csv_path=os.getcwd()
    
    # File path
    csv_file = os.path.join(csv_path, 'universities.csv')

    # Open the CSV file for writing
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(['university_id', 'name', 'address', 'city', 'state', 'website', 'zip', 'longitude', 'latitude','classification'])
        
        # Iterate over the adoption data and write each row
        for adoption in adoption_data:
            university = adoption['university']
            writer.writerow([
                university.get('id',''),
                university.get('name',''),
                university.get('address',''),
                university.get('city',''),
                university.get('state',''),           
                university.get('website',''),
                university.get('zip',''),               
                university.get('longitude',''),         
                university.get('latitude',''),         
                university.get('classification','')
            ])
    
    print(f"University data exported to {csv_file}")


#contacts.csv
def export_contacts_data(adoption_data):
    csv_path=os.getcwd()
    
    # File path
    csv_file = os.path.join(csv_path, 'contacts.csv')

    # Open the CSV file for writing
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(['adoption_id', 'contact_order', 'gender', 'firstname', 'lastname'])
        
        # Iterate over the adoption data and write each row
        for adoption in adoption_data:
            contacts = adoption['contacts']
            for contact in contacts:
                writer.writerow([
                    adoption.get('id',''),             
                    contact.get('order',''),            
                    contact.get('gender',''),            
                    contact.get('firstname',''),         
                    contact.get('lastname','')        
                ])
    
    print(f"Contacts data exported to {csv_file}")



#messages.csv
def export_messages_data(adoption_data):
    csv_path=os.getcwd()
    
    # File path
    csv_file = os.path.join(csv_path, 'messages.csv')

    # Open the CSV file for writing
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(['adoption_id', 'message_id', 'date', 'content', 'category'])
        
        # Iterate over the adoption data and write each row
        for adoption in adoption_data:
            messages = adoption['messages']
            for message in messages:
                writer.writerow([
                    adoption.get('id',''),               
                    message.get('id',''),                
                    message.get('date',''),              
                    message.get('content',''),           
                    message.get('category','')          
                ])
    
    print(f"Messages data exported to {csv_file}")


def list_universities_by_state(adoption_data):
    while True:
        state_name = input("Enter the name of the state (e.g. Illinois): ").replace(' ','')
        universities_in_state = []

        for adoption in adoption_data:
            university = adoption['university']
            
            # Check if the university's state matches the input state name
            if university.get('state', '').lower().replace(' ','') == state_name.lower():
                universities_in_state.append(university['name'])

        # Check if any universities were found and display them
        if universities_in_state:
            print(f"List of universities in {state_name}:")
            print('____________________________________')
            for university in universities_in_state:
                print(f"- {university}")
            break
        else:
            print(f"No universities found in {state_name}.")



def list_books_by_category(adoption_data):
    while True:
        # Create a set to hold unique book categories
        categories = set()

        # Iterate over the adoption data to extract all unique book categories
        for adoption in adoption_data:
            adoptions = adoption['adoptions']
            for record in adoptions:
                category = record['book']['category']
                categories.add(category)

        # Convert the set to a sorted list for better display
        sorted_categories = sorted(categories)

        # Display all available categories
        print("Available book categories:")
        print('--------------------------')
        for category in sorted_categories:
            print(f"- {category}")

        # Prompt user to choose a category
        chosen_category = input("\nEnter a category from the list: ")

        # List to hold book titles from the chosen category
        book_titles = []

        # Iterate over the adoption data and filter books by the chosen category
        for adoption in adoption_data:
            adoptions = adoption['adoptions']
            for record in adoptions:
                if record['book']['category'].lower().replace(' ','') == chosen_category.lower().replace(' ',''):
                    book_titles.append(record['book']['title'])

        # Check if any books were found in the chosen category
        if book_titles:
            # Save the book titles to a text file
            with open(f'{chosen_category}_books.txt', 'w') as file:
                for title in book_titles:
                    file.write(title + '\n')
            
            print(f"\nBooks in the '{chosen_category}' category have been saved to '{chosen_category}_books.txt'.")
            break
        else:
            print(f"\nNo books found in the '{chosen_category}' category.")
            print('------------------------------------------------------')



adoption_data = load_json_from_folder()
if adoption_data:
    print(f"The data is : {adoption_data}")
print('___________________________________________________________')
export_adoptions_data(adoption_data)
print('___________________________________________________________')
export_books_data(adoption_data)
print('___________________________________________________________')
export_universities_data(adoption_data)
print('___________________________________________________________')
export_contacts_data(adoption_data)
print('___________________________________________________________')
export_messages_data(adoption_data)
print('___________________________________________________________')
list_universities_by_state(adoption_data)
print('___________________________________________________________')
list_books_by_category(adoption_data)
print('___________________________________________________________')
