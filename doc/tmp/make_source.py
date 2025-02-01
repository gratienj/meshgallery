#  written by Olivier Ricois (olivier.ricois@ifpen.fr)

import os
import sys
import glob
import pathlib

IFPEN_LOGO = "images/IFPENVF_quadri.jpg"

RST_DIR_NAME = "_axlrst"

inDir = "../../src/"
exDirs=["../../src/Modules/Geomechanical"]
outDir = "."



listAxlServiceFiles = [
    "axl_from_framework/IFPSolver.axl",
    "axl_from_framework/NewtonSolver.axl",
    "../../../ArcGeoPhy/src/ArcGeoPhy/Faults/FaultMng/StaticFaultMng.axl",
    "../../../ArcGeoPhy/src/ArcGeoPhy/PhysicalConstants/PhysicalConstantMng.axl",
    "../../../ArcGeoSim/src/ArcGeoSim/Mesh/Exporters/IXM4Writer.axl",
    "../../../ArcGeoSim/src/ArcGeoSim/Numerics/DiscreteOperator/DivKGradFaultSchemeImpl/DivKGradFaultScheme.axl",
    "../../../ArcGeoSim/src/ArcGeoSim/Time/TimeLine/TimeLine.axl",
    "../../../ArcGeoSim/src/ArcGeoSim/Numerics/GroupCreator/StandardGroupCreator.axl",
    "../../../ArcGeoSim/src/ArcGeoSim/Utils/CAWF/PreCICE.axl",
    "../../../ArcGeoSim/src/ArcGeoSim/Numerics/Expressions/UnsteadyRegularGridData/LinearInterpGridDataFunction/LinearInterpGridDataFunction.axl",
    "../../../ArcGeoSim/src/ArcGeoSim/Numerics/Expressions/UnsteadyRegularGridData/OnePointInterpGridDataFunction/OnePointInterpGridDataFunction.axl",
    "../../../ArcGeoSim/src/ArcGeoSim/Numerics/Expressions/ExpressionBuilder/ExpressionBuilderR4vR1.axl",
    "../../../ArcGeoSim/src/ArcGeoSim/Mesh/AccessorToolsMng/MeshAccessorToolsMng.axl"   ]

listAxlModulesFiles = [
    ]

listExcludedAxlServicesFiles = [
    "GraphAMRTest",
    "HeatLossTester",
    "MaterialBalanceTest",
    "Reacteur",
    "MeshCleanerTest",
    "PhysicalLawTester",
    "MeshMerge",
    "VFPTablesTest",
    "FluxEstimator",
    "PoroMechanicsModel",
    "UnitsTester",
    "ServiceSyntaxTester"
    ]
listExcludedAxlModulesFiles = [
    "AnalyticSolution",
    "Darcy",
    "GraphAMRTest",
    "MaterialBalanceTest",
    "MeshCleanerTest",
    "MeshMerge",
    "PoroElasticity",
    "Reacteur",
    "VFPTablesTest"    ]


TST_DIR_NAME = "../../test/Sphinx/"


