from rosie.chamber_of_deputies import settings
from rosie.chamber_of_deputies.adapter import Adapter
from rosie.core import Core


def main(target_directory='/tmp/serenata-data', years=None):
    adapter = Adapter(target_directory, years=years)
    core = Core(settings, adapter)
    core()
