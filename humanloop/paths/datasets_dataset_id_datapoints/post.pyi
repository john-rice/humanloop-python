# coding: utf-8

"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python or TypeScript SDK.  To install the official [Python SDK](https://pypi.org/project/humanloop/), run the following command:  ```bash pip install humanloop ```  To install the official [TypeScript SDK](https://www.npmjs.com/package/humanloop), run the following command:  ```bash npm i humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://docs.humanloop.com/).

    The version of the OpenAPI document: 4.0.1
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from humanloop.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from humanloop.api_response import AsyncGeneratorResponse
from humanloop import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from humanloop import schemas  # noqa: F401

from humanloop.model.datasets_create_datapoint_request import DatasetsCreateDatapointRequest as DatasetsCreateDatapointRequestSchema
from humanloop.model.http_validation_error import HTTPValidationError as HTTPValidationErrorSchema
from humanloop.model.datasets_create_datapoint_response import DatasetsCreateDatapointResponse as DatasetsCreateDatapointResponseSchema
from humanloop.model.create_datapoints_by_logs_request_log_ids import CreateDatapointsByLogsRequestLogIds as CreateDatapointsByLogsRequestLogIdsSchema
from humanloop.model.chat_message_with_tool_call import ChatMessageWithToolCall as ChatMessageWithToolCallSchema
from humanloop.model.create_datapoint_request_target import CreateDatapointRequestTarget as CreateDatapointRequestTargetSchema
from humanloop.model.create_datapoint_request_inputs import CreateDatapointRequestInputs as CreateDatapointRequestInputsSchema

from humanloop.type.create_datapoint_request_target import CreateDatapointRequestTarget
from humanloop.type.datasets_create_datapoint_response import DatasetsCreateDatapointResponse
from humanloop.type.create_datapoints_by_logs_request_log_ids import CreateDatapointsByLogsRequestLogIds
from humanloop.type.create_datapoint_request_inputs import CreateDatapointRequestInputs
from humanloop.type.chat_message_with_tool_call import ChatMessageWithToolCall
from humanloop.type.http_validation_error import HTTPValidationError
from humanloop.type.datasets_create_datapoint_request import DatasetsCreateDatapointRequest

from ...api_client import Dictionary
from humanloop.pydantic.datasets_create_datapoint_response import DatasetsCreateDatapointResponse as DatasetsCreateDatapointResponsePydantic
from humanloop.pydantic.create_datapoints_by_logs_request_log_ids import CreateDatapointsByLogsRequestLogIds as CreateDatapointsByLogsRequestLogIdsPydantic
from humanloop.pydantic.http_validation_error import HTTPValidationError as HTTPValidationErrorPydantic
from humanloop.pydantic.datasets_create_datapoint_request import DatasetsCreateDatapointRequest as DatasetsCreateDatapointRequestPydantic
from humanloop.pydantic.create_datapoint_request_target import CreateDatapointRequestTarget as CreateDatapointRequestTargetPydantic
from humanloop.pydantic.create_datapoint_request_inputs import CreateDatapointRequestInputs as CreateDatapointRequestInputsPydantic
from humanloop.pydantic.chat_message_with_tool_call import ChatMessageWithToolCall as ChatMessageWithToolCallPydantic

