def bubble_sort(list_to_sort):
	# Repetimos la iteración de la lista por todos los elementos para moverlos al final
  for outer_index in range(0, len(list_to_sort) - 1):
    # Usamos esta variable para revisar si hemos movido elementos
    has_made_changes = False
		# Le restamos uno al length para parar en el penultimo elemento
    # Usamos el indice exterior para restar las ejecuciones de
    # los elementos que ya estan ordenados al final
    for index in range(0, len(list_to_sort) - 1 - outer_index):
      # Guardamos los valores del elemento actual y el siguiente
      current_element = list_to_sort[index]
      next_element = list_to_sort[index + 1]

      print(f'-- Iteracion {outer_index}, {index}. Elemento actual: {current_element}, Siguiente elemento: {next_element}')

      # Si el actual es mayor al siguiente, intercambiamos sus posiciones
      if current_element > next_element:
        print('El elemento actual es mayor al siguiente. Intercambiandolos...')
        list_to_sort[index] = next_element
        list_to_sort[index + 1] = current_element
        has_made_changes = True

    # Si no hemos movido elementos, la lista ya esta ordenada
    if not has_made_changes:
      return


my_test_list = [1, 2, 3, 10, 4, 5, 6, 7, 8]
bubble_sort(my_test_list)

print(my_test_list)


"""
=======================================================================
EJERCICIO GUÍA - SEMANA 15: BUBBLE SORT CON MÉTRICAS
=======================================================================
OBJETIVO: Implementar el algoritmo Bubble Sort OPTIMIZADO y calcular su eficiencia.

REQUERIMIENTOS:
1. La función debe utilizar la optimización de RANGO (evitar revisar elementos ordenados al final).
2. La función debe utilizar la optimización de SALIDA TEMPRANA (detenerse si no hay 'swaps').
3. La función debe inicializar y mantener el conteo de dos métricas:
   - 'comparisons' (Comparaciones): Cuenta cada vez que se revisa un par de elementos.
   - 'swaps' (Intercambios): Cuenta cada vez que dos elementos son movidos.
4. La función debe devolver (return) las métricas 'swaps' y 'comparisons' al finalizar.
======================================================================="""

def bubble_sort_metrics(list_to_sort):
  comparisions=0
  swaps=0
  for outer_index in range(0, len(list_to_sort) -1):
    has_made_change=False
    for index in range(0, len(list_to_sort) -1 - outer_index):
      comparisions+=1
      current_element=list_to_sort[index]
      next_element=list_to_sort[index+1]
      print(f"irteracion: {outer_index}, {index} elemento actual: {current_element}, siguiente elemento: {next_element}")
      if current_element > next_element:
        swaps+=1
        print("elemento actual es mayor al siguiene, intercambiandolos...")
        list_to_sort[index]=next_element
        list_to_sort[index+1]=current_element
        has_made_change=True

    if not has_made_change:
      return swaps, comparisions


# Ejemplo de uso:
# test_list = [18, -11, 68, 6, 32]
test_list=[1, 2, 3, 4, 5, 6, 7, 8]
swaps_final, comparisons_final = bubble_sort_metrics(test_list.copy())
print(f"\nLista ordenada: {test_list}")
print(f"--- RESULTADOS FINALES ---")
print(f"Total de Intercambios (Swaps): {swaps_final}")
print(f"Total de Comparaciones: {comparisons_final}")