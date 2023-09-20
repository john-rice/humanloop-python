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


class ModelProviders(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Supported model providers.
    """


    class MetaOapg:
        enum_value_to_name = {
            "openai": "OPENAI",
            "openai_azure": "OPENAI_AZURE",
            "ai21": "AI21",
            "mock": "MOCK",
            "anthropic": "ANTHROPIC",
            "langchain": "LANGCHAIN",
            "cohere": "COHERE",
            "replicate": "REPLICATE",
        }
    
    @schemas.classproperty
    def OPENAI(cls):
        return cls("openai")
    
    @schemas.classproperty
    def OPENAI_AZURE(cls):
        return cls("openai_azure")
    
    @schemas.classproperty
    def AI21(cls):
        return cls("ai21")
    
    @schemas.classproperty
    def MOCK(cls):
        return cls("mock")
    
    @schemas.classproperty
    def ANTHROPIC(cls):
        return cls("anthropic")
    
    @schemas.classproperty
    def LANGCHAIN(cls):
        return cls("langchain")
    
    @schemas.classproperty
    def COHERE(cls):
        return cls("cohere")
    
    @schemas.classproperty
    def REPLICATE(cls):
        return cls("replicate")
