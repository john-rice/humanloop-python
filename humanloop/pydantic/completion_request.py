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

from humanloop.pydantic.model_config_completion_request import ModelConfigCompletionRequest
from humanloop.pydantic.provider_api_keys import ProviderApiKeys

class CompletionRequest(BaseModel):
    # The model configuration used to generate.
    model_config_: ModelConfigCompletionRequest = Field(alias='model_config')

    # Unique project name. If no project exists with this name, a new project will be created.
    project: typing.Optional[str] = Field(None, alias='project')

    # Unique ID of a project to associate to the log. Either this or `project` must be provided.
    project_id: typing.Optional[str] = Field(None, alias='project_id')

    # ID of the session to associate the datapoint.
    session_id: typing.Optional[str] = Field(None, alias='session_id')

    # A unique string identifying the session to associate the datapoint to. Allows you to log multiple datapoints to a session (using an ID kept by your internal systems) by passing the same `session_reference_id` in subsequent log requests. Specify at most one of this or `session_id`.
    session_reference_id: typing.Optional[str] = Field(None, alias='session_reference_id')

    # ID associated to the parent datapoint in a session.
    parent_id: typing.Optional[str] = Field(None, alias='parent_id')

    # A unique string identifying the previously-logged parent datapoint in a session. Allows you to log nested datapoints with your internal system IDs by passing the same reference ID as `parent_id` in a prior log request. Specify at most one of this or `parent_id`. Note that this cannot refer to a datapoint being logged in the same request.
    parent_reference_id: typing.Optional[str] = Field(None, alias='parent_reference_id')

    # The inputs passed to the prompt template.
    inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='inputs')

    # Identifies where the model was called from.
    source: typing.Optional[str] = Field(None, alias='source')

    # Any additional metadata to record.
    metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='metadata')

    # Whether the request/response payloads will be stored on Humanloop.
    save: typing.Optional[bool] = Field(None, alias='save')

    # ID of the source datapoint if this is a log derived from a datapoint in a dataset.
    source_datapoint_id: typing.Optional[str] = Field(None, alias='source_datapoint_id')

    # API keys required by each provider to make API calls. The API keys provided here are not stored by Humanloop. If not specified here, Humanloop will fall back to the key saved to your organization.
    provider_api_keys: typing.Optional[ProviderApiKeys] = Field(None, alias='provider_api_keys')

    # The number of generations.
    num_samples: typing.Optional[int] = Field(None, alias='num_samples')

    # If true, tokens will be sent as data-only server-sent events. If num_samples > 1, samples are streamed back independently.
    stream: typing.Optional[bool] = Field(None, alias='stream')

    # End-user ID passed through to provider call.
    user: typing.Optional[str] = Field(None, alias='user')

    # WARNING: This property is deprecated
    # Deprecated field: the seed is instead set as part of the request.config object.
    seed: typing.Optional[int] = Field(None, alias='seed')

    # Whether to return the inputs in the response. If false, the response will contain an empty dictionary under inputs. This is useful for reducing the size of the response. Defaults to true.
    return_inputs: typing.Optional[bool] = Field(None, alias='return_inputs')

    # Include the log probabilities of the top n tokens in the provider_response
    logprobs: typing.Optional[int] = Field(None, alias='logprobs')

    # The suffix that comes after a completion of inserted text. Useful for completions that act like inserts.
    suffix: typing.Optional[str] = Field(None, alias='suffix')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
