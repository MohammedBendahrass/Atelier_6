from collections import deque


def genarate_Binaire_Nombre(n):
    result = []
    queue = deque(["1"])

    for i in range(n):
        binaire_nombre = queue.popleft()
        result.append(binaire_nombre)

        queue.append(binaire_nombre + "0")
        queue.append(binaire_nombre + "1")

    return result


n = int(input("Entrez la valeur de n : "))
binaire_nombre = genarate_Binaire_Nombre(n)
print(binaire_nombre)
