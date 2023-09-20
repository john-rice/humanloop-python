# coding: utf-8

"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python or TypeScript SDK.  To install the official [Python SDK](https://pypi.org/project/humanloop/), run the following command:  ```bash pip install humanloop ```  To install the official [TypeScript SDK](https://www.npmjs.com/package/humanloop), run the following command:  ```bash npm i humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://docs.humanloop.com/).

    The version of the OpenAPI document: 4.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal


class RequiredCreateLogResponse(TypedDict):
    # String ID of logged datapoint. Starts with `data_`.
    id: str

    # String ID of project the datapoint belongs to. Starts with `pr_`.
    project_id: str

class OptionalCreateLogResponse(TypedDict, total=False):
    # String ID of session the datapoint belongs to. Populated only if the datapoint was logged with `session_id` or `session_reference_id`, and is `None` otherwise. Starts with `sesh_`.
    session_id: str

class CreateLogResponse(RequiredCreateLogResponse, OptionalCreateLogResponse):
    pass
