# -*- coding: utf-8 -*-

"""
***************************************************************************
    __init__.py
    ---------------------
    Date                 : October 2014
    Copyright            : (C) 2014 by Alessandro Pasotti
    Email                : elpaso at itopen dot it
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Alessandro Pasotti'
__date__ = 'October 2014'
__copyright__ = '(C) 2014, Alessandro Pasotti'

from qgis.PyQt import QtCore     # NOQA

from qgis._server import *  # NOQA

"""
This folder is completed using sipify.py script
It is not aimed to be manually edited
"""
# The following has been generated automatically from src/server/qgsaccesscontrol.h
try:
    QgsAccessControl.__overridden_methods__ = ['isFilterThreadSafe', 'filterFeatures', 'layerAttributes', 'clone']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/server/qgsaccesscontrolfilter.h
try:
    QgsAccessControlFilter.__virtual_methods__ = ['layerFilterExpression', 'layerFilterSubsetString', 'layerPermissions', 'authorizedLayerAttributes', 'allowToEdit', 'cacheKey']
except (NameError, AttributeError):
    pass
try:
    QgsAccessControlFilter.LayerPermissions.__doc__ = """Describe the layer permission"""
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/server/qgsbufferserverrequest.h
try:
    QgsBufferServerRequest.__overridden_methods__ = ['data']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/server/qgsbufferserverresponse.h
try:
    QgsBufferServerResponse.__overridden_methods__ = ['setHeader', 'addHeader', 'removeHeader', 'header', 'fullHeaders', 'fullHeader', 'headers', 'headersSent', 'setStatusCode', 'statusCode', 'sendError', 'io', 'finish', 'flush', 'clear', 'data', 'truncate']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/server/qgsconfigcache.h
try:
    QgsConfigCache.__attribute_docs__ = {'projectRemovedFromCache': 'Emitted whenever a project is removed from the cache.\n\n.. versionadded:: 3.38\n'}
    QgsConfigCache.initialize = staticmethod(QgsConfigCache.initialize)
    QgsConfigCache.instance = staticmethod(QgsConfigCache.instance)
    QgsConfigCache.__signal_arguments__ = {'projectRemovedFromCache': ['path: str']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/server/qgsfcgiserverrequest.h
try:
    QgsFcgiServerRequest.__overridden_methods__ = ['data', 'header']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/server/qgsfeaturefilter.h
try:
    QgsFeatureFilter.__overridden_methods__ = ['isFilterThreadSafe', 'filterFeatures', 'layerAttributes', 'clone']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/server/qgsfeaturefilterprovidergroup.h
try:
    QgsFeatureFilterProviderGroup.__overridden_methods__ = ['isFilterThreadSafe', 'filterFeatures', 'layerAttributes', 'clone']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/server/qgsserverapi.h
try:
    QgsServerApi.__virtual_methods__ = ['accept']
    QgsServerApi.__abstract_methods__ = ['executeRequest']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/server/qgsserverapiutils.h
try:
    QgsServerApiUtils.parseBbox = staticmethod(QgsServerApiUtils.parseBbox)
    QgsServerApiUtils.temporalDimensions = staticmethod(QgsServerApiUtils.temporalDimensions)
    QgsServerApiUtils.parseTemporalDateInterval = staticmethod(QgsServerApiUtils.parseTemporalDateInterval)
    QgsServerApiUtils.parseTemporalDateTimeInterval = staticmethod(QgsServerApiUtils.parseTemporalDateTimeInterval)
    QgsServerApiUtils.fieldName = staticmethod(QgsServerApiUtils.fieldName)
    QgsServerApiUtils.temporalFilterExpression = staticmethod(QgsServerApiUtils.temporalFilterExpression)
    QgsServerApiUtils.temporalExtent = staticmethod(QgsServerApiUtils.temporalExtent)
    QgsServerApiUtils.parseCrs = staticmethod(QgsServerApiUtils.parseCrs)
    QgsServerApiUtils.sanitizedFieldValue = staticmethod(QgsServerApiUtils.sanitizedFieldValue)
    QgsServerApiUtils.publishedCrsList = staticmethod(QgsServerApiUtils.publishedCrsList)
    QgsServerApiUtils.crsToOgcUri = staticmethod(QgsServerApiUtils.crsToOgcUri)
    QgsServerApiUtils.appendMapParameter = staticmethod(QgsServerApiUtils.appendMapParameter)
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/server/qgsservercachefilter.h
try:
    QgsServerCacheFilter.__virtual_methods__ = ['getCachedDocument', 'setCachedDocument', 'deleteCachedDocument', 'deleteCachedDocuments', 'getCachedImage', 'setCachedImage', 'deleteCachedImage', 'deleteCachedImages']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/server/qgsserverexception.h
try:
    QgsServerException.__virtual_methods__ = ['formatResponse']
except (NameError, AttributeError):
    pass
try:
    QgsOgcServiceException.__overridden_methods__ = ['formatResponse']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/server/qgsserverfeatureid.h
try:
    QgsServerFeatureId.getServerFid = staticmethod(QgsServerFeatureId.getServerFid)
    QgsServerFeatureId.updateFeatureRequestFromServerFids = staticmethod(QgsServerFeatureId.updateFeatureRequestFromServerFids)
    QgsServerFeatureId.getExpressionFromServerFid = staticmethod(QgsServerFeatureId.getExpressionFromServerFid)
    QgsServerFeatureId.pkSeparator = staticmethod(QgsServerFeatureId.pkSeparator)
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/server/qgsserverfilter.h
try:
    QgsServerFilter.__virtual_methods__ = ['requestReady', 'responseComplete', 'sendResponse', 'onRequestReady', 'onProjectReady', 'onResponseComplete', 'onSendResponse']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/server/qgsserverinterface.h
try:
    QgsServerInterface.__abstract_methods__ = ['capabilitiesCache', 'requestHandler', 'registerFilter', 'setFilters', 'filters', 'registerAccessControl', 'accessControls', 'registerServerCache', 'cacheManager', 'getEnv', 'configFilePath', 'setConfigFilePath', 'removeConfigCacheEntry', 'serviceRegistry', 'reloadSettings']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/server/qgsserverlogger.h
try:
    QgsServerLogger.instance = staticmethod(QgsServerLogger.instance)
    QgsServerLogger.__overridden_methods__ = ['logMessage']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/server/qgsserverogcapi.h
QgsServerOgcApi.alternate = QgsServerOgcApi.Rel.alternate
QgsServerOgcApi.describedBy = QgsServerOgcApi.Rel.describedBy
QgsServerOgcApi.collection = QgsServerOgcApi.Rel.collection
QgsServerOgcApi.item = QgsServerOgcApi.Rel.item
QgsServerOgcApi.self = QgsServerOgcApi.Rel.self
QgsServerOgcApi.service_desc = QgsServerOgcApi.Rel.service_desc
QgsServerOgcApi.service_doc = QgsServerOgcApi.Rel.service_doc
QgsServerOgcApi.prev = QgsServerOgcApi.Rel.prev
QgsServerOgcApi.next = QgsServerOgcApi.Rel.next
QgsServerOgcApi.license = QgsServerOgcApi.Rel.license
QgsServerOgcApi.items = QgsServerOgcApi.Rel.items
QgsServerOgcApi.conformance = QgsServerOgcApi.Rel.conformance
QgsServerOgcApi.data = QgsServerOgcApi.Rel.data
QgsServerOgcApi.Rel.baseClass = QgsServerOgcApi
QgsServerOgcApi.GEOJSON = QgsServerOgcApi.ContentType.GEOJSON
QgsServerOgcApi.OPENAPI3 = QgsServerOgcApi.ContentType.OPENAPI3
QgsServerOgcApi.JSON = QgsServerOgcApi.ContentType.JSON
QgsServerOgcApi.HTML = QgsServerOgcApi.ContentType.HTML
QgsServerOgcApi.XML = QgsServerOgcApi.ContentType.XML
QgsServerOgcApi.FLATGEOBUF = QgsServerOgcApi.ContentType.FLATGEOBUF
QgsServerOgcApi.ContentType.baseClass = QgsServerOgcApi
# monkey patching scoped based enum
QgsServerOgcApi.Profile.NONE.__doc__ = "No profile"
QgsServerOgcApi.Profile.RFC7946.__doc__ = "GeoJSON profile according to RFC7946"
QgsServerOgcApi.Profile.__doc__ = """JSON profile

