# coding: utf-8

"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python or TypeScript SDK.  To install the official [Python SDK](https://pypi.org/project/humanloop/), run the following command:  ```bash pip install humanloop ```  To install the official [TypeScript SDK](https://www.npmjs.com/package/humanloop), run the following command:  ```bash npm i humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://docs.humanloop.com/).

    The version of the OpenAPI document: 4.0.1
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict


class EvaluationResultResponse(BaseModel):
    id: str = Field(alias='id')

    evaluator_id: str = Field(alias='evaluator_id')

    log_id: str = Field(alias='log_id')

    updated_at: datetime = Field(alias='updated_at')

    evaluation_id: typing.Optional[str] = Field(None, alias='evaluation_id')

    value: typing.Optional[typing.Union[bool, typing.Union[int, float]]] = Field(None, alias='value')

    error: typing.Optional[str] = Field(None, alias='error')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
