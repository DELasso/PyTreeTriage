class Node:
    def __init__(self, paciente):
        self.paciente = paciente
        self.left = None
        self.right = None


class Paciente:
    def __init__(self, id, genero, nombre, edad, triaje):
        self.id = id
        self.genero = genero
        self.nombre = nombre
        self.edad = edad
        self.triaje = triaje

    def __lt__(self, object):
        # Comparar primero por triaje, si son iguales, comparar por el número de paciente (orden de llegada)
        return (self.triaje, self.id) < (object.triaje, object.id)

    def __str__(self):
        return f"Paciente(ID: {self.id}, Nombre: {self.nombre}, Edad: {self.edad}, Triaje: {self.triaje})"


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, paciente):
        node = Node(paciente)
        self.heap.append(node)
        self.ordenar_hacia_arriba(len(self.heap) - 1)

    def obtener_maxima_urgencia(self):
        if self.heap:
            return self.heap[0].paciente
        return None

    def atender_maxima_urgencia(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop().paciente

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return root.paciente

    def remove(self, paciente):
        for i in range(len(self.heap)):
            if self.heap[i].paciente == paciente:
                if i == len(self.heap) - 1:
                    return self.heap.pop().paciente
                nodo_a_eliminar = self.heap[i]
                self.heap[i] = self.heap.pop()
                self._bubble_down(i)
                self.ordenar_hacia_arriba(i)
                return nodo_a_eliminar.paciente
        return None

    def ordenar_hacia_arriba(self, index):
        parent_index = (index - 1) // 2
        if parent_index >= 0 and self.heap[index].paciente < self.heap[parent_index].paciente:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.ordenar_hacia_arriba(parent_index)

    def _bubble_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        priority = index

        if left_child_index < len(self.heap) and self.heap[left_child_index].paciente < self.heap[priority].paciente:
            priority = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index].paciente < self.heap[priority].paciente:
            priority = right_child_index

        if priority != index:
            self.heap[index], self.heap[priority] = self.heap[priority], self.heap[index]
            self._bubble_down(priority)

    def print_tree(self, index=0, prefix="", is_left=True):
        if index >= len(self.heap) or self.heap[index] is None:
            return

        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        if left_child_index < len(self.heap):
            self.print_tree(left_child_index, prefix + ("│   " if is_left else "    "), False)

        print(prefix + ("└── " if is_left else "┌── ") + str(self.heap[index].paciente))

        if right_child_index < len(self.heap):
            self.print_tree(right_child_index, prefix + ("    " if is_left else "│   "), True)

    def __str__(self):
        return str([str(node.paciente) for node in self.heap])


class GestionUrgencias:
    def __init__(self):
        self.heap = MinHeap()
        self.id = 0

    def registrar_paciente(self, genero, nombre, edad, triaje):
        paciente = Paciente(self.id, genero, nombre, edad, triaje)
        self.heap.insert(paciente)
        self.id += 1
        print(f"Paciente registrado: {paciente}")

    def consultar_proximo(self):
        return self.heap.obtener_maxima_urgencia()

    def atender_siguiente(self):
        paciente = self.heap.atender_maxima_urgencia()
        if paciente:
            print(f"Paciente atendido: {paciente}")
        return paciente

    def consultar_espera(self):
        return [node.paciente for node in self.heap.heap]

    def consultar_espera_por_triaje(self, triaje):
        return [node.paciente for node in self.heap.heap if node.paciente.triaje == triaje]

    def eliminar_paciente(self, id=None, nombre=None):
        for node in self.heap.heap:
            if (id is not None and node.paciente.id == id) or (nombre is not None and node.paciente.nombre == nombre):
                paciente_a_borrar = self.heap.remove(node.paciente)
                if paciente_a_borrar:
                    print(f"Paciente eliminado: {paciente_a_borrar}")
                    return paciente_a_borrar
                self.heap._bubble_down(0)
        return None

    def imprimir_arbol(self):
        self.heap.print_tree()

"""
gestion = GestionUrgencias()
gestion.registrar_paciente("M", "Lasso", 19, 4)
gestion.registrar_paciente("F", "Adely", 22, 2)
gestion.registrar_paciente("M", "Lopez", 19, 1)
gestion.registrar_paciente("F", "Doanza", 44, 4)



print("\nProximo paciente a atender:")
print(gestion.consultar_proximo())

print("\nAtendiendo al siguiente paciente:")
gestion.atender_siguiente()


print("\nProximo paciente a atender:")
print(gestion.consultar_proximo())

print("\nPacientes en espera:")
for p in gestion.consultar_espera():
    print(p)

print("\nPacientes en espera con triaje 4:")
for p in gestion.consultar_espera_por_triaje(4):
    print(p)

print("\nEliminando paciente con nombre 'Adely':")
gestion.eliminar_paciente(nombre="Adely")

print("\nPacientes en espera:")
for p in gestion.consultar_espera():
    print(p)

print("\nÁrbol del heap:")
gestion.imprimir_arbol()
"""