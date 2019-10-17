class ProductionRule():
    def __init__(self, head, body):
        self._head = head
        self._body = body

    def get_variable(self):
        return self._head

    def get_body(self):
        return self._body

    def add_bodys(self, body):
        self._body = body