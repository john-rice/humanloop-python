# coding: utf-8

"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python or TypeScript SDK.  To install the official [Python SDK](https://pypi.org/project/humanloop/), run the following command:  ```bash pip install humanloop ```  To install the official [TypeScript SDK](https://www.npmjs.com/package/humanloop), run the following command:  ```bash npm i humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://docs.humanloop.com/).

    The version of the OpenAPI document: 4.0.1
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from humanloop import schemas  # noqa: F401


class FeedbackSelectAggregate(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "total",
            "values",
            "feedback_type",
        }
        
        class properties:
        
            @staticmethod
            def feedback_type() -> typing.Type['FeedbackTypeModel']:
                return FeedbackTypeModel
        
            @staticmethod
            def values() -> typing.Type['FeedbackSelectAggregateValues']:
                return FeedbackSelectAggregateValues
            total = schemas.IntSchema
            __annotations__ = {
                "feedback_type": feedback_type,
                "values": values,
                "total": total,
            }
    
    total: MetaOapg.properties.total
    values: 'FeedbackSelectAggregateValues'
    feedback_type: 'FeedbackTypeModel'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["feedback_type"]) -> 'FeedbackTypeModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["values"]) -> 'FeedbackSelectAggregateValues': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["feedback_type", "values", "total", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["feedback_type"]) -> 'FeedbackTypeModel': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["values"]) -> 'FeedbackSelectAggregateValues': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["feedback_type", "values", "total", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        total: typing.Union[MetaOapg.properties.total, decimal.Decimal, int, ],
        values: 'FeedbackSelectAggregateValues',
        feedback_type: 'FeedbackTypeModel',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FeedbackSelectAggregate':
        return super().__new__(
            cls,
            *args,
            total=total,
            values=values,
            feedback_type=feedback_type,
            _configuration=_configuration,
            **kwargs,
        )

from humanloop.model.feedback_select_aggregate_values import FeedbackSelectAggregateValues
from humanloop.model.feedback_type_model import FeedbackTypeModel
