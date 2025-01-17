from sqlalchemy.orm import Mapped


class NameMixin:
    name: Mapped[str]
