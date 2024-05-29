# coding: utf-8
"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python or TypeScript SDK.  To install the official [Python SDK](https://pypi.org/project/humanloop/), run the following command:  ```bash pip install humanloop ```  To install the official [TypeScript SDK](https://www.npmjs.com/package/humanloop), run the following command:  ```bash npm i humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://docs.humanloop.com/).

    The version of the OpenAPI document: 4.0.1
    Generated by: https://konfigthis.com
"""

from humanloop.paths.logs.delete import Delete
from humanloop.paths.logs_id.get import Get
from humanloop.paths.logs.get import List
from humanloop.paths.logs.post import Log
from humanloop.paths.logs_id.patch import Update
from humanloop.paths.logs.patch import UpdateByRef
from humanloop.apis.tags.logs_api_raw import LogsApiRaw


class LogsApiGenerated(
    Delete,
    Get,
    List,
    Log,
    Update,
    UpdateByRef,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: LogsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = LogsApiRaw(api_client)