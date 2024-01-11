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

from humanloop.type.log_request import LogRequest

class RequiredCreateEvaluationLogRequest(TypedDict):
    # The datapoint for which a log was generated. Must be one of the datapoints in the dataset being evaluated.
    datapoint_id: str

    # The log generated for the datapoint.
    log: LogRequest

class OptionalCreateEvaluationLogRequest(TypedDict, total=False):
    pass

class CreateEvaluationLogRequest(RequiredCreateEvaluationLogRequest, OptionalCreateEvaluationLogRequest):
    pass