* ``NONE``: No profile
* ``RFC7946``: GeoJSON profile according to RFC7946

"""
# --
QgsServerOgcApi.Profile.baseClass = QgsServerOgcApi
try:
    QgsServerOgcApi.sanitizeUrl = staticmethod(QgsServerOgcApi.sanitizeUrl)
    QgsServerOgcApi.relToString = staticmethod(QgsServerOgcApi.relToString)
    QgsServerOgcApi.contentTypeToString = staticmethod(QgsServerOgcApi.contentTypeToString)
    QgsServerOgcApi.contentTypeToStdString = staticmethod(QgsServerOgcApi.contentTypeToStdString)
    QgsServerOgcApi.contentTypeToExtension = staticmethod(QgsServerOgcApi.contentTypeToExtension)
    QgsServerOgcApi.contenTypeFromExtension = staticmethod(QgsServerOgcApi.contenTypeFromExtension)
    QgsServerOgcApi.contentTypeFromExtension = staticmethod(QgsServerOgcApi.contentTypeFromExtension)
    QgsServerOgcApi.mimeType = staticmethod(QgsServerOgcApi.mimeType)
    QgsServerOgcApi.__overridden_methods__ = ['name', 'description', 'version', 'rootPath', 'executeRequest']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/server/qgsserverogcapihandler.h
try:
    QgsServerOgcApiHandler.parentLink = staticmethod(QgsServerOgcApiHandler.parentLink)
    QgsServerOgcApiHandler.layerFromCollectionId = staticmethod(QgsServerOgcApiHandler.layerFromCollectionId)
    QgsServerOgcApiHandler.__virtual_methods__ = ['parameters', 'tags', 'defaultContentType', 'handleRequest', 'values']
    QgsServerOgcApiHandler.__abstract_methods__ = ['path', 'operationId', 'summary', 'description', 'linkTitle', 'linkType']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/server/qgsserverparameters.h
QgsServerParameter.UNKNOWN = QgsServerParameter.Name.UNKNOWN
QgsServerParameter.SERVICE = QgsServerParameter.Name.SERVICE
QgsServerParameter.VERSION_SERVICE = QgsServerParameter.Name.VERSION_SERVICE
QgsServerParameter.REQUEST = QgsServerParameter.Name.REQUEST
QgsServerParameter.MAP = QgsServerParameter.Name.MAP
QgsServerParameter.FILE_NAME = QgsServerParameter.Name.FILE_NAME
QgsServerParameter.Name.baseClass = QgsServerParameter
try:
    QgsServerParameterDefinition.raiseError = staticmethod(QgsServerParameterDefinition.raiseError)
    QgsServerParameterDefinition.__virtual_methods__ = ['isValid']
except (NameError, AttributeError):
    pass
try:
    QgsServerParameter.name = staticmethod(QgsServerParameter.name)
except (NameError, AttributeError):
    pass
try:
    QgsServerParameters.__virtual_methods__ = ['request', 'version', 'loadParameter']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/server/qgsserverprojectutils.h
try:
    QgsServerProjectUtils.owsServiceCapabilities = staticmethod(QgsServerProjectUtils.owsServiceCapabilities)
    QgsServerProjectUtils.owsServiceTitle = staticmethod(QgsServerProjectUtils.owsServiceTitle)
    QgsServerProjectUtils.owsServiceAbstract = staticmethod(QgsServerProjectUtils.owsServiceAbstract)
    QgsServerProjectUtils.owsServiceKeywords = staticmethod(QgsServerProjectUtils.owsServiceKeywords)
    QgsServerProjectUtils.owsServiceOnlineResource = staticmethod(QgsServerProjectUtils.owsServiceOnlineResource)
    QgsServerProjectUtils.owsServiceContactOrganization = staticmethod(QgsServerProjectUtils.owsServiceContactOrganization)
    QgsServerProjectUtils.owsServiceContactPosition = staticmethod(QgsServerProjectUtils.owsServiceContactPosition)
    QgsServerProjectUtils.owsServiceContactPerson = staticmethod(QgsServerProjectUtils.owsServiceContactPerson)
    QgsServerProjectUtils.owsServiceContactMail = staticmethod(QgsServerProjectUtils.owsServiceContactMail)
    QgsServerProjectUtils.owsServiceContactPhone = staticmethod(QgsServerProjectUtils.owsServiceContactPhone)
    QgsServerProjectUtils.owsServiceFees = staticmethod(QgsServerProjectUtils.owsServiceFees)
    QgsServerProjectUtils.owsServiceAccessConstraints = staticmethod(QgsServerProjectUtils.owsServiceAccessConstraints)
    QgsServerProjectUtils.wmsMaxWidth = staticmethod(QgsServerProjectUtils.wmsMaxWidth)
    QgsServerProjectUtils.wmsMaxHeight = staticmethod(QgsServerProjectUtils.wmsMaxHeight)
    QgsServerProjectUtils.wmsImageQuality = staticmethod(QgsServerProjectUtils.wmsImageQuality)
    QgsServerProjectUtils.wmsTileBuffer = staticmethod(QgsServerProjectUtils.wmsTileBuffer)
    QgsServerProjectUtils.wmsRenderMapTiles = staticmethod(QgsServerProjectUtils.wmsRenderMapTiles)
    QgsServerProjectUtils.wmsMaxAtlasFeatures = staticmethod(QgsServerProjectUtils.wmsMaxAtlasFeatures)
    QgsServerProjectUtils.wmsDefaultMapUnitsPerMm = staticmethod(QgsServerProjectUtils.wmsDefaultMapUnitsPerMm)
    QgsServerProjectUtils.wmsUseLayerIds = staticmethod(QgsServerProjectUtils.wmsUseLayerIds)
    QgsServerProjectUtils.wmsInfoFormatSia2045 = staticmethod(QgsServerProjectUtils.wmsInfoFormatSia2045)
    QgsServerProjectUtils.wmsFeatureInfoAddWktGeometry = staticmethod(QgsServerProjectUtils.wmsFeatureInfoAddWktGeometry)
    QgsServerProjectUtils.wmsFeatureInfoUseAttributeFormSettings = staticmethod(QgsServerProjectUtils.wmsFeatureInfoUseAttributeFormSettings)
    QgsServerProjectUtils.wmsHTMLFeatureInfoUseOnlyMaptip = staticmethod(QgsServerProjectUtils.wmsHTMLFeatureInfoUseOnlyMaptip)
    QgsServerProjectUtils.wmsFeatureInfoSegmentizeWktGeometry = staticmethod(QgsServerProjectUtils.wmsFeatureInfoSegmentizeWktGeometry)
    QgsServerProjectUtils.wmsAddLegendGroupsLegendGraphic = staticmethod(QgsServerProjectUtils.wmsAddLegendGroupsLegendGraphic)
    QgsServerProjectUtils.wmsSkipNameForGroup = staticmethod(QgsServerProjectUtils.wmsSkipNameForGroup)
    QgsServerProjectUtils.wmsFeatureInfoPrecision = staticmethod(QgsServerProjectUtils.wmsFeatureInfoPrecision)
    QgsServerProjectUtils.wmsFeatureInfoDocumentElement = staticmethod(QgsServerProjectUtils.wmsFeatureInfoDocumentElement)
    QgsServerProjectUtils.wmsFeatureInfoDocumentElementNs = staticmethod(QgsServerProjectUtils.wmsFeatureInfoDocumentElementNs)
    QgsServerProjectUtils.wmsFeatureInfoSchema = staticmethod(QgsServerProjectUtils.wmsFeatureInfoSchema)
    QgsServerProjectUtils.wmsFeatureInfoLayerAliasMap = staticmethod(QgsServerProjectUtils.wmsFeatureInfoLayerAliasMap)
    QgsServerProjectUtils.wmsInspireActivate = staticmethod(QgsServerProjectUtils.wmsInspireActivate)
    QgsServerProjectUtils.wmsInspireLanguage = staticmethod(QgsServerProjectUtils.wmsInspireLanguage)
    QgsServerProjectUtils.wmsInspireMetadataUrl = staticmethod(QgsServerProjectUtils.wmsInspireMetadataUrl)
    QgsServerProjectUtils.wmsInspireMetadataUrlType = staticmethod(QgsServerProjectUtils.wmsInspireMetadataUrlType)
    QgsServerProjectUtils.wmsInspireTemporalReference = staticmethod(QgsServerProjectUtils.wmsInspireTemporalReference)
    QgsServerProjectUtils.wmsInspireMetadataDate = staticmethod(QgsServerProjectUtils.wmsInspireMetadataDate)
    QgsServerProjectUtils.wmsRestrictedComposers = staticmethod(QgsServerProjectUtils.wmsRestrictedComposers)
    QgsServerProjectUtils.wmsServiceUrl = staticmethod(QgsServerProjectUtils.wmsServiceUrl)
    QgsServerProjectUtils.wmsRootName = staticmethod(QgsServerProjectUtils.wmsRootName)
    QgsServerProjectUtils.wmsRestrictedLayers = staticmethod(QgsServerProjectUtils.wmsRestrictedLayers)
    QgsServerProjectUtils.wmsOutputCrsList = staticmethod(QgsServerProjectUtils.wmsOutputCrsList)
    QgsServerProjectUtils.wmsOutputCrsListAsOgcUrn = staticmethod(QgsServerProjectUtils.wmsOutputCrsListAsOgcUrn)
    QgsServerProjectUtils.wmsExtent = staticmethod(QgsServerProjectUtils.wmsExtent)
    QgsServerProjectUtils.wfsServiceUrl = staticmethod(QgsServerProjectUtils.wfsServiceUrl)
    QgsServerProjectUtils.wfsLayerIds = staticmethod(QgsServerProjectUtils.wfsLayerIds)
    QgsServerProjectUtils.wfsLayerPrecision = staticmethod(QgsServerProjectUtils.wfsLayerPrecision)
    QgsServerProjectUtils.wfstUpdateLayerIds = staticmethod(QgsServerProjectUtils.wfstUpdateLayerIds)
    QgsServerProjectUtils.wfstInsertLayerIds = staticmethod(QgsServerProjectUtils.wfstInsertLayerIds)
    QgsServerProjectUtils.wfstDeleteLayerIds = staticmethod(QgsServerProjectUtils.wfstDeleteLayerIds)
    QgsServerProjectUtils.wcsServiceUrl = staticmethod(QgsServerProjectUtils.wcsServiceUrl)
    QgsServerProjectUtils.wcsLayerIds = staticmethod(QgsServerProjectUtils.wcsLayerIds)
    QgsServerProjectUtils.wmtsServiceUrl = staticmethod(QgsServerProjectUtils.wmtsServiceUrl)
    QgsServerProjectUtils.serviceUrl = staticmethod(QgsServerProjectUtils.serviceUrl)
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/server/qgsserverquerystringparameter.h
# monkey patching scoped based enum
QgsServerQueryStringParameter.Type.String.__doc__ = "Parameter is a string"
QgsServerQueryStringParameter.Type.Integer.__doc__ = "Parameter is an integer"
QgsServerQueryStringParameter.Type.Double.__doc__ = "Parameter is a double"
QgsServerQueryStringParameter.Type.Boolean.__doc__ = "Parameter is a boolean"
QgsServerQueryStringParameter.Type.List.__doc__ = "Parameter is a (comma separated) list of strings, the handler will perform any further required conversion of the list values"
QgsServerQueryStringParameter.Type.__doc__ = """The Type enum represents the parameter type

