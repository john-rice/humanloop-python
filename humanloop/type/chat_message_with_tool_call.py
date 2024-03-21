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

from humanloop.type.chat_role import ChatRole
from humanloop.type.function_tool_nullable import FunctionToolNullable
from humanloop.type.image_chat_content import ImageChatContent
from humanloop.type.text_chat_content import TextChatContent
from humanloop.type.tool_call import ToolCall

class RequiredChatMessageWithToolCall(TypedDict):
    # Role of the message author.
    role: ChatRole

class OptionalChatMessageWithToolCall(TypedDict, total=False):
    # The content of the message.
    content: typing.Union[str, typing.List[typing.Union[typing.List[TextChatContent], typing.List[ImageChatContent]]]]

    # Optional name of the message author.
    name: typing.Optional[str]

    # Tool call that this message is responding to.
    tool_call_id: typing.Optional[str]

    # A list of tool calls requested by the assistant.
    tool_calls: typing.Optional[typing.List[ToolCall]]

    # WARNING: This property is deprecated
    # NB: Deprecated in favour of tool_calls. A tool call requested by the assistant.
    tool_call: typing.Optional[FunctionToolNullable]

class ChatMessageWithToolCall(RequiredChatMessageWithToolCall, OptionalChatMessageWithToolCall):
    pass