# Path params
DatasetIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'dataset_id': typing.Union[DatasetIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_dataset_id = api_client.PathParameter(
    name="dataset_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=DatasetIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = DatasetsCreateDatapointRequestSchema


request_body_datasets_create_datapoint_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor201ResponseBodyApplicationJson = DatasetsCreateDatapointResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: DatasetsCreateDatapointResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: DatasetsCreateDatapointResponse


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = HTTPValidationErrorSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: HTTPValidationError


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: HTTPValidationError


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_datapoint_mapped_args(
        self,
        dataset_id: str,
        body: typing.Optional[DatasetsCreateDatapointRequest] = None,
        log_ids: typing.Optional[CreateDatapointsByLogsRequestLogIds] = None,
        inputs: typing.Optional[CreateDatapointRequestInputs] = None,
        messages: typing.Optional[typing.List[ChatMessageWithToolCall]] = None,
        target: typing.Optional[CreateDatapointRequestTarget] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if log_ids is not None:
            _body["log_ids"] = log_ids
        if inputs is not None:
            _body["inputs"] = inputs
        if messages is not None:
            _body["messages"] = messages
        if target is not None:
            _body["target"] = target
        args.body = body if body is not None else _body
        if dataset_id is not None:
            _path_params["dataset_id"] = dataset_id
        args.path = _path_params
        return args

    async def _acreate_datapoint_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create Datapoint
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_dataset_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/datasets/{dataset_id}/datapoints',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_datasets_create_datapoint_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_datapoint_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create Datapoint
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_dataset_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/datasets/{dataset_id}/datapoints',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_datasets_create_datapoint_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateDatapointRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_datapoint(
        self,
        dataset_id: str,
        body: typing.Optional[DatasetsCreateDatapointRequest] = None,
        log_ids: typing.Optional[CreateDatapointsByLogsRequestLogIds] = None,
        inputs: typing.Optional[CreateDatapointRequestInputs] = None,
        messages: typing.Optional[typing.List[ChatMessageWithToolCall]] = None,
        target: typing.Optional[CreateDatapointRequestTarget] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_datapoint_mapped_args(
            body=body,
            dataset_id=dataset_id,
            log_ids=log_ids,
            inputs=inputs,
            messages=messages,
            target=target,
        )
        return await self._acreate_datapoint_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def create_datapoint(
        self,
        dataset_id: str,
        body: typing.Optional[DatasetsCreateDatapointRequest] = None,
        log_ids: typing.Optional[CreateDatapointsByLogsRequestLogIds] = None,
        inputs: typing.Optional[CreateDatapointRequestInputs] = None,
        messages: typing.Optional[typing.List[ChatMessageWithToolCall]] = None,
        target: typing.Optional[CreateDatapointRequestTarget] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_datapoint_mapped_args(
            body=body,
            dataset_id=dataset_id,
            log_ids=log_ids,
            inputs=inputs,
            messages=messages,
            target=target,
        )
        return self._create_datapoint_oapg(
            body=args.body,
            path_params=args.path,
        )

class CreateDatapoint(BaseApi):

    async def acreate_datapoint(
        self,
        dataset_id: str,
        body: typing.Optional[DatasetsCreateDatapointRequest] = None,
        log_ids: typing.Optional[CreateDatapointsByLogsRequestLogIds] = None,
        inputs: typing.Optional[CreateDatapointRequestInputs] = None,
        messages: typing.Optional[typing.List[ChatMessageWithToolCall]] = None,
        target: typing.Optional[CreateDatapointRequestTarget] = None,
        validate: bool = False,
        **kwargs,
    ) -> DatasetsCreateDatapointResponsePydantic:
        raw_response = await self.raw.acreate_datapoint(
            body=body,
            dataset_id=dataset_id,
            log_ids=log_ids,
            inputs=inputs,
            messages=messages,
            target=target,
            **kwargs,
        )
        if validate:
            return RootModel[DatasetsCreateDatapointResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(DatasetsCreateDatapointResponsePydantic, raw_response.body)
    
    
    def create_datapoint(
        self,
        dataset_id: str,
        body: typing.Optional[DatasetsCreateDatapointRequest] = None,
        log_ids: typing.Optional[CreateDatapointsByLogsRequestLogIds] = None,
        inputs: typing.Optional[CreateDatapointRequestInputs] = None,
        messages: typing.Optional[typing.List[ChatMessageWithToolCall]] = None,
        target: typing.Optional[CreateDatapointRequestTarget] = None,
        validate: bool = False,
    ) -> DatasetsCreateDatapointResponsePydantic:
        raw_response = self.raw.create_datapoint(
            body=body,
            dataset_id=dataset_id,
            log_ids=log_ids,
            inputs=inputs,
            messages=messages,
            target=target,
        )
        if validate:
            return RootModel[DatasetsCreateDatapointResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(DatasetsCreateDatapointResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        dataset_id: str,
        body: typing.Optional[DatasetsCreateDatapointRequest] = None,
        log_ids: typing.Optional[CreateDatapointsByLogsRequestLogIds] = None,
        inputs: typing.Optional[CreateDatapointRequestInputs] = None,
        messages: typing.Optional[typing.List[ChatMessageWithToolCall]] = None,
        target: typing.Optional[CreateDatapointRequestTarget] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_datapoint_mapped_args(
            body=body,
            dataset_id=dataset_id,
            log_ids=log_ids,
            inputs=inputs,
            messages=messages,
            target=target,
        )
        return await self._acreate_datapoint_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        dataset_id: str,
        body: typing.Optional[DatasetsCreateDatapointRequest] = None,
        log_ids: typing.Optional[CreateDatapointsByLogsRequestLogIds] = None,
        inputs: typing.Optional[CreateDatapointRequestInputs] = None,
        messages: typing.Optional[typing.List[ChatMessageWithToolCall]] = None,
        target: typing.Optional[CreateDatapointRequestTarget] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_datapoint_mapped_args(
            body=body,
            dataset_id=dataset_id,
            log_ids=log_ids,
            inputs=inputs,
            messages=messages,
            target=target,
        )
        return self._create_datapoint_oapg(
            body=args.body,
            path_params=args.path,
        )

