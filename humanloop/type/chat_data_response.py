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

from humanloop.type.chat_message_with_tool_call import ChatMessageWithToolCall
from humanloop.type.function_tool import FunctionTool
from humanloop.type.tool_call import ToolCall
from humanloop.type.tool_result_response import ToolResultResponse

class RequiredChatDataResponse(TypedDict):
    # Unique ID for the model inputs and output logged to Humanloop. Use this when recording feedback later.
    id: str

    # The index for the sampled generation for a given input. The num_samples request parameter controls how many samples are generated.
    index: int

    # Output text returned from the provider model with leading and trailing whitespaces stripped.
    output: str

    # Raw output text returned from the provider model.
    raw_output: str

    # The model configuration used to create the generation.
    model_config_id: str

    # The message returned by the provider.
    output_message: ChatMessageWithToolCall


class OptionalChatDataResponse(TypedDict, total=False):
    # The inputs passed to the chat template.
    inputs: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Why the generation ended. One of 'stop' (indicating a stop token was encountered), or 'length' (indicating the max tokens limit has been reached), or 'tool_call' (indicating that the model has chosen to call a tool - in which case the tool_call parameter of the response will be populated). It will be set as null for the intermediary responses during a stream, and will only be set as non-null for the final streamed token.
    finish_reason: str

    # Results of any tools run during the generation.
    tool_results: typing.List[ToolResultResponse]

    # The messages passed to the to provider chat endpoint.
    messages: typing.List[ChatMessageWithToolCall]

    # WARNING: This property is deprecated
    # Deprecated: Please use tool_calls field within the output_message.JSON definition of the tool to call and the corresponding argument values. Will be populated when finish_reason='tool_call'.
    tool_call: FunctionTool

    # Deprecated: Please use tool_calls field within the output_message.JSON definition of the tools to call and the corresponding argument values. Will be populated when finish_reason='tool_call'.
    tool_calls: typing.List[ToolCall]

class ChatDataResponse(RequiredChatDataResponse, OptionalChatDataResponse):
    pass
