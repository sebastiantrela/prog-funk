def analyze_data(data):
    match data:
        case []:
            return "Pusta lista"
        case [_]:
            return "Lista z jednym elementem"
        case [_, _]:
            return "Lista z dwoma elementami"
        case list():
            return "Lista z wieloma elementami"
        case ():
            return "Pusta krotka"
        case (_,):
            return "Krotka z jednym elementem"
        case (_, _):
            return "Krotka z dwoma elementami"
        case tuple():
            return "Krotka z wieloma elementami"
        case _:
            return "Inny typ danych"

print(analyze_data([1, 2, 3]))
print(analyze_data(()))  
print(analyze_data((1,)))  
print(analyze_data("tekst"))  