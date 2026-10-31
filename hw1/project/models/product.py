class Product:
    def __init__(
        self,
        name: str,
        category: str,
        price: int | float,
    ) -> None:
        self.name: str = name
        self.category: str = category
        self.price: int | float = price
        self.sale: int | float = 0

    def edit_category(self, new_category: str) -> None:
        self.category = new_category

    def edit_price(self, new_price: int | float) -> None:
        self.price = new_price

    def set_sale(self, sale: int | float) -> None:
        self.sale = sale

    def cancel_sale(self) -> None:
        self.sale = 0

    def get_price(self) -> int | float:
        return self.price * (100 - self.sale) / 100

    def __repr__(self) -> str:
        return (
            f'Product(name={self.name!r}, category={self.category!r}, '
            f'price={self.price}, sale={self.sale})'
        )
