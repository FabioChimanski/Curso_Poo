def main_menu():
    tasks = []
    
    while True:
        print("\n--- TODO MANAGER ---")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Delete Tasks")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            # Sua lógica para adicionar aqui
            task = input('Inform your task: ')
            tasks.append(task)
            print('Task added sucessfully!')

            with open("tasks.txt", "a") as arquivo:
                arquivo.write(task + "\n")
            
        elif choice == '2':
            # Sua lógica para listar aqui
            print('List tasks')
            print('------------------')
            
            with open("task.txt, r") as arquivo:
                conteudo = arquivo.read()
                print(conteudo)


        elif choice == '3':
            #DELETAR
            if not tasks:
                print("No tasks so far")

            task_del = input("Please specify the task you wish to delete: ")

            if task_del in tasks:
                tasks.remove(task_del)
                print(f"The task {task_del} was successfully removed!")
            else:
                print(f'Task {task_del} not exist!')


        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option!")
            
        

if __name__ == "__main__":
    main_menu()