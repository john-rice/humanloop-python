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

from humanloop.pydantic.tool_source import ToolSource
from humanloop.pydantic.user_response import UserResponse

class ToolConfigResponse(BaseModel):
    # String ID of config. Starts with `config_`.
    id: str = Field(alias='id')

    type: Literal["tool"] = Field(alias='type')

    # Whether the config is committed or not.
    status: str = Field(alias='status')

    # Name for the tool referenced by the model.
    name: str = Field(alias='name')

    # Description of the tool referenced by the model
    description: typing.Optional[str] = Field(None, alias='description')

    # Definition of parameters needed to run the tool. Provided in jsonschema format: https://json-schema.org/
    parameters: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='parameters')

    # Other parameters that define the config.
    other: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='other')

    # The user who created the config.
    created_by: typing.Optional[UserResponse] = Field(None, alias='created_by')

    # Source of the tool. If defined at an organization level will be 'organization' else 'inline'.
    source: typing.Optional[ToolSource] = Field(None, alias='source')

    # Code source of the tool.
    source_code: typing.Optional[str] = Field(None, alias='source_code')

    # Definition of parameters needed to run the tool. Provided in jsonschema format: https://json-schema.org/
    setup_schema: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='setup_schema')

    # The function signature of the tool when being called.
    signature: typing.Optional[str] = Field(None, alias='signature')

    # Whether the tool is one where Humanloop defines runtime or not.
    is_preset: typing.Optional[bool] = Field(None, alias='is_preset')

    # If is_preset = true, this is the name of the preset tool on Humanloop. This is used as the key to lookup the Humanloop runtime of the tool
    preset_name: typing.Optional[str] = Field(None, alias='preset_name')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
