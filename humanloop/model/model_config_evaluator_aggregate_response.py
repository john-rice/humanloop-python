# coding: utf-8

"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python or TypeScript SDK.  To install the official [Python SDK](https://pypi.org/project/humanloop/), run the following command:  ```bash pip install humanloop ```  To install the official [TypeScript SDK](https://www.npmjs.com/package/humanloop), run the following command:  ```bash npm i humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://docs.humanloop.com/).

    The version of the OpenAPI document: 4.0.0
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


class ModelConfigEvaluatorAggregateResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "model_config_id",
            "evaluator_id",
        }
        
        class properties:
            model_config_id = schemas.StrSchema
            evaluator_id = schemas.StrSchema
            aggregate_value = schemas.AnyTypeSchema
            __annotations__ = {
                "model_config_id": model_config_id,
                "evaluator_id": evaluator_id,
                "aggregate_value": aggregate_value,
            }
    
    model_config_id: MetaOapg.properties.model_config_id
    evaluator_id: MetaOapg.properties.evaluator_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["model_config_id"]) -> MetaOapg.properties.model_config_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["evaluator_id"]) -> MetaOapg.properties.evaluator_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["aggregate_value"]) -> MetaOapg.properties.aggregate_value: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["model_config_id", "evaluator_id", "aggregate_value", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["model_config_id"]) -> MetaOapg.properties.model_config_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["evaluator_id"]) -> MetaOapg.properties.evaluator_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["aggregate_value"]) -> typing.Union[MetaOapg.properties.aggregate_value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["model_config_id", "evaluator_id", "aggregate_value", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        model_config_id: typing.Union[MetaOapg.properties.model_config_id, str, ],
        evaluator_id: typing.Union[MetaOapg.properties.evaluator_id, str, ],
        aggregate_value: typing.Union[MetaOapg.properties.aggregate_value, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ModelConfigEvaluatorAggregateResponse':
        return super().__new__(
            cls,
            *args,
            model_config_id=model_config_id,
            evaluator_id=evaluator_id,
            aggregate_value=aggregate_value,
            _configuration=_configuration,
            **kwargs,
        )