def generateIndex(inDir, exDirs, outDir):    
    fileExt = r"**/*.axl"
    chemins_exclus = {os.path.abspath(extDir) for extDir in exDirs}
    for fileName in pathlib.Path(inDir).glob(fileExt) :
        for chemin in chemins_exclus:
            if (os.path.abspath(fileName).startswith(chemin)):
                break
            basename = os.path.basename(fileName)
            name = os.path.splitext(basename)[0]
            if (open(fileName, "r",encoding="ISO-8859-1").read().find("interface name")>0):
                if name not in listExcludedAxlServicesFiles: 
                    listAxlServiceFiles.append(fileName)  
            else:
                if name not in listExcludedAxlModulesFiles: 
                    listAxlModulesFiles.append(fileName)  
    
    # generate axlModules.rst
    outFile = open(pathlib.Path(outDir, "axlModules.rst"), "w")
    outFile.write(".. image:: %s\n" %IFPEN_LOGO)
    outFile.write("   :scale: 8 %\n")
    outFile.write("   :align: right\n\n")

    outFile.write(".. _axlModules:\n\n")
    outFile.write("List of available modules\n")
    outFile.write("=========================\n\n")
    outFile.write("An application based on the Arcane framework is composed of plugins or  **modules**. ")
    outFile.write("A module is a software component that models a specific physical context (thermodynamics, thermal,...). ")
    outFile.write("Each module within the  application is independent and manages:\n\n")
    outFile.write("  - Its **variables**: computational data such as temperature, pressure, velocity, over the domain of simulation and the timesteps. Variables are global in the application and are shared between the different modules.\n");
    outFile.write("  - Its **options** of configuration (xml input data).\n");
    outFile.write("  - Its **business objets** and **functionnalities** via configuration of services (:ref:`axlServices`).\n");
    outFile.write("  - Its **entry points**: the operations performed by the module during an iteration of the time loop.\n\n");
    outFile.write("The modules available in Fraxim are:\n\n")
    outFile.write(".. toctree::\n")
    outFile.write("   :maxdepth: 1\n\n")
    listRstFiles = []
    for axlfile in listAxlModulesFiles :
        basename = os.path.basename(axlfile)
        file_name = os.path.splitext(basename)[0]
        listRstFiles.append(pathlib.Path(RST_DIR_NAME,file_name))
    listRstFiles = sorted(listRstFiles)
    
    for rstfile in listRstFiles :
        outFile.write("   %s\n" % (rstfile))       
    outFile.close()
   
    # generate axlServices.rst
    outFile = open(pathlib.Path(outDir, "axlServices.rst"), "w")
    outFile.write(".. image:: %s\n" %IFPEN_LOGO)
    outFile.write("   :scale: 8 %\n")
    outFile.write("   :align: right\n\n")
    outFile.write(".. _axlServices:\n\n")
    outFile.write("List of available services\n")
    outFile.write("==========================\n\n")
    outFile.write("A service defines an option or a functionality of the application.\n")
    outFile.write("It is configured by the user with xml input data.\n")
    outFile.write("From a computer design perspective, a service implements an interface and several implementations may be available for a functionality in Fraxim.\n")
    outFile.write("The list of service interfaces is available in the :ref:`genindex` table.\n\n")
    outFile.write("The services available in Fraxim are:\n\n")
    outFile.write(".. toctree::\n")
    outFile.write("   :maxdepth: 1\n\n")
    listRstFiles = []
    for axlfile in listAxlServiceFiles :
        basename = os.path.basename(axlfile)
        file_name = os.path.splitext(basename)[0]
        listRstFiles.append(pathlib.Path(RST_DIR_NAME,file_name))
    listRstFiles = sorted(listRstFiles)
    
    for rstfile in listRstFiles :
        outFile.write("   %s\n" % (rstfile))
    outFile.close()
    
def generateRSTs(outDir, listAxlServiceFiles):
    # make directory
    path = pathlib.Path(outDir,RST_DIR_NAME)
    path.mkdir(parents=True, exist_ok=True)
    # title
    for axlfile in listAxlServiceFiles :
        axldir = os.path.dirname(axlfile)
        basename = os.path.basename(axlfile)
        file_name = os.path.splitext(basename)[0]
        rstFile = open(pathlib.Path(path,file_name+".rst"),"w")
        rstFile.write(".. image:: %s\n" %pathlib.Path("..",IFPEN_LOGO))
        rstFile.write("   :scale: 8 %\n")
        rstFile.write("   :align: right\n\n")
        rstFile.write(".. _%s:\n\n" %file_name)
        rstFile.write(":index:`%s`\n" %file_name)
        rstFile.write("=========================================================\n\n")
        rstFile.write(".. datatemplate:xml:: %s\n" % pathlib.Path("..",axlfile))
        rstFile.write("   :template: axl.tmpl\n")
        
        # add example data file if any in TST_DIR_NAME
        axlarc = pathlib.Path(TST_DIR_NAME,file_name+".arc")
        if (os.path.exists(axlarc)):
            rstFile.write("\n")
            rstFile.write("\n.. _%s_data:\n\n" %file_name)
            rstFile.write("Example of data file\n")
            rstFile.write("~~~~~~~~~~~~~~~~~~~~\n\n")
            rstFile.write(".. literalinclude:: %s\n" % pathlib.Path("..",axlarc))
            rstFile.write("   :language: xml\n")
            rstFile.write("   :lines: 12-%s\n" % (len(open(axlarc, "r",encoding="ISO-8859-1").readlines())-2))
        rstFile.close()
            

###################
generateIndex(inDir, exDirs, outDir)
generateRSTs(outDir, listAxlServiceFiles)
generateRSTs(outDir, listAxlModulesFiles)