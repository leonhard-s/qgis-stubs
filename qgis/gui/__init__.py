# -*- coding: utf-8 -*-

"""
***************************************************************************
    __init__.py
    ---------------------
    Date                 : May 2014
    Copyright            : (C) 2014 by Nathan Woodrow
    Email                : woodrow dot nathan at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Nathan Woodrow'
__date__ = 'May 2014'
__copyright__ = '(C) 2014, Nathan Woodrow'

from qgis.PyQt import QtCore
from qgis._gui import *
"""
This folder is completed using sipify.pl script
It is not aimed to be manually edited
"""
# The following has been generated automatically from src/gui/qgsadvanceddigitizingdockwidget.h
QgsAdvancedDigitizingDockWidget.CadCapacities.baseClass = QgsAdvancedDigitizingDockWidget
CadCapacities = QgsAdvancedDigitizingDockWidget  # dirty hack since SIP seems to introduce the flags in module
# monkey patching scoped based enum
QgsAdvancedDigitizingDockWidget.NoConstraint = QgsAdvancedDigitizingDockWidget.AdditionalConstraint.NoConstraint
QgsAdvancedDigitizingDockWidget.NoConstraint.is_monkey_patched = True
QgsAdvancedDigitizingDockWidget.AdditionalConstraint.NoConstraint.__doc__ = "No additional constraint"
QgsAdvancedDigitizingDockWidget.Perpendicular = QgsAdvancedDigitizingDockWidget.AdditionalConstraint.Perpendicular
QgsAdvancedDigitizingDockWidget.Perpendicular.is_monkey_patched = True
QgsAdvancedDigitizingDockWidget.AdditionalConstraint.Perpendicular.__doc__ = "Perpendicular"
QgsAdvancedDigitizingDockWidget.Parallel = QgsAdvancedDigitizingDockWidget.AdditionalConstraint.Parallel
QgsAdvancedDigitizingDockWidget.Parallel.is_monkey_patched = True
QgsAdvancedDigitizingDockWidget.AdditionalConstraint.Parallel.__doc__ = "Parallel"
QgsAdvancedDigitizingDockWidget.AdditionalConstraint.__doc__ = 'Additional constraints which can be enabled\n\n' + '* ``NoConstraint``: ' + QgsAdvancedDigitizingDockWidget.AdditionalConstraint.NoConstraint.__doc__ + '\n' + '* ``Perpendicular``: ' + QgsAdvancedDigitizingDockWidget.AdditionalConstraint.Perpendicular.__doc__ + '\n' + '* ``Parallel``: ' + QgsAdvancedDigitizingDockWidget.AdditionalConstraint.Parallel.__doc__
# --
# The following has been generated automatically from src/gui/qgsattributeeditorcontext.h
QgsAttributeEditorContext.Mode.baseClass = QgsAttributeEditorContext
# The following has been generated automatically from src/gui/attributetable/qgsattributetablefiltermodel.h
QgsAttributeTableFilterModel.FilterMode.baseClass = QgsAttributeTableFilterModel
QgsAttributeTableFilterModel.ColumnType.baseClass = QgsAttributeTableFilterModel
# The following has been generated automatically from src/gui/auth/qgsauthsettingswidget.h
QgsAuthSettingsWidget.WarningType.baseClass = QgsAuthSettingsWidget
# The following has been generated automatically from src/gui/codeeditors/qgscodeeditorcolorscheme.h
# monkey patching scoped based enum
QgsCodeEditorColorScheme.ColorRole.Default.__doc__ = "Default text color"
QgsCodeEditorColorScheme.ColorRole.Keyword.__doc__ = "Keyword color"
QgsCodeEditorColorScheme.ColorRole.Class.__doc__ = "Class color"
QgsCodeEditorColorScheme.ColorRole.Method.__doc__ = "Method color"
QgsCodeEditorColorScheme.ColorRole.Decoration.__doc__ = "Decoration color"
QgsCodeEditorColorScheme.ColorRole.Number.__doc__ = "Number color"
QgsCodeEditorColorScheme.ColorRole.Comment.__doc__ = "Comment color"
QgsCodeEditorColorScheme.ColorRole.CommentLine.__doc__ = "Line comment color"
QgsCodeEditorColorScheme.ColorRole.CommentBlock.__doc__ = "Comment block color"
QgsCodeEditorColorScheme.ColorRole.Background.__doc__ = "Background color"
QgsCodeEditorColorScheme.ColorRole.Cursor.__doc__ = "Cursor color"
QgsCodeEditorColorScheme.ColorRole.CaretLine.__doc__ = "Caret line color"
QgsCodeEditorColorScheme.ColorRole.SingleQuote.__doc__ = "Single quote color"
QgsCodeEditorColorScheme.ColorRole.DoubleQuote.__doc__ = "Double quote color"
QgsCodeEditorColorScheme.ColorRole.TripleSingleQuote.__doc__ = "Triple single quote color"
QgsCodeEditorColorScheme.ColorRole.TripleDoubleQuote.__doc__ = "Triple double quote color"
QgsCodeEditorColorScheme.ColorRole.Operator.__doc__ = "Operator color"
QgsCodeEditorColorScheme.ColorRole.QuotedOperator.__doc__ = "Quoted operator color"
QgsCodeEditorColorScheme.ColorRole.Identifier.__doc__ = "Identifier color"
QgsCodeEditorColorScheme.ColorRole.QuotedIdentifier.__doc__ = "Quoted identifier color"
QgsCodeEditorColorScheme.ColorRole.Tag.__doc__ = "Tag color"
QgsCodeEditorColorScheme.ColorRole.UnknownTag.__doc__ = "Unknown tag"
QgsCodeEditorColorScheme.ColorRole.MarginBackground.__doc__ = "Margin background color"
QgsCodeEditorColorScheme.ColorRole.MarginForeground.__doc__ = "Margin foreground color"
QgsCodeEditorColorScheme.ColorRole.SelectionBackground.__doc__ = "Selection background color"
QgsCodeEditorColorScheme.ColorRole.SelectionForeground.__doc__ = "Selection foreground color"
QgsCodeEditorColorScheme.ColorRole.MatchedBraceBackground.__doc__ = "Matched brace background color"
QgsCodeEditorColorScheme.ColorRole.MatchedBraceForeground.__doc__ = "Matched brace foreground color"
QgsCodeEditorColorScheme.ColorRole.Edge.__doc__ = "Edge color"
QgsCodeEditorColorScheme.ColorRole.Fold.__doc__ = "Fold color"
QgsCodeEditorColorScheme.ColorRole.Error.__doc__ = "Error color"
QgsCodeEditorColorScheme.ColorRole.ErrorBackground.__doc__ = "Error background color"
QgsCodeEditorColorScheme.ColorRole.FoldIconForeground.__doc__ = "Fold icon foreground color"
QgsCodeEditorColorScheme.ColorRole.FoldIconHalo.__doc__ = "Fold icon halo color"
QgsCodeEditorColorScheme.ColorRole.IndentationGuide.__doc__ = "Indentation guide line"
QgsCodeEditorColorScheme.ColorRole.__doc__ = 'Color roles.\n\n' + '* ``Default``: ' + QgsCodeEditorColorScheme.ColorRole.Default.__doc__ + '\n' + '* ``Keyword``: ' + QgsCodeEditorColorScheme.ColorRole.Keyword.__doc__ + '\n' + '* ``Class``: ' + QgsCodeEditorColorScheme.ColorRole.Class.__doc__ + '\n' + '* ``Method``: ' + QgsCodeEditorColorScheme.ColorRole.Method.__doc__ + '\n' + '* ``Decoration``: ' + QgsCodeEditorColorScheme.ColorRole.Decoration.__doc__ + '\n' + '* ``Number``: ' + QgsCodeEditorColorScheme.ColorRole.Number.__doc__ + '\n' + '* ``Comment``: ' + QgsCodeEditorColorScheme.ColorRole.Comment.__doc__ + '\n' + '* ``CommentLine``: ' + QgsCodeEditorColorScheme.ColorRole.CommentLine.__doc__ + '\n' + '* ``CommentBlock``: ' + QgsCodeEditorColorScheme.ColorRole.CommentBlock.__doc__ + '\n' + '* ``Background``: ' + QgsCodeEditorColorScheme.ColorRole.Background.__doc__ + '\n' + '* ``Cursor``: ' + QgsCodeEditorColorScheme.ColorRole.Cursor.__doc__ + '\n' + '* ``CaretLine``: ' + QgsCodeEditorColorScheme.ColorRole.CaretLine.__doc__ + '\n' + '* ``SingleQuote``: ' + QgsCodeEditorColorScheme.ColorRole.SingleQuote.__doc__ + '\n' + '* ``DoubleQuote``: ' + QgsCodeEditorColorScheme.ColorRole.DoubleQuote.__doc__ + '\n' + '* ``TripleSingleQuote``: ' + QgsCodeEditorColorScheme.ColorRole.TripleSingleQuote.__doc__ + '\n' + '* ``TripleDoubleQuote``: ' + QgsCodeEditorColorScheme.ColorRole.TripleDoubleQuote.__doc__ + '\n' + '* ``Operator``: ' + QgsCodeEditorColorScheme.ColorRole.Operator.__doc__ + '\n' + '* ``QuotedOperator``: ' + QgsCodeEditorColorScheme.ColorRole.QuotedOperator.__doc__ + '\n' + '* ``Identifier``: ' + QgsCodeEditorColorScheme.ColorRole.Identifier.__doc__ + '\n' + '* ``QuotedIdentifier``: ' + QgsCodeEditorColorScheme.ColorRole.QuotedIdentifier.__doc__ + '\n' + '* ``Tag``: ' + QgsCodeEditorColorScheme.ColorRole.Tag.__doc__ + '\n' + '* ``UnknownTag``: ' + QgsCodeEditorColorScheme.ColorRole.UnknownTag.__doc__ + '\n' + '* ``MarginBackground``: ' + QgsCodeEditorColorScheme.ColorRole.MarginBackground.__doc__ + '\n' + '* ``MarginForeground``: ' + QgsCodeEditorColorScheme.ColorRole.MarginForeground.__doc__ + '\n' + '* ``SelectionBackground``: ' + QgsCodeEditorColorScheme.ColorRole.SelectionBackground.__doc__ + '\n' + '* ``SelectionForeground``: ' + QgsCodeEditorColorScheme.ColorRole.SelectionForeground.__doc__ + '\n' + '* ``MatchedBraceBackground``: ' + QgsCodeEditorColorScheme.ColorRole.MatchedBraceBackground.__doc__ + '\n' + '* ``MatchedBraceForeground``: ' + QgsCodeEditorColorScheme.ColorRole.MatchedBraceForeground.__doc__ + '\n' + '* ``Edge``: ' + QgsCodeEditorColorScheme.ColorRole.Edge.__doc__ + '\n' + '* ``Fold``: ' + QgsCodeEditorColorScheme.ColorRole.Fold.__doc__ + '\n' + '* ``Error``: ' + QgsCodeEditorColorScheme.ColorRole.Error.__doc__ + '\n' + '* ``ErrorBackground``: ' + QgsCodeEditorColorScheme.ColorRole.ErrorBackground.__doc__ + '\n' + '* ``FoldIconForeground``: ' + QgsCodeEditorColorScheme.ColorRole.FoldIconForeground.__doc__ + '\n' + '* ``FoldIconHalo``: ' + QgsCodeEditorColorScheme.ColorRole.FoldIconHalo.__doc__ + '\n' + '* ``IndentationGuide``: ' + QgsCodeEditorColorScheme.ColorRole.IndentationGuide.__doc__
# --
# The following has been generated automatically from src/gui/qgscolorbutton.h
QgsColorButton.Behavior.baseClass = QgsColorButton
# The following has been generated automatically from src/gui/qgscolorwidgets.h
QgsColorTextWidget.ColorTextFormat.baseClass = QgsColorTextWidget
# The following has been generated automatically from src/gui/attributetable/qgsdualview.h
QgsDualView.ViewMode.baseClass = QgsDualView
QgsDualView.FeatureListBrowsingAction.baseClass = QgsDualView
# The following has been generated automatically from src/gui/qgsexpressionbuilderwidget.h
QgsExpressionBuilderWidget.Flag.baseClass = QgsExpressionBuilderWidget
Flag = QgsExpressionBuilderWidget  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/gui/qgsfieldmappingmodel.h
# monkey patching scoped based enum
QgsFieldMappingModel.ColumnDataIndex.SourceExpression.__doc__ = "Expression"
QgsFieldMappingModel.ColumnDataIndex.DestinationName.__doc__ = "Destination field name"
QgsFieldMappingModel.ColumnDataIndex.DestinationType.__doc__ = "Destination field QVariant::Type casted to (int)"
QgsFieldMappingModel.ColumnDataIndex.DestinationLength.__doc__ = "Destination field length"
QgsFieldMappingModel.ColumnDataIndex.DestinationPrecision.__doc__ = "Destination field precision"
QgsFieldMappingModel.ColumnDataIndex.DestinationConstraints.__doc__ = "Destination field constraints"
QgsFieldMappingModel.ColumnDataIndex.__doc__ = 'The ColumnDataIndex enum represents the column index for the view\n\n' + '* ``SourceExpression``: ' + QgsFieldMappingModel.ColumnDataIndex.SourceExpression.__doc__ + '\n' + '* ``DestinationName``: ' + QgsFieldMappingModel.ColumnDataIndex.DestinationName.__doc__ + '\n' + '* ``DestinationType``: ' + QgsFieldMappingModel.ColumnDataIndex.DestinationType.__doc__ + '\n' + '* ``DestinationLength``: ' + QgsFieldMappingModel.ColumnDataIndex.DestinationLength.__doc__ + '\n' + '* ``DestinationPrecision``: ' + QgsFieldMappingModel.ColumnDataIndex.DestinationPrecision.__doc__ + '\n' + '* ``DestinationConstraints``: ' + QgsFieldMappingModel.ColumnDataIndex.DestinationConstraints.__doc__
# --
QgsFieldMappingModel.ColumnDataIndex.baseClass = QgsFieldMappingModel
# The following has been generated automatically from src/gui/qgsfilewidget.h
QgsFileWidget.StorageMode.baseClass = QgsFileWidget
QgsFileWidget.RelativeStorage.baseClass = QgsFileWidget
# The following has been generated automatically from src/gui/qgsfilterlineedit.h
QgsFilterLineEdit.ClearMode.baseClass = QgsFilterLineEdit
# The following has been generated automatically from src/gui/qgsfloatingwidget.h
QgsFloatingWidget.AnchorPoint.baseClass = QgsFloatingWidget
# The following has been generated automatically from src/gui/qgsfontbutton.h
QgsFontButton.Mode.baseClass = QgsFontButton
# The following has been generated automatically from src/gui/qgsgui.h
QgsGui.ProjectCrsBehavior.baseClass = QgsGui
# The following has been generated automatically from src/gui/editorwidgets/qgsjsoneditwidget.h
# monkey patching scoped based enum
QgsJsonEditWidget.View.Text.__doc__ = "JSON data displayed as text."
QgsJsonEditWidget.View.Tree.__doc__ = "JSON data displayed as tree. Tree view is disabled for invalid JSON data."
QgsJsonEditWidget.View.__doc__ = 'View mode, text or tree.\n\n' + '* ``Text``: ' + QgsJsonEditWidget.View.Text.__doc__ + '\n' + '* ``Tree``: ' + QgsJsonEditWidget.View.Tree.__doc__
# --
# monkey patching scoped based enum
QgsJsonEditWidget.FormatJson.Indented.__doc__ = "JSON data formatted with regular indentation"
QgsJsonEditWidget.FormatJson.Compact.__doc__ = "JSON data formatted as a compact one line string"
QgsJsonEditWidget.FormatJson.Disabled.__doc__ = "JSON data is not formatted"
QgsJsonEditWidget.FormatJson.__doc__ = 'Format mode in the text view\n\n' + '* ``Indented``: ' + QgsJsonEditWidget.FormatJson.Indented.__doc__ + '\n' + '* ``Compact``: ' + QgsJsonEditWidget.FormatJson.Compact.__doc__ + '\n' + '* ``Disabled``: ' + QgsJsonEditWidget.FormatJson.Disabled.__doc__
# --
# The following has been generated automatically from src/gui/qgsmapcanvasinteractionblocker.h
# monkey patching scoped based enum
QgsMapCanvasInteractionBlocker.Interaction.MapPanOnSingleClick.__doc__ = "A map pan interaction caused by a single click and release on the map canvas"
QgsMapCanvasInteractionBlocker.Interaction.__doc__ = 'Available interactions to block.\n\n' + '* ``MapPanOnSingleClick``: ' + QgsMapCanvasInteractionBlocker.Interaction.MapPanOnSingleClick.__doc__
# --
# The following has been generated automatically from src/gui/qgsmaplayeractionregistry.h
QgsMapLayerAction.Targets.baseClass = QgsMapLayerAction
Targets = QgsMapLayerAction  # dirty hack since SIP seems to introduce the flags in module
QgsMapLayerAction.Flags.baseClass = QgsMapLayerAction
Flags = QgsMapLayerAction  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/gui/qgsmaplayerconfigwidgetfactory.h
# monkey patching scoped based enum
QgsMapLayerConfigWidgetFactory.ParentPage.NoParent.__doc__ = "Factory creates pages itself, not sub-components"
QgsMapLayerConfigWidgetFactory.ParentPage.Temporal.__doc__ = "Factory creates sub-components of the temporal properties page (only supported for raster layer temporal properties)"
QgsMapLayerConfigWidgetFactory.ParentPage.__doc__ = 'Available parent pages, for factories which create a widget which is a sub-component\nof a standard page.\n\n.. versionadded:: 3.20\n\n' + '* ``NoParent``: ' + QgsMapLayerConfigWidgetFactory.ParentPage.NoParent.__doc__ + '\n' + '* ``Temporal``: ' + QgsMapLayerConfigWidgetFactory.ParentPage.Temporal.__doc__
# --
# The following has been generated automatically from src/gui/qgsmaptoolidentify.h
QgsMapToolIdentify.IdentifyMode.baseClass = QgsMapToolIdentify
QgsMapToolIdentify.LayerType.baseClass = QgsMapToolIdentify
LayerType = QgsMapToolIdentify  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/gui/processing/qgsprocessingaggregatewidgets.h
# monkey patching scoped based enum
QgsAggregateMappingModel.ColumnDataIndex.SourceExpression.__doc__ = "Expression"
QgsAggregateMappingModel.ColumnDataIndex.Aggregate.__doc__ = "Aggregate name"
QgsAggregateMappingModel.ColumnDataIndex.Delimiter.__doc__ = "Delimiter"
QgsAggregateMappingModel.ColumnDataIndex.DestinationName.__doc__ = "Destination field name"
QgsAggregateMappingModel.ColumnDataIndex.DestinationType.__doc__ = "Destination field QVariant::Type casted to (int)"
QgsAggregateMappingModel.ColumnDataIndex.DestinationLength.__doc__ = "Destination field length"
QgsAggregateMappingModel.ColumnDataIndex.DestinationPrecision.__doc__ = "Destination field precision"
QgsAggregateMappingModel.ColumnDataIndex.__doc__ = 'The ColumnDataIndex enum represents the column index for the view\n\n' + '* ``SourceExpression``: ' + QgsAggregateMappingModel.ColumnDataIndex.SourceExpression.__doc__ + '\n' + '* ``Aggregate``: ' + QgsAggregateMappingModel.ColumnDataIndex.Aggregate.__doc__ + '\n' + '* ``Delimiter``: ' + QgsAggregateMappingModel.ColumnDataIndex.Delimiter.__doc__ + '\n' + '* ``DestinationName``: ' + QgsAggregateMappingModel.ColumnDataIndex.DestinationName.__doc__ + '\n' + '* ``DestinationType``: ' + QgsAggregateMappingModel.ColumnDataIndex.DestinationType.__doc__ + '\n' + '* ``DestinationLength``: ' + QgsAggregateMappingModel.ColumnDataIndex.DestinationLength.__doc__ + '\n' + '* ``DestinationPrecision``: ' + QgsAggregateMappingModel.ColumnDataIndex.DestinationPrecision.__doc__
# --
QgsAggregateMappingModel.ColumnDataIndex.baseClass = QgsAggregateMappingModel
# The following has been generated automatically from src/gui/processing/qgsprocessingtoolboxmodel.h
QgsProcessingToolboxProxyModel.Filters.baseClass = QgsProcessingToolboxProxyModel
Filters = QgsProcessingToolboxProxyModel  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/gui/qgsrelationeditorwidget.h
QgsRelationEditorWidget.Button.baseClass = QgsRelationEditorWidget
QgsRelationEditorWidget.Buttons.baseClass = QgsRelationEditorWidget
Buttons = QgsRelationEditorWidget  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/gui/qgssublayersdialog.h
QgsSublayersDialog.PromptMode.baseClass = QgsSublayersDialog
