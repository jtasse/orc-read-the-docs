# Documentation for Orbital Refuse Collector (ORC) API

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *https://orc.wiremockapi.cloud*

| Class | Method | HTTP request | Description |
|------------ | ------------- | ------------- | -------------|
| *DefaultApi* | [**deleteSatelliteById**](Apis/DefaultApi.md#deletesatellitebyid) | **DELETE** /satellites/{id} | Delete a satellite |
*DefaultApi* | [**getSatelliteById**](Apis/DefaultApi.md#getsatellitebyid) | **GET** /satellites/{id} | Get a satellite by ID |
*DefaultApi* | [**getSatellites**](Apis/DefaultApi.md#getsatellites) | **GET** /satellites | Get a list of satellites |
*DefaultApi* | [**scheduleDecommissionForSatellite**](Apis/DefaultApi.md#scheduledecommissionforsatellite) | **POST** /satellites/scheduleDecommission | Schedule decommission for a satellite |
*DefaultApi* | [**updateSatellite**](Apis/DefaultApi.md#updatesatellite) | **PUT** /satellites | Update a satellite |


<a name="documentation-for-models"></a>
## Documentation for Models

 - [DecommissionSchedule](./Models/DecommissionSchedule.md)
 - [Satellite](./Models/Satellite.md)


<a name="documentation-for-authorization"></a>
## Documentation for Authorization

All endpoints do not require authorization.
