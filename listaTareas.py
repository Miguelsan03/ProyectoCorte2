class Itarea:
    def __init__(self,description, vencimiento=None):
        self.description = description
        self.vencimiento = vencimiento
        self.completed = False

    def completado(self):
        self.completed= True

class ListaTareas:
    def __init__(self) -> None:
        self._tasks = []
        self._observers = []
    
    def addTask(self, task):
        self._tasks.append(task)
        self.notify_observers()

    def done(self, task):
        Itarea.completado()
        self.notify_observers()

    def verTareas(self, task):
        print(self._tasks)

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

class Observer(Itarea):
    def __init__(self, name) -> None:
        self._name = name
        super().__init__()

    def update(self, message):
        for task in ListaTareas._tasks():
            if not task.completado and Itarea.vencimiento < 1:
                print(f"{self._task} se vence en poco tiempo ")
