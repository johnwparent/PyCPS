import sys


def print_getter_setter(name: str) -> None:
    setter = f"""
    @{name}.setter
    def {name}(self, val):
        self._{name} = val"""
    getter = f"""
    @property
    def {name}(self):
        return self._{name}"""
    print(setter)
    print(getter)
    print("\n\n")


if __name__ == "__main__":
    name = sys.argv[1]
    print_getter_setter(name)