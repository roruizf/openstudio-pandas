import os
from typing import Optional
import openstudio


def load_osm_file_as_model(osm_file_path: str, version_translator: Optional[bool] = True) -> openstudio.model.Model:
    """Loads an OSM file into an OpenStudio model.

    Args:
        osm_file_path: The path to the OSM file. This can be a relative path
            or an absolute path.
        version_translator: Whether to use the OpenStudio version translator.
            This is necessary if the OSM file is in a version of OpenStudio
            that is different from the version of OpenStudio that is being used
            to load the file. Defaults to True.

    Returns:
        An OpenStudio model containing the data from the OSM file.
    """
    # Get the absolute path to the OSM file.
    osm_file_path = os.path.abspath(osm_file_path)

    if version_translator:
        translator = openstudio.osversion.VersionTranslator()
        osm_model = translator.loadModel(osm_file_path).get()
    else:
        osm_model = openstudio.model.Model.load(osm_file_path).get()

    print(
        f"The OSM read file contains data for the {osm_model.building().get().name()}")
    # Return the OpenStudio model.
    return osm_model


def save_model_as_osm_file(osm_model, osm_file_path, new_file_name=None):

    osm_file_folder = os.path.split(osm_file_path)[0]

    if new_file_name is not None:
        new_osm_file_name = new_file_name
    else:
        new_osm_file_name = os.path.split(osm_file_path)[-1]

    openstudio.model.saveModel(
        osm_model, new_osm_file_name, osm_file_folder)