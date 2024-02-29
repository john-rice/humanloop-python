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

from humanloop.model.http_validation_error import HTTPValidationError as HTTPValidationErrorSchema
from humanloop.model.paginated_data_log_response import PaginatedDataLogResponse as PaginatedDataLogResponseSchema

from humanloop.type.paginated_data_log_response import PaginatedDataLogResponse
from humanloop.type.http_validation_error import HTTPValidationError

from ...api_client import Dictionary
from humanloop.pydantic.paginated_data_log_response import PaginatedDataLogResponse as PaginatedDataLogResponsePydantic
from humanloop.pydantic.http_validation_error import HTTPValidationError as HTTPValidationErrorPydantic

from . import path

# Query params
ProjectIdSchema = schemas.StrSchema
SearchSchema = schemas.StrSchema
MetadataSearchSchema = schemas.StrSchema
StartDateSchema = schemas.DateSchema
EndDateSchema = schemas.DateSchema
SizeSchema = schemas.IntSchema
PageSchema = schemas.IntSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'project_id': typing.Union[ProjectIdSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'search': typing.Union[SearchSchema, str, ],
        'metadata_search': typing.Union[MetadataSearchSchema, str, ],
        'start_date': typing.Union[StartDateSchema, str, date, ],
        'end_date': typing.Union[EndDateSchema, str, date, ],
        'size': typing.Union[SizeSchema, decimal.Decimal, int, ],
        'page': typing.Union[PageSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_project_id = api_client.QueryParameter(
    name="project_id",
    style=api_client.ParameterStyle.FORM,
    schema=ProjectIdSchema,
    required=True,
    explode=True,
)
request_query_search = api_client.QueryParameter(
    name="search",
    style=api_client.ParameterStyle.FORM,
    schema=SearchSchema,
    explode=True,
)
request_query_metadata_search = api_client.QueryParameter(
    name="metadata_search",
    style=api_client.ParameterStyle.FORM,
    schema=MetadataSearchSchema,
    explode=True,
)
request_query_start_date = api_client.QueryParameter(
    name="start_date",
    style=api_client.ParameterStyle.FORM,
    schema=StartDateSchema,
    explode=True,
)
request_query_end_date = api_client.QueryParameter(
    name="end_date",
    style=api_client.ParameterStyle.FORM,
    schema=EndDateSchema,
    explode=True,
)
request_query_size = api_client.QueryParameter(
    name="size",
    style=api_client.ParameterStyle.FORM,
    schema=SizeSchema,
    explode=True,
)
request_query_page = api_client.QueryParameter(
    name="page",
    style=api_client.ParameterStyle.FORM,
    schema=PageSchema,
    explode=True,
)
_auth = [
    'APIKeyHeader',
]
SchemaFor200ResponseBodyApplicationJson = PaginatedDataLogResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PaginatedDataLogResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PaginatedDataLogResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
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
_status_code_to_response = {
    '200': _response_for_200,
    '422': _response_for_422,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_mapped_args(
        self,
        project_id: str,
        search: typing.Optional[str] = None,
        metadata_search: typing.Optional[str] = None,
        start_date: typing.Optional[date] = None,
        end_date: typing.Optional[date] = None,
        size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if project_id is not None:
            _query_params["project_id"] = project_id
        if search is not None:
            _query_params["search"] = search
        if metadata_search is not None:
            _query_params["metadata_search"] = metadata_search
        if start_date is not None:
            _query_params["start_date"] = start_date
        if end_date is not None:
            _query_params["end_date"] = end_date
        if size is not None:
            _query_params["size"] = size
        if page is not None:
            _query_params["page"] = page
        args.query = _query_params
        return args

    async def _alist_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        List 
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_project_id,
            request_query_search,
            request_query_metadata_search,
            request_query_start_date,
            request_query_end_date,
            request_query_size,
            request_query_page,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/logs',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _list_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        List 
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_project_id,
            request_query_search,
            request_query_metadata_search,
            request_query_start_date,
            request_query_end_date,
            request_query_size,
            request_query_page,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/logs',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


class ListRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist(
        self,
        project_id: str,
        search: typing.Optional[str] = None,
        metadata_search: typing.Optional[str] = None,
        start_date: typing.Optional[date] = None,
        end_date: typing.Optional[date] = None,
        size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_mapped_args(
            project_id=project_id,
            search=search,
            metadata_search=metadata_search,
            start_date=start_date,
            end_date=end_date,
            size=size,
            page=page,
        )
        return await self._alist_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list(
        self,
        project_id: str,
        search: typing.Optional[str] = None,
        metadata_search: typing.Optional[str] = None,
        start_date: typing.Optional[date] = None,
        end_date: typing.Optional[date] = None,
        size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_mapped_args(
            project_id=project_id,
            search=search,
            metadata_search=metadata_search,
            start_date=start_date,
            end_date=end_date,
            size=size,
            page=page,
        )
        return self._list_oapg(
            query_params=args.query,
        )

class List(BaseApi):

    async def alist(
        self,
        project_id: str,
        search: typing.Optional[str] = None,
        metadata_search: typing.Optional[str] = None,
        start_date: typing.Optional[date] = None,
        end_date: typing.Optional[date] = None,
        size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> PaginatedDataLogResponsePydantic:
        raw_response = await self.raw.alist(
            project_id=project_id,
            search=search,
            metadata_search=metadata_search,
            start_date=start_date,
            end_date=end_date,
            size=size,
            page=page,
            **kwargs,
        )
        if validate:
            return PaginatedDataLogResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(PaginatedDataLogResponsePydantic, raw_response.body)
    
    
    def list(
        self,
        project_id: str,
        search: typing.Optional[str] = None,
        metadata_search: typing.Optional[str] = None,
        start_date: typing.Optional[date] = None,
        end_date: typing.Optional[date] = None,
        size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        validate: bool = False,
    ) -> PaginatedDataLogResponsePydantic:
        raw_response = self.raw.list(
            project_id=project_id,
            search=search,
            metadata_search=metadata_search,
            start_date=start_date,
            end_date=end_date,
            size=size,
            page=page,
        )
        if validate:
            return PaginatedDataLogResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(PaginatedDataLogResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        project_id: str,
        search: typing.Optional[str] = None,
        metadata_search: typing.Optional[str] = None,
        start_date: typing.Optional[date] = None,
        end_date: typing.Optional[date] = None,
        size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_mapped_args(
            project_id=project_id,
            search=search,
            metadata_search=metadata_search,
            start_date=start_date,
            end_date=end_date,
            size=size,
            page=page,
        )
        return await self._alist_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        project_id: str,
        search: typing.Optional[str] = None,
        metadata_search: typing.Optional[str] = None,
        start_date: typing.Optional[date] = None,
        end_date: typing.Optional[date] = None,
        size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_mapped_args(
            project_id=project_id,
            search=search,
            metadata_search=metadata_search,
            start_date=start_date,
            end_date=end_date,
            size=size,
            page=page,
        )
        return self._list_oapg(
            query_params=args.query,
        )