* ``String``: Parameter is a string
* ``Integer``: Parameter is an integer
* ``Double``: Parameter is a double
* ``Boolean``: Parameter is a boolean
* ``List``: Parameter is a (comma separated) list of strings, the handler will perform any further required conversion of the list values

"""
# --
QgsServerQueryStringParameter.Type.baseClass = QgsServerQueryStringParameter
try:
    QgsServerQueryStringParameter.typeName = staticmethod(QgsServerQueryStringParameter.typeName)
    QgsServerQueryStringParameter.__virtual_methods__ = ['value']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/server/qgsserverrequest.h
QgsServerRequest.HeadMethod = QgsServerRequest.Method.HeadMethod
QgsServerRequest.PutMethod = QgsServerRequest.Method.PutMethod
QgsServerRequest.GetMethod = QgsServerRequest.Method.GetMethod
QgsServerRequest.PostMethod = QgsServerRequest.Method.PostMethod
QgsServerRequest.DeleteMethod = QgsServerRequest.Method.DeleteMethod
QgsServerRequest.PatchMethod = QgsServerRequest.Method.PatchMethod
QgsServerRequest.OptionsMethod = QgsServerRequest.Method.OptionsMethod
QgsServerRequest.Method.baseClass = QgsServerRequest
QgsServerRequest.HOST = QgsServerRequest.RequestHeader.HOST
QgsServerRequest.FORWARDED = QgsServerRequest.RequestHeader.FORWARDED
QgsServerRequest.X_FORWARDED_FOR = QgsServerRequest.RequestHeader.X_FORWARDED_FOR
QgsServerRequest.X_FORWARDED_HOST = QgsServerRequest.RequestHeader.X_FORWARDED_HOST
QgsServerRequest.X_FORWARDED_PROTO = QgsServerRequest.RequestHeader.X_FORWARDED_PROTO
QgsServerRequest.X_QGIS_SERVICE_URL = QgsServerRequest.RequestHeader.X_QGIS_SERVICE_URL
QgsServerRequest.X_QGIS_WMS_SERVICE_URL = QgsServerRequest.RequestHeader.X_QGIS_WMS_SERVICE_URL
QgsServerRequest.X_QGIS_WFS_SERVICE_URL = QgsServerRequest.RequestHeader.X_QGIS_WFS_SERVICE_URL
QgsServerRequest.X_QGIS_WCS_SERVICE_URL = QgsServerRequest.RequestHeader.X_QGIS_WCS_SERVICE_URL
QgsServerRequest.X_QGIS_WMTS_SERVICE_URL = QgsServerRequest.RequestHeader.X_QGIS_WMTS_SERVICE_URL
QgsServerRequest.ACCEPT = QgsServerRequest.RequestHeader.ACCEPT
QgsServerRequest.USER_AGENT = QgsServerRequest.RequestHeader.USER_AGENT
QgsServerRequest.AUTHORIZATION = QgsServerRequest.RequestHeader.AUTHORIZATION
QgsServerRequest.RequestHeader.baseClass = QgsServerRequest
try:
    QgsServerRequest.methodToString = staticmethod(QgsServerRequest.methodToString)
    QgsServerRequest.__virtual_methods__ = ['setParameter', 'removeParameter', 'header', 'data', 'setUrl']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/server/qgsserverresponse.h
try:
    QgsServerResponse.__virtual_methods__ = ['write', 'finish', 'flush', 'feedback']
    QgsServerResponse.__abstract_methods__ = ['setHeader', 'addHeader', 'removeHeader', 'header', 'fullHeader', 'headers', 'fullHeaders', 'headersSent', 'setStatusCode', 'statusCode', 'sendError', 'io', 'clear', 'data', 'truncate']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/server/qgsserversettings.h
QgsServerSettingsEnv.DEFAULT_VALUE = QgsServerSettingsEnv.Source.DEFAULT_VALUE
QgsServerSettingsEnv.ENVIRONMENT_VARIABLE = QgsServerSettingsEnv.Source.ENVIRONMENT_VARIABLE
QgsServerSettingsEnv.INI_FILE = QgsServerSettingsEnv.Source.INI_FILE
QgsServerSettingsEnv.Source.baseClass = QgsServerSettingsEnv
QgsServerSettingsEnv.QGIS_OPTIONS_PATH = QgsServerSettingsEnv.EnvVar.QGIS_OPTIONS_PATH
QgsServerSettingsEnv.QGIS_SERVER_PARALLEL_RENDERING = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_PARALLEL_RENDERING
QgsServerSettingsEnv.QGIS_SERVER_MAX_THREADS = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_MAX_THREADS
QgsServerSettingsEnv.QGIS_SERVER_LOG_LEVEL = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_LOG_LEVEL
QgsServerSettingsEnv.QGIS_SERVER_LOG_FILE = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_LOG_FILE
QgsServerSettingsEnv.QGIS_SERVER_LOG_STDERR = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_LOG_STDERR
QgsServerSettingsEnv.QGIS_PROJECT_FILE = QgsServerSettingsEnv.EnvVar.QGIS_PROJECT_FILE
QgsServerSettingsEnv.QGIS_SERVER_IGNORE_BAD_LAYERS = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_IGNORE_BAD_LAYERS
QgsServerSettingsEnv.QGIS_SERVER_IGNORE_RENDERING_ERRORS = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_IGNORE_RENDERING_ERRORS
QgsServerSettingsEnv.QGIS_SERVER_RETRY_BAD_LAYERS = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_RETRY_BAD_LAYERS
QgsServerSettingsEnv.QGIS_SERVER_CACHE_DIRECTORY = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_CACHE_DIRECTORY
QgsServerSettingsEnv.QGIS_SERVER_CACHE_SIZE = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_CACHE_SIZE
QgsServerSettingsEnv.QGIS_SERVER_SHOW_GROUP_SEPARATOR = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_SHOW_GROUP_SEPARATOR
QgsServerSettingsEnv.QGIS_SERVER_OVERRIDE_SYSTEM_LOCALE = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_OVERRIDE_SYSTEM_LOCALE
QgsServerSettingsEnv.QGIS_SERVER_WMS_MAX_HEIGHT = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_WMS_MAX_HEIGHT
QgsServerSettingsEnv.QGIS_SERVER_WMS_MAX_WIDTH = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_WMS_MAX_WIDTH
QgsServerSettingsEnv.QGIS_SERVER_API_RESOURCES_DIRECTORY = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_API_RESOURCES_DIRECTORY
QgsServerSettingsEnv.QGIS_SERVER_API_WFS3_MAX_LIMIT = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_API_WFS3_MAX_LIMIT
QgsServerSettingsEnv.QGIS_SERVER_API_WFS3_ROOT_PATH = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_API_WFS3_ROOT_PATH
QgsServerSettingsEnv.QGIS_SERVER_TRUST_LAYER_METADATA = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_TRUST_LAYER_METADATA
QgsServerSettingsEnv.QGIS_SERVER_FORCE_READONLY_LAYERS = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_FORCE_READONLY_LAYERS
QgsServerSettingsEnv.QGIS_SERVER_DISABLE_GETPRINT = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_DISABLE_GETPRINT
QgsServerSettingsEnv.QGIS_SERVER_LANDING_PAGE_PROJECTS_DIRECTORIES = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_LANDING_PAGE_PROJECTS_DIRECTORIES
QgsServerSettingsEnv.QGIS_SERVER_LANDING_PAGE_PROJECTS_PG_CONNECTIONS = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_LANDING_PAGE_PROJECTS_PG_CONNECTIONS
QgsServerSettingsEnv.QGIS_SERVER_LOG_PROFILE = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_LOG_PROFILE
QgsServerSettingsEnv.QGIS_SERVER_SERVICE_URL = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_SERVICE_URL
QgsServerSettingsEnv.QGIS_SERVER_WMS_SERVICE_URL = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_WMS_SERVICE_URL
QgsServerSettingsEnv.QGIS_SERVER_WFS_SERVICE_URL = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_WFS_SERVICE_URL
QgsServerSettingsEnv.QGIS_SERVER_WCS_SERVICE_URL = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_WCS_SERVICE_URL
QgsServerSettingsEnv.QGIS_SERVER_WMTS_SERVICE_URL = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_WMTS_SERVICE_URL
QgsServerSettingsEnv.QGIS_SERVER_LANDING_PAGE_PREFIX = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_LANDING_PAGE_PREFIX
QgsServerSettingsEnv.QGIS_SERVER_PROJECT_CACHE_CHECK_INTERVAL = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_PROJECT_CACHE_CHECK_INTERVAL
QgsServerSettingsEnv.QGIS_SERVER_PROJECT_CACHE_STRATEGY = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_PROJECT_CACHE_STRATEGY
QgsServerSettingsEnv.QGIS_SERVER_PROJECT_CACHE_SIZE = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_PROJECT_CACHE_SIZE
QgsServerSettingsEnv.QGIS_SERVER_ALLOWED_EXTRA_SQL_TOKENS = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_ALLOWED_EXTRA_SQL_TOKENS
QgsServerSettingsEnv.QGIS_SERVER_APPLICATION_NAME = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_APPLICATION_NAME
QgsServerSettingsEnv.QGIS_SERVER_CAPABILITIES_CACHE_SIZE = QgsServerSettingsEnv.EnvVar.QGIS_SERVER_CAPABILITIES_CACHE_SIZE
QgsServerSettingsEnv.EnvVar.baseClass = QgsServerSettingsEnv
try:
    QgsServerSettings.name = staticmethod(QgsServerSettings.name)
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/server/qgsserverstatichandler.h
try:
    QgsServerStaticHandler.__overridden_methods__ = ['handleRequest', 'path', 'operationId', 'summary', 'description', 'linkTitle', 'linkType']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/server/qgsservice.h
try:
    QgsService.__abstract_methods__ = ['name', 'version', 'executeRequest']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/server/qgsservicemodule.h
try:
    QgsServiceModule.__abstract_methods__ = ['registerSelf']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/server/qgsstorebadlayerinfo.h
try:
    QgsStoreBadLayerInfo.__overridden_methods__ = ['handleBadLayers']
except (NameError, AttributeError):
    pass

