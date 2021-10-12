# 5.	Реализовать класс Stationery (канцелярская принадлежность):
# ●	определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# ●	создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# ●	в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# ●	создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def _draw(self):
        return f'Enter the drow'


class Pen(Stationery):
    def _draw(self):
        return f'Enter the drow {self.title}'


class Pencil(Stationery):
    def _draw(self):
        return f'Enter the drow {self.title}'


class Handle(Stationery):
    def _draw(self):
        return f'Enter the drow {self.title}'


pen = Pen('pen')
print(pen._draw())
pencil = Pencil('pencil')
print(pencil._draw())
handle = Handle('hadle')
print(handle._draw())
