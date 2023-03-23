from abc import ABC, abstractmethod


class Multifunction(ABC):

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def get_print_spool_details(self):
        pass

    @abstractmethod
    def scan(self):
        pass

    @abstractmethod
    def scan_photo(self):
        pass

    @abstractmethod
    def fax(self):
        pass

    @abstractmethod
    def internet_fax(self):
        pass


class CannonPrinter(Multifunction):

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


class HPPrinterScanner(Multifunction):

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


class XeroxWorkCentre(Multifunction):

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


