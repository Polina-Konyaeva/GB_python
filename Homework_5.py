class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):

    def draw(self):
        print(f'Отрисовка осуществляется {self.title}')

class Pencil(Stationery):

    def draw(self):
        print(f'Отрисовка осуществляется {self.title}')

class Handle(Stationery):

    def draw(self):
        print(f'Отрисовка осуществляется {self.title}')

pen_s = Pen('ручкой')
pen_s.draw()

pencil_s = Pencil('карандашем')
pencil_s.draw()

handle_s = Handle('маркером')
handle_s.draw()
