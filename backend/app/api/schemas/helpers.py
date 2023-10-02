from pydantic import BaseModel, ConfigDict


def lower_camel(string: str) -> str:
    camel = "".join(word.capitalize() for word in string.split("_"))
    low_camel = camel[0].lower() + camel[1:]
    return low_camel


class BaseConfig(BaseModel):
    model_config = ConfigDict(
        from_attributes=True, alias_generator=lower_camel, populate_by_name=True
    )


class CustomPagination(BaseConfig):
    page_number: int = None
    page_size: int = None
    total_record_count: int = None
    pagination: dict = {}

    def __init__(
        self, instances, prefix, first, last, page, page_size, *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.page_number = page
        self.page_size = page_size
        self.total_record_count = len(instances)
        self.records = instances[first:last]

        if last >= len(instances):
            self.pagination["next"] = None
        else:
            self.pagination["next"] = f"{prefix}?page={page + 1}&pageSize={page_size}"
        if page > 1:
            self.pagination[
                "previous"
            ] = f"{prefix}?page={page - 1}&pageSize={page_size}"
        else:
            self.pagination["previous"] = None

# from typing import Any, Optional

# from sqlalchemy import func
# from sqlalchemy.engine import Connection
# from sqlalchemy.sql import Select

# from fastapi_pagination.api import apply_items_transformer, create_page
# from fastapi_pagination.bases import AbstractParams
# from fastapi_pagination.types import AdditionalData, ItemsTransformer
# from fastapi_pagination.utils import verify_params


# def paginate(
#     conn: Connection,
#     stmt: Select,
#     params: Optional[AbstractParams] = None,
#     *,
#     transformer: Optional[ItemsTransformer] = None,
#     additional_data: Optional[AdditionalData] = None,
# ) -> Any:
#     params, raw_params = verify_params(params, "limit-offset")

#     total = conn.scalar(stmt.with_only_columns(func.count()))
#     q = stmt.offset(raw_params.offset).limit(raw_params.limit)
#     items = conn.execute(q).all()

#     t_items = apply_items_transformer(items, transformer)

#     return create_page(
#         t_items,
#         total,
#         params,
#         **(additional_data or {}),
#     )