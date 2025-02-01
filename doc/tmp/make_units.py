#  written by Olivier Ricois (olivier.ricois@ifpen.fr)

import os
import sys
import glob
import pathlib
import re

IFPEN_LOGO = "images/IFPENVF_quadri.jpg"
RST_DIR_NAME = "_unitrst"

UNIT_FILES = [
    ("../../../ArcGeoSim/src/ArcGeoSim/Physics/Units/PFUUnitsSystem.cc","Field"),
    ("../../../ArcGeoSim/src/ArcGeoSim/Physics/Units/PMUUnitsSystem.cc","Metric"),
    ("../../../ArcGeoSim/src/ArcGeoSim/Physics/Units/PAUUnitsSystem.cc","AM")
    ]

UNITS_NAMES = [
    ("Adim","Adim"),
    ("Time","s"),
    ("X","m"),
    ("Y","m"),
    ("Z","m"),
    ("Angle","rad"),
    ("Surface","m2"),
    ("Height","m"),
    ("Volume","m3"),
    ("GasVolume","m3"),
    ("GasVolumeFactor","vol/vol"),
    ("Pressure","Pa"),
    ("CapillaryPressure","Pa"),
    ("Constraint","N/m2"),
    ("Temperature","K"),
    ("InvTemperature","1/K"),
    ("ThermalGradient","K/m"),
    ("Transmissivity","m3"),
    ("Porosity","Adim"),
    ("PorousVolume","m3"),
    ("Permeability","m2"),
    ("Dispersion","m2"),
    ("Diffusion","m2/s"),
    ("Flow","u.s-1"),
    ("MassFlow","Kg/s"),
    ("LiqVolFlow","m3/s"),
    ("GasVolFlow","m3/s"),
    ("Density","Kg/m3"),
    ("Viscosity","Pa.s"),
    ("Compressibility","1/Pa"),
    ("Weight","Kg"),
    ("Mass","Kg"),
    ("MolarMass","Kg/mol"),
    ("MassDensity","Kg/m3"),
    ("MolarVol","m3/mol"),
    ("Concentration","mol/m3"),
    ("Solubility","mol/Kg"),
    ("Salinity","g/l"),
    ("Production","Kg"),
    ("MassProduction","Kg"),
    ("Rs","m3/m3"),
    ("GasOilVolumeRatio","m3/m3"),
    ("Radius","m"),
    ("Energy","J"),
    ("HeatMassCapacity","J/(Kg.K)"),
    ("HeatMassCapacityT","J/(Kg.K2)"),
    ("HeatVolCapacity","J/(m3.K)"),
    ("HeatVolCapacityT","J/(m3.K2)"),
    ("ThermalConductivity","W/(m.K)"),
    ("ThermalDiffusivity","m2/s"),
    ("ProductivityIndex","Pa.s.m3/s/Pa"),
    ("HeatRate","J/s"),
    ("SpecificEnergy","J/Kg"),
    ("SteamRate","dm3/s(cwe)"),
    ("SteamVolume","dm3(cwe)"),
    ("MassicVolume","m3/kg"),
    ("Stiffness","N/m3"),
    ("HeatFluxDensity","W/m2"),
    ("RainFall","m3/m2/s")
     ]
UNITS_NAMES = sorted(UNITS_NAMES)

def generateIndex(outDir):
    # generate UnitSystems.rst
    outFile = open(pathlib.Path(outDir, "UnitSystems.rst"), "w")
    outFile.write(".. image:: %s\n" %IFPEN_LOGO)
    outFile.write("   :scale: 8 %\n")
    outFile.write("   :align: right\n\n")
    outFile.write("List of available unit systems\n")
    outFile.write("==============================\n\n")
    outFile.write(".. toctree::\n")
    outFile.write("   :maxdepth: 1\n\n")
    listRstFiles = []
    for file,name in UNIT_FILES :
        basename = os.path.basename(file)
        file_name = os.path.splitext(basename)[0]
        listRstFiles.append(pathlib.Path(RST_DIR_NAME,file_name))
    listRstFiles = sorted(listRstFiles)
    
    for rstfile in listRstFiles :
        outFile.write("   %s\n" % (rstfile))       
    outFile.close()
        


def generateUnitSystemFiles(outDir):
    # make directory
    path = pathlib.Path(outDir,RST_DIR_NAME)
    path.mkdir(parents=True, exist_ok=True)
    
    for file,name in UNIT_FILES :
        basename = os.path.basename(file)
        file_name = os.path.splitext(basename)[0]
        
        rstFile = open(pathlib.Path(path,file_name+".rst"),"w")
        rstFile.write(".. _%s:\n\n" %file_name)
        rstFile.write("%s\n" %file_name)
        rstFile.write("==========================\n\n")
        rstFile.write("This is the **%s** unit system." %name)
        rstFile.write("The units and conversion factors to the SI unit system for each data quantity are shown below.\n\n")
        rstFile.write(".. list-table:: table of the units and conversions\n")
        rstFile.write("   :header-rows: 1\n")
        rstFile.write("   :align: left\n\n")
        rstFile.write("   * - Quantity\n")
        rstFile.write("     - Name\n")
        rstFile.write("     - Mult\n")
        rstFile.write("     - Const\n")
        
         # read source
        mult = {}
        add = {}
        sname = {}
        for name,short in UNITS_NAMES:
            mult[name]=repr("1")
            add[name]=repr("0")
            sname[name]=short
            
        with open(file, "r",encoding="ISO-8859-1") as unitFile:
            lignes = unitFile.readlines()
            for ligne in lignes:
                if (ligne.find("m_mult_factors.setProperty")>0):
                    l = re.split("::|,|\) ", ligne)
                    mult[l[1]] = repr(l[2])
                if (ligne.find("m_short_name.setProperty")>0):
                    l = re.split("::|,|\) ", ligne)
                    sname[l[1]] = str(l[2].replace("\"",""))
                if (ligne.find("m_const_factors.setProperty")>0):
                    l = re.split("::|,|\) ", ligne)
                    add[l[1]] = repr(l[2])
                
    
        for name,short in UNITS_NAMES:
            rstFile.write("   * - %s\n" % name)
            rstFile.write("     - %s\n" % sname[name])
            rstFile.write("     - %s\n" % mult[name])
            rstFile.write("     - %s\n" % add[name])
        rstFile.close()
           
    
###################
outDir = "."
generateIndex(outDir)
generateUnitSystemFiles(outDir)