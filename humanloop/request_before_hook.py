# coding: utf-8

"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python SDK.  To install the official Python SDK, run the following command:  ```bash pip install humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://humanloop.gitbook.io/humanloop-docs/).

    The version of the OpenAPI document: 4.0.0
    Generated by: https://konfigthis.com
"""

import typing
from urllib3._collections import HTTPHeaderDict
from humanloop.operation_parameter_map import operation_parameter_map
from humanloop.configuration import Configuration
from humanloop.type.provider_api_keys import ProviderApiKeys


def request_before_hook(
    resource_path: str,
    method: str,
    configuration: Configuration,
    path_template: str,
    headers: typing.Optional[HTTPHeaderDict] = None,
    body: typing.Any = None,
    fields: typing.Optional[typing.Tuple[typing.Tuple[str, str], ...]] = None,
    auth_settings: typing.Optional[typing.List[str]] = None,
    **kwargs: typing.Any,
):
    parameters = operation_parameter_map["{}-{}".format(path_template, method)]["parameters"]
    # if parameter does not exist with name "provider_api_keys", return
    if "provider_api_keys" not in map(lambda x: x["name"], parameters):
        return

    if not isinstance(body, dict):
        return
    api_keys: ProviderApiKeys = (
        body["provider_api_keys"] if "provider_api_keys" in body else {}
    )
    if "openapi" not in api_keys and configuration.openai_api_key is not None:
        api_keys["openai"] = configuration.openai_api_key
    if "anthropic" not in api_keys and configuration.anthropic_api_key is not None:
        api_keys["anthropic"] = configuration.anthropic_api_key
    if "cohere" not in api_keys and configuration.cohere_api_key is not None:
        api_keys["cohere"] = configuration.cohere_api_key
    if (
        "openenai_azure" not in api_keys
        and configuration.openai_azure_api_key is not None
    ):
        api_keys["openai_azure"] = configuration.openai_azure_api_key
    if (
        "openai_azure_endpoint" not in api_keys
        and configuration.openai_azure_endpoint_api_key is not None
    ):
        api_keys["openai_azure_endpoint"] = configuration.openai_azure_endpoint_api_key
    body["provider_api_keys"] = api_keys
