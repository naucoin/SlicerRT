project(vtkSlicer${MODULE_NAME}ModuleLogic)

set(KIT ${PROJECT_NAME})

set(${KIT}_EXPORT_DIRECTIVE "VTK_SLICER_${MODULE_NAME_UPPER}_LOGIC_EXPORT")

set(${KIT}_INCLUDE_DIRECTORIES
  ${SlicerRtCommon_INCLUDE_DIRS}
  ${vtkSlicerSubjectHierarchyModuleLogic_INCLUDE_DIRS}
  ${vtkSlicerSegmentationsModuleMRML_INCLUDE_DIRS}
  ${vtkSlicerSegmentationsModuleLogic_INCLUDE_DIRS}
  )

set(${KIT}_SRCS
  vtkSlicer${MODULE_NAME}ModuleLogic.cxx
  vtkSlicer${MODULE_NAME}ModuleLogic.h
  vtkSlicerDoseVolumeHistogramComparisonLogic.cxx
  vtkSlicerDoseVolumeHistogramComparisonLogic.h
  )

set(${KIT}_TARGET_LIBRARIES
  vtkSlicerRtCommon
  vtkSlicerSegmentationsModuleMRML
  vtkSlicerSegmentationsModuleLogic
  vtkSlicerSubjectHierarchyModuleLogic
  vtkSlicer${MODULE_NAME}ModuleMRML
  ${ITK_LIBRARIES}
  )

SET (${KIT}_INCLUDE_DIRS ${CMAKE_CURRENT_SOURCE_DIR} ${CMAKE_CURRENT_BINARY_DIR} ${Slicer_Base_INCLUDE_DIRS} CACHE INTERNAL "" FORCE)

#-----------------------------------------------------------------------------
SlicerMacroBuildModuleLogic(
  NAME ${KIT}
  EXPORT_DIRECTIVE ${${KIT}_EXPORT_DIRECTIVE}
  INCLUDE_DIRECTORIES ${${KIT}_INCLUDE_DIRECTORIES}
  SRCS ${${KIT}_SRCS}
  TARGET_LIBRARIES ${${KIT}_TARGET_LIBRARIES}
  )
