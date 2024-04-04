def f1():
    print("to jest pierwsza funkcja")

def f2(func):
    print("to jest funkcja, która została wywołana w pierwszej funkcji")
    func()

f2(f1)