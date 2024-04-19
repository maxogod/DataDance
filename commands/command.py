
class Command:

    args: list[str] = []

    def __str__(self):
        return f"{self.__class__.__name__} {self.args}"

    def execute(self):
        raise NotImplementedError

    pass
