import pydantic
import typing as t

str100 = t.Annotated[str, pydantic.StringConstraints(max_length=100)]
