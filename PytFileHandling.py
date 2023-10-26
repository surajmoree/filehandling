import os
import json

def create_folder(directory):                             #diretory passing just a variable
    if not os.path.exists(directory):
        os.makedirs(directory)

def create_subfolder(parent_directory, subfolder_name):
    subfolder_path = os.path.join(parent_directory, subfolder_name)
    create_folder(subfolder_path)
    return subfolder_path

def create_student_data(data_path, student_data):         # data_path is passs for store data in subfolder path which we declear in main()
    with open(data_path, 'a') as file:
        file.write(json.dumps(student_data) + '\n')   #The dump function in Python is mainly used when we want
                                                      #to store and transfer objects (Python objects) into a file in the form of JSON
    print("Data created successfully!")

def read_all_student_data(data_path):                    
    if  os.path.exists(data_path):
        with open(data_path, 'r') as file:
            student_data_list = file.read().strip().split('\n')
            print("Student Data:")                               # idx is use for getting index of element
            for idx, student_data in enumerate(student_data_list, start=1):  # enumerate is use iterate through a sequence and keep track of the index of each element
                print(f"{idx}. {json.loads(student_data)}")    # json.loads is use to parse a valid JSON string and convert it into a Python Dictionary
    else:
        print("Data file not found. Create data first.")

def update_student_data_by_id(data_path, student_id, new_data):
    if os.path.exists(data_path):
        with open(data_path, 'r') as file:
            student_data_list = file.read().strip().split('\n')
       
        if 1 <= student_id <= len(student_data_list):  
            student_data_list[student_id - 1] = json.dumps(new_data)
           
            with open(data_path, 'w') as file:
                file.write('\n'.join(student_data_list))
           
            print(f"Data with ID {student_id} updated successfully!")
        else:
            print("Invalid student ID.")
    else:
        print("Data file not found. Create data first.")

def delete_student_data_by_id(data_path, student_id):
    if os.path.exists(data_path):
        with open(data_path, 'r') as file:
            student_data_list = file.read().strip().split('\n')
       
        if 1 <= student_id <= len(student_data_list):
            deleted_data = student_data_list.pop(student_id - 1)
           
            with open(data_path, 'w') as file:
                file.write('\n'.join(student_data_list))
           
            print(f"Data with ID {student_id} deleted successfully: {json.loads(deleted_data)}")
        else:
            print("Invalid student ID.")
    else:
        print("Data file not found. Nothing to delete.")

def main():
    create_folder_flag = input("Do you want to create a folder? (yes/no): ").lower()   #lower() convert any string to lower case
    if create_folder_flag == 'yes':
        parent_folder = input("Enter the name of the parent folder: ")
        create_folder(parent_folder)
       
        subfolder_name = input("Enter the name of the subfolder: ")
        subfolder_path = create_subfolder(parent_folder, subfolder_name)
       
        data_path = os.path.join(subfolder_path, "student_data.json")
       
        while True:
            print("\nOptions:")
            print("1. Create Student Data")
            print("2. Read All Student Data")
            print("3. Update Student Data by ID")
            print("4. Delete Student Data by ID")
            print("5. Exit")
           
            choice = input("Select an option: ")
           
            if choice == "1":
                student_data = {
                    "name": input("Enter student's name: "),
                    "city": input("Enter student's city: "),
                    "grade": input("Enter student's grade: "),
                    "percentage": input("Enter student's percentage: "),
                    "result": input("Enter student's result: ")
                }
                create_student_data(data_path, student_data)
            elif choice == "2":
                read_all_student_data(data_path)
            elif choice == "3":
                student_id = int(input("Enter the ID of the student to update: "))
                new_data = {
                    "name": input("Enter new name: "),
                    "city": input("Enter new city: "),
                    "grade": input("Enter new grade: "),
                    "percentage": input("Enter new percentage: "),
                    "result": input("Enter new result: ")
                }
                update_student_data_by_id(data_path, student_id, new_data)
            elif choice == "4":
                student_id = int(input("Enter the ID of the student to delete: "))
                delete_student_data_by_id(data_path, student_id)
            elif choice == "5":
                print("Exiting program.")
                break
            else:
                print("Invalid option. Please try again.")
    else:
        print("No folder created. Exiting program.")
       
           
     
   
         
         
         
   

if __name__ == "__main__":
    main()
