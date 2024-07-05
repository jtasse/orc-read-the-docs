# DefaultApi

All URIs are relative to *https://orc.wiremockapi.cloud*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteSatelliteById**](DefaultApi.md#deleteSatelliteById) | **DELETE** /satellites/{id} | Delete a satellite |
| [**getSatelliteById**](DefaultApi.md#getSatelliteById) | **GET** /satellites/{id} | Get a satellite by ID |
| [**getSatellites**](DefaultApi.md#getSatellites) | **GET** /satellites | Get a list of satellites |
| [**scheduleDecommissionForSatellite**](DefaultApi.md#scheduleDecommissionForSatellite) | **POST** /satellites/scheduleDecommission | Schedule decommission for a satellite |
| [**updateSatellite**](DefaultApi.md#updateSatellite) | **PUT** /satellites | Update a satellite |


<a name="deleteSatelliteById"></a>
# **deleteSatelliteById**
> deleteSatelliteById(id)

Delete a satellite

    Delete a satellite with the specified ID

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| Satellite ID | [default to null] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="getSatelliteById"></a>
# **getSatelliteById**
> Satellite getSatelliteById(id)

Get a satellite by ID

    Get a satellite with the specified ID

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| Satellite ID | [default to null] |

### Return type

[**Satellite**](../Models/Satellite.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getSatellites"></a>
# **getSatellites**
> Satellite getSatellites(satellitesToRetrieve)

Get a list of satellites

    Returns a list of all satellites

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **satellitesToRetrieve** | **Integer**| Number of satellites to retrieve | [default to null] |

### Return type

[**Satellite**](../Models/Satellite.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="scheduleDecommissionForSatellite"></a>
# **scheduleDecommissionForSatellite**
> scheduleDecommissionForSatellite(DecommissionSchedule)

Schedule decommission for a satellite

    Schedule a decommission for the satellite with the specified ID

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **DecommissionSchedule** | [**DecommissionSchedule**](../Models/DecommissionSchedule.md)| Time at which the satellite should be decommissioned | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

<a name="updateSatellite"></a>
# **updateSatellite**
> Satellite updateSatellite(Satellite)

Update a satellite

    Update a satellite with the specified ID

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **Satellite** | [**Satellite**](../Models/Satellite.md)| Updated satellite information | |

### Return type

[**Satellite**](../Models/Satellite.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

