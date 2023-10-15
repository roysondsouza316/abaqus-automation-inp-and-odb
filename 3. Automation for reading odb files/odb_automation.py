import os
from abaqus import *
from abaqusConstants import *
from caeModules import *

os.chdir('D:/Git_projects/Abaqus_automation/Automation for reading odb files/')

# Define the range of models you want to process
start_model = 0
end_model = 5

# Loop through the range of model numbers
for i in range(start_model, end_model + 1):
    # Create the analysis name and ODB file path based on the model number
    AnalysisName = 'model_{}'.format(i)
    odb_path = '{}.odb'.format(AnalysisName)

    # Open the main Abaqus CAE database file and the ODB file for the current model
    openMdb('Base_model.cae')
    o3 = session.openOdb(name=odb_path)

    # Define the step and model variables for later use
    stpvar = 'Step-1'
    mdlvar = 'Model-1'

    # Get a reference to the opened ODB file
    openodb = session.odbs[odb_path]
    # Find the last frame in the specified step of the analysis
    LastFrame = openodb.steps[stpvar].frames[-1].frameValue

    # Get the displacement data from the ODB file. In'Node PART-1-1.44', It extracts the 
    # data of node 44 from the region PART-1.1.
    Disp_U2 = openodb.steps[stpvar].historyRegions['Node PART-1-1.44']
    dataDisp_U2 = Disp_U2.historyOutputs['U2'].data

    # Define the assembly variable and get the internal energy and strain energy data
    set_tot = 'Assembly ASSEMBLY'
    dataALLIE = openodb.steps[stpvar].historyRegions[set_tot].historyOutputs['ALLIE'].data
    dataALLSE = openodb.steps[stpvar].historyRegions[set_tot].historyOutputs['ALLSE'].data

    # Create XYData objects for each of the data sets
    U2_dispData = session.XYData(name='datadisp', data=dataDisp_U2)
    ALLIE_xyData = session.XYData(name='dataALLIE', data=dataALLIE)
    ALLSE_xyData = session.XYData(name='dataALLSE', data=dataALLSE)

    # Write the XYData objects to text files
    session.writeXYReport(fileName="{}_disp_U2.txt".format(AnalysisName), xyData=(U2_dispData,))
    session.writeXYReport(fileName="{}_ALLIE.txt".format(AnalysisName), xyData=(ALLIE_xyData,))
    session.writeXYReport(fileName="{}_ALLSE.txt".format(AnalysisName), xyData=(ALLSE_xyData,))

    # Close the ODB to avoid memory issues
    session.odbs[odb_path].close()
