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
    QgsAccessControl.__overridden_methods__ = ['filterFeatures', 'clone', 'layerAttributes']
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
    QgsBufferServerResponse.__overridden_methods__ = ['setHeader', 'removeHeader', 'header', 'headers', 'headersSent', 'setStatusCode', 'statusCode', 'sendError', 'io', 'finish', 'flush', 'clear', 'data', 'truncate']
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
    QgsFeatureFilter.__overridden_methods__ = ['filterFeatures', 'layerAttributes', 'clone']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/server/qgsfeaturefilterprovidergroup.h
try:
    QgsFeatureFilterProviderGroup.__overridden_methods__ = ['filterFeatures', 'layerAttributes', 'clone']
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
QgsServerOgcApi.Rel.baseClass = QgsServerOgcApi
QgsServerOgcApi.ContentType.baseClass = QgsServerOgcApi
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
QgsServerRequest.Method.baseClass = QgsServerRequest
QgsServerRequest.RequestHeader.baseClass = QgsServerRequest
try:
    QgsServerRequest.methodToString = staticmethod(QgsServerRequest.methodToString)
    QgsServerRequest.__virtual_methods__ = ['setParameter', 'removeParameter', 'header', 'data', 'setUrl']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/server/qgsserverresponse.h
try:
    QgsServerResponse.__virtual_methods__ = ['write', 'SIP_VIRTUALERRORHANDLER', 'feedback']
    QgsServerResponse.__abstract_methods__ = ['setHeader', 'removeHeader', 'header', 'headers', 'headersSent', 'setStatusCode', 'statusCode', 'sendError', 'io', 'clear', 'data', 'truncate']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/server/qgsserversettings.h
QgsServerSettingsEnv.Source.baseClass = QgsServerSettingsEnv
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

