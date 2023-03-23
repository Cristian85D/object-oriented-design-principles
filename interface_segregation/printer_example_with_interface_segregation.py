from abc import ABC, abstractmethod

class Print(ABC):

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def get_print_spool_details(self):
        pass


class Scan(ABC):

    @abstractmethod
    def scan(self):
        pass

    @abstractmethod
    def scan_photo(self):
        pass


class Fax(ABC):

    @abstractmethod
    def fax(self):
        pass

    @abstractmethod
    def internet_fax(self):
        pass


class XeroxWorkCentre(Print, Scan, Fax):
    def print(self):
        """ Assume real code here"""

    def get_print_spool_details(self):
        """ Assume real code here"""

    def scan(self):
        """ Assume real code here"""

    def scan_photo(self):
        """ Assume real code here"""

    def fax(self):
        """ Assume real code here"""

    def internet_fax(self):
        """ Assume real code here"""


class HPPrinterScanner(Print, Scan):

    def print(self):
        """ Assume real code here"""

    def get_print_spool_details(self):
        """ Assume real code here"""

    def scan(self):
        """ Assume real code here"""

    def scan_photo(self):
        """ Assume real code here"""


class CannonPrinter(Print):

    def print(self):
        """ Assume real code here"""

    def get_print_spool_details(self):
        """ Assume real code here"""
