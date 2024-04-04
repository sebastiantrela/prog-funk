global_variable = None

def func(local_variable):
    global global_variable
    global_variable = 5
    print(f"zmienna lokalna: {local_variable}")
    print(f"zmienna globalna przed zmianą: {global_variable}")

    global_variable = 15
    print(f"zmienna globalna po zmianie: {global_variable}")

func(50)