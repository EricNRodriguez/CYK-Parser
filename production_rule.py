class ProductionRule():
    def __init__(self, head, *body):
        self._head = head
        self._bodys = [b for b in body]

    def get_variable(self):
        return self._head

    def get_bodys(self):
        return self._bodys

    def add_bodys(self, *body):
        self._bodys = [*self._bodys, *body]

