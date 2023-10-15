# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2020 replay file
# Internal Version: 2019_09_13-20.49.31 163176
# Run by dsouza on Wed Jun 28 21:57:31 2023
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(1.11979, 1.1169), width=164.833, 
    height=110.796)
session.viewports['Viewport: 1'].makeCurrent()
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
execfile('odb_automation.py', __main__.__dict__)
#: The model database "D:\Git_projects\Abaqus_automation\Automation for reading odb files\Base_model.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: Model: D:/Git_projects/Abaqus_automation/Automation for reading odb files/model_0.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       3
#: Number of Node Sets:          5
#: Number of Steps:              1
#: The model database "D:\Git_projects\Abaqus_automation\Automation for reading odb files\Base_model.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: Model: D:/Git_projects/Abaqus_automation/Automation for reading odb files/model_1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       3
#: Number of Node Sets:          5
#: Number of Steps:              1
#: The model database "D:\Git_projects\Abaqus_automation\Automation for reading odb files\Base_model.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: Model: D:/Git_projects/Abaqus_automation/Automation for reading odb files/model_2.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       3
#: Number of Node Sets:          5
#: Number of Steps:              1
#: The model database "D:\Git_projects\Abaqus_automation\Automation for reading odb files\Base_model.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: Model: D:/Git_projects/Abaqus_automation/Automation for reading odb files/model_3.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       3
#: Number of Node Sets:          5
#: Number of Steps:              1
#: The model database "D:\Git_projects\Abaqus_automation\Automation for reading odb files\Base_model.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: Model: D:/Git_projects/Abaqus_automation/Automation for reading odb files/model_4.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       3
#: Number of Node Sets:          5
#: Number of Steps:              1
#: The model database "D:\Git_projects\Abaqus_automation\Automation for reading odb files\Base_model.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: Model: D:/Git_projects/Abaqus_automation/Automation for reading odb files/model_5.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       3
#: Number of Node Sets:          5
#: Number of Steps:              1
print 'RT script done'
#: RT script done
