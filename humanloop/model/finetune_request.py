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


class FinetuneRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "dataset_id",
            "name",
            "config",
        }
        
        class properties:
            name = schemas.StrSchema
            dataset_id = schemas.StrSchema
        
            @staticmethod
            def config() -> typing.Type['FinetuneConfig']:
                return FinetuneConfig
            metadata = schemas.DictSchema
        
            @staticmethod
            def provider_api_keys() -> typing.Type['ProviderApiKeys']:
                return ProviderApiKeys
            __annotations__ = {
                "name": name,
                "dataset_id": dataset_id,
                "config": config,
                "metadata": metadata,
                "provider_api_keys": provider_api_keys,
            }
    
    dataset_id: MetaOapg.properties.dataset_id
    name: MetaOapg.properties.name
    config: 'FinetuneConfig'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataset_id"]) -> MetaOapg.properties.dataset_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["config"]) -> 'FinetuneConfig': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> MetaOapg.properties.metadata: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provider_api_keys"]) -> 'ProviderApiKeys': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "dataset_id", "config", "metadata", "provider_api_keys", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataset_id"]) -> MetaOapg.properties.dataset_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["config"]) -> 'FinetuneConfig': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union[MetaOapg.properties.metadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provider_api_keys"]) -> typing.Union['ProviderApiKeys', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "dataset_id", "config", "metadata", "provider_api_keys", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        dataset_id: typing.Union[MetaOapg.properties.dataset_id, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        config: 'FinetuneConfig',
        metadata: typing.Union[MetaOapg.properties.metadata, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        provider_api_keys: typing.Union['ProviderApiKeys', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FinetuneRequest':
        return super().__new__(
            cls,
            *args,
            dataset_id=dataset_id,
            name=name,
            config=config,
            metadata=metadata,
            provider_api_keys=provider_api_keys,
            _configuration=_configuration,
            **kwargs,
        )

from humanloop.model.finetune_config import FinetuneConfig
from humanloop.model.provider_api_keys import ProviderApiKeys
