"""Task manager with maps, sets and POO"""


class TaskManager:
    """Class Task manager. Base class"""
    def __init__(self):
        """Constructor"""
        self.tasks = {}

    def addTask(self, task, tags):
        """Add task method"""
        task = task.lower()
        if task in self.tasks:
            self.tasks[task] = self.tasks[task] | set(tags)
            # self.tasks[task].update(tags)
        else:
            # tags = set(tags)
           self.tasks[task] = set(tags)

    def printTasks(self):
        """Print task method"""
        return self.tasks


myTaskManager = TaskManager()
myTaskManager.addTask("Comprar leche", ["compras", "urgente"])
myTaskManager.addTask("Sacar al perro", ["mascotas"])
myTaskManager.addTask("Hacer ejercicio", ["salud"])
myTaskManager.addTask("Comprar leche", ["lacteos"])
print(myTaskManager.printTasks())

"""Output:
{
  "comprar leche": {"compras", "urgente", "lacteos"},
  'sacar al perro': {'mascotas'},
  'hacer ejercicio': {'salud'}
}
"""

"""
# # Input: 
# myTaskManager = TaskManager()
# myTaskManager.addTask("Comprar leche", ["compras", "urgente"])
# myTaskManager.addTask("Comprar leche", ["formula", "lacteos"])
# myTaskManager.addTask("Sacar al perro", ["mascotas"])
# myTaskManager.addTask("Sacar al perro", ["animales de carrera"])
# myTaskManager.addTask("Hacer ejercicio", ["salud"])
# myTaskManager.printTasks()
# 
# # Output:
# # {
# #   'comprar leche': {'compras', 'urgente'}, 
# #   'sacar al perro': {'mascotas'}, 
# #   'hacer ejercicio': {'salud'}
# # }
"""