import os
import json
import csv

def load_json_from_folder():
    while True:
        try:
            folder_name = input("Please enter the folder name where the 'gtadikamalla_adoptions.json' file is located: ")

            if folder_name in '':
                raise FileNotFoundError(f"The folder name should not be empty. Please try again.")
            
            cwd=os.getcwd()
            current_folder=os.path.basename(cwd)

            if folder_name.lower().replace(' ','') in current_folder.lower().replace(' ',''):
                file_path = os.path.join(cwd, 'gtadikamalla_adoptions.json')

                    
                if not os.path.exists(file_path):
                    raise FileNotFoundError(f"The file 'gtadikamalla_adoptions.json' was not found in the folder '{folder_name}'. Please try again.")


                with open(file_path, 'r') as file:
                        data = json.load(file)
                        print("Successfully loaded the JSON data into a variable.")
                return data  
            else:
                raise FileNotFoundError(f"The file 'gtadikamalla_adoptions.json' was not found in the folder '{folder_name}'. Please try again.")

        except FileNotFoundError as fnf_error:
            print(f"Error: {fnf_error}")
        except json.JSONDecodeError as json_error:
            print(f"Error decoding JSON file: {json_error}. Please ensure the file contains valid JSON.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")


#Adoptions CSV
def export_adoptions_data(adoption_data):
    csv_path=os.getcwd()

    csv_file = os.path.join(csv_path, 'adoptions.csv')

    
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(['adoption_id', 'adoptions_id', 'date', 'quantity', 'book_id', 'isbn10', 'isbn13', 'title', 'category'])
        
        
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
    
    csv_file = os.path.join(csv_path, 'books.csv')

    
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(['book_id','isbn10', 'isbn13', 'title', 'category'])
        

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





#universities csv
def export_universities_data(adoption_data):
    
    csv_path=os.getcwd()


    csv_file = os.path.join(csv_path, 'universities.csv')

    
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(['university_id', 'name', 'address', 'city', 'state', 'website', 'zip', 'longitude', 'latitude','classification'])
        
        
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


#contacts csv
def export_contacts_data(adoption_data):
    csv_path=os.getcwd()
    
    
    csv_file = os.path.join(csv_path, 'contacts.csv')

    
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(['adoption_id', 'contact_order', 'gender', 'firstname', 'lastname'])
        
        
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



#messages csv
def export_messages_data(adoption_data):
    csv_path=os.getcwd()
    
    
    csv_file = os.path.join(csv_path, 'messages.csv')

    
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(['adoption_id', 'message_id', 'date', 'content', 'category'])
        
        
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

#List of universities using by state name
def list_universities_by_state(adoption_data):
    while True:
        state_name = input("Enter the name of the state (e.g. Illinois): ").replace(' ','')
        universities_in_state = []

        for adoption in adoption_data:
            university = adoption['university']
            

            if university.get('state', '').lower().replace(' ','') == state_name.lower():
                universities_in_state.append(university['name'])

        
        if universities_in_state:
            print(f"List of universities in {state_name}:")
            print('____________________________________')
            for university in universities_in_state:
                print(f"- {university}")
            break
        else:
            print(f"No universities found in {state_name}.")


#List of category of books
def list_books_by_category(adoption_data):
    while True:
        
        categories = set()

        
        for adoption in adoption_data:
            adoptions = adoption['adoptions']
            for record in adoptions:
                category = record['book']['category']
                categories.add(category)

        
        sorted_categories = sorted(categories)

        
        print("Available book categories:")
        print('--------------------------')
        for category in sorted_categories:
            print(f"- {category}")


        chosen_category = input("\nEnter a category from the list: ")

       
        book_titles = []

        
        for adoption in adoption_data:
            adoptions = adoption['adoptions']
            for record in adoptions:
                if record['book']['category'].lower().replace(' ','') == chosen_category.lower().replace(' ',''):
                    book_titles.append(record['book']['title'])


        if book_titles:
            
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
