import os
from os.path import join
import sys

from helper_tools import *

# get dictionary with relevant paths for tests within this module
paths = get_pyneal_scanner_test_paths()
sys.path.insert(0, paths['pynealDir'])
sys.path.insert(0, paths['pynealScannerDir'])

import pyneal_scanner.utils.general_utils as general_utils


### Tests for classes/functions within the general_utils.py module. Where
#   applicable, test against each of the different scanner environments
class Test_general_utils:
    """ Test pyneal_scanner.utils.general_utils module """

    def test_ScannerSettings(self):
        """ test general_utils.ScannerSettings class

        Test methods in ScannerSettings class against sample data from each
        scanner make
        """
        # loop over the different scan environments
        for scanEnv in ['GE', 'Philips', 'Siemens']:
            print('testing environment: ' + scanEnv)

            # set paths based on current test environment
            if scanEnv == 'GE':
                envDir = paths['GE_dir']
                funcDir = paths['GE_funcDir']
            elif scanEnv == 'Philips':
                envDir = paths['Philips_dir']
                funcDir = paths['Philips_funcDir']
            elif scanEnv == 'Siemens':
                envDir = paths['Siemens_dir']
                funcDir = paths['Siemens_funcDir']

            # update config file to match local paths
            configFile = join(envDir, 'scannerConfig.yaml')
            replace_scannerConfig_baseDir(configFile, funcDir)

            # run through all functions in ScannerSettings class
            scanSettings = general_utils.ScannerSettings(envDir)
            scanSettings.print_allSettings()
            scanSettings.get_scannerMake()
            scanSettings.get_scannerBaseDir()
            scanSettings.get_pynealSocketHost()
            scanSettings.get_pynealSocketPort()
            scanSettings.get_allSettings()

            # remove local paths from config file
            cleanConfigFile(configFile)

            print('Passed!')

    def test_initializeSession(self):
        """ test general_utils.initializeSession() """
        # loop over the different scan environments
        for scanEnv in ['GE', 'Philips', 'Siemens']:
            print('testing environment: ' + scanEnv)

            # set paths based on current test environment
            if scanEnv == 'GE':
                envDir = paths['GE_dir']
                funcDir = paths['GE_funcDir']
            elif scanEnv == 'Philips':
                envDir = paths['Philips_dir']
                funcDir = paths['Philips_funcDir']
            elif scanEnv == 'Siemens':
                envDir = paths['Siemens_dir']
                funcDir = paths['Siemens_funcDir']

            # update config file to match local paths
            configFile = join(envDir, 'scannerConfig.yaml')
            replace_scannerConfig_baseDir(configFile, funcDir)

            general_utils.initializeSession(pynealScannerDir=envDir)

            # remove local paths from config file
            cleanConfigFile(configFile)

            print('Passed!')