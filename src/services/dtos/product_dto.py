class ProductDTO():
    def __init__(self, name: str, description: str, price: float, id: int = 0) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.price = price