import logging

from deploy.Windows.emulator import EmulatorManager
from deploy.Windows.logger import logger
from deploy.Windows.utils import *


def show_fix_tip(module):
    logger.info(f"""
    To fix this:
    1. Open console.bat
    2. Execute the following commands:
        pip uninstall -y {module}
        pip install --no-cache-dir {module}
    3. Re-open Alas.exe
    """)


class AdbManager(EmulatorManager):
    def adb_install(self):
        logger.hr('Start ADB service', 0)

        if self.ReplaceAdb:
            logger.hr('Replace ADB', 1)
            self.adb_replace()
        if self.AutoConnect:
            logger.hr('ADB Connect', 1)
            self.brute_force_connect()
