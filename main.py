from solve_tsp import *
from path_visualize import grafica
import csv

#item_count = int(input())
# for i in range(1, item_count+1):
#     parts = input().split() # CSV
#     points.append(Point(float(parts[0]), float(parts[1])))

def main():
    name = input("Nombre del archivo: ")
    points = []
    with open('../'+name, 'r') as file:
        coordenadas = csv.reader(file, delimiter=' ')
        for coordenada in coordenadas:
            cor = coordenada#[-2:]
            points.append(Point(float(cor[0]), float(cor[1])))
    solution = solve_Christofides(points)
    print(solution)
    print(calcular_costo(solution, points))
    grafica(points, solution)

def calcular_costo(ruta, puntos):
    total_cost = 0
    for i in range(len(ruta) - 1):
        punto1 = puntos[ruta[i]]
        punto2 = puntos[ruta[i + 1]]
        total_cost += length(punto1, punto2)
    # Para cerrar el ciclo, sumar la distancia entre el último y el primero
    total_cost += length(puntos[ruta[-1]], puntos[ruta[0]])
    return total_cost

if __name__ == '__main__':
    main()

