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
from pydantic import BaseModel, Field, RootModel


class BaseMetricResponse(BaseModel):
    # A description of what the metric measures.
    description: str = Field(alias='description')

    # ID of the metric. Starts with 'metric_'.
    id: str = Field(alias='id')

    # The name of the metric.
    name: str = Field(alias='name')

    # Python code used to calculate a metric value on each logged datapoint.
    code: str = Field(alias='code')

    # Whether the metric is a global default metric. Metrics with this flag enabled cannot be deleted or modified.
    default: bool = Field(alias='default')

    # If enabled, the metric is calculated for every logged datapoint.
    active: bool = Field(alias='active')

    created_at: datetime = Field(alias='created_at')

    updated_at: datetime = Field(alias='updated_at')
    class Config:
        arbitrary_types_allowed = True
