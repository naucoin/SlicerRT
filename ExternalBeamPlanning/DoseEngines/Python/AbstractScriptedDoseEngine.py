import os
import vtk, qt, ctk, slicer, logging

#
# Abstract class of python scripted dose engines
#

class AbstractScriptedDoseEngine():
  #TODO:
  """ Abstract scripted dose engines implemented in python

      USAGE:
      1. Instantiation and registration
        Instantiate segment editor effect adaptor class from
        module (e.g. from setup function), and set python source:
        > import qSlicerExternalBeamPlanningDoseEnginesPythonQt as engines
        > scriptedEngine = engines.qSlicerScriptedDoseEngine(None)
        > scriptedEngine.setPythonSource(MyEffect.filePath)
        > scriptedEffect.self().register()
        If engine name is added to slicer.modules.doseenginenames
        list then the above instantiation and registration steps are not necessary,
        as the ExternalBeamPlanning module do all these.

      2. Call host C++ implementation using
        > self.scriptedEngine.functionName()

      2.a. Most frequently used such methods are:
        Parameter get/set: parameter, integerParameter, doubleParameter, setParameter
        Add beam parameters: addBeamParameterSpinBox, addBeamParameterSlider, addBeamParameterComboBox, addBeamParameterCheckBox

      2.b. Always call API functions (the ones that are defined in the adaptor
        class qSlicerScriptedDoseEngine) using the adaptor accessor:
        > self.scriptedEffect.addResultDose()

      An example for a generic effect is the MockPythonDoseEngine

  """

  def __init__(self, scriptedEngine):
    self.scriptedEngine = scriptedEngine

  def register(self):
    import qSlicerExternalBeamPlanningDoseEnginesPythonQt
    #TODO: For some reason the instance() function cannot be called as a class function although it's static
    handler = qSlicerExternalBeamPlanningDoseEnginesPythonQt.qSlicerDoseEnginePluginHandler()
    engineHandlerSingleton = handler.instance()
    engineHandlerSingleton.registerDoseEngine(self.scriptedEngine)
