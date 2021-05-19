"""
Module handling loading and processing of data.
"""
import pandas as pd
from pathlib import Path
from datetime import date, datetime


def __convert_date(value):
    """Convert recording date to datetime object.

    This function converts a recording date in the 
    following format "%d-%m-%Y" to a datetime.datetime object.

    Args:
        - value: the string to be converted.

    Returns:
        the converted string into a datetime.datetime object.
    """
    return datetime.strptime(value, '%d-%m-%Y')


def __convert_recording_time(value):
    """Convert recording date from string to datetime object.
    """
    return datetime.strptime(value, '%H.%M')


def __convert_age(value):
    return int(value.split(' ')[0])


def __convert_weight(value):
    return float(value.split(' ')[0])


def __convert_height(value):
    return float(value.split(' ')[0])*100.


def __convert_recording_info(field, value):
    conversion_dict = {
        'Data': __convert_date,
        'Orario reg Soundi': __convert_recording_time,
        'Orario reg Gima': __convert_recording_time,
        'Età': __convert_age,
        'Peso': __convert_weight,
        'Altezza': __convert_height,
    }
    if (field in conversion_dict.keys()):
        return conversion_dict[field](value)
    else:
        raise ValueError


def load_recording_info(path):
    """Load recording information from the file in the given
    path.

    This function processes the file in the provided path and
    extract the following information:

    -`Data` (datetime.datetime Object): year, month, and day of the recording

    -`Orario reg Gima` (datetime.datetime Object): year, month, day, hour, and minute of the Gima recording

    -`Orario reg Soundi` (datetime.datetime Object): year, month, day, hour and minute of the Soundi recording

    -`Età` (int) : subject age 

    -`Peso` (float) : subject weight 

    -`Altezza` (float) : subject height

    Args:
        path (str): path to the file containing recording information.

    Returns:
        recording_info_dict (dict): dictionary with recording information fields.

    Raises:
        ValueError: if path not found
    """
    # Check on path
    if (not isinstance(path, Path)):
        path = Path(path)
    # Check on path existance
    if (not path.exists()):
        raise ValueError

    recording_info_dict = {}

    with open(path, 'r') as f:
        for line in f.readlines():
            field = line.split(':')[0]
            value = line.split(':')[1][1:]
            value = value.replace('\n', '')
            if (value[0] == ' '):
                value = value.replace(' ', '')
            value = __convert_recording_info(field, value)
            recording_info_dict[field] = value
    # Add time (year, month, day) to Gima and Soundi recordings
    recording_info_dict['Orario reg Gima'] = datetime(year=recording_info_dict['Data'].year,
                                                      month=recording_info_dict['Data'].month,
                                                      day=recording_info_dict['Data'].day,
                                                      hour=recording_info_dict['Orario reg Gima'].hour,
                                                      minute=recording_info_dict['Orario reg Gima'].minute,
                                                      second=recording_info_dict['Orario reg Gima'].second)
    recording_info_dict['Orario reg Soundi'] = datetime(year=recording_info_dict['Data'].year,
                                                        month=recording_info_dict['Data'].month,
                                                        day=recording_info_dict['Data'].day,
                                                        hour=recording_info_dict['Orario reg Soundi'].hour,
                                                        minute=recording_info_dict['Orario reg Soundi'].minute,
                                                        second=recording_info_dict['Orario reg Soundi'].second)

    return recording_info_dict


def __load_single_column_data(path):
    """Load single-column data from file.

    This function loads data from a file containing
    a single column of data, with scientific notation for 
    data formatting

    Args:
        path (str): path to the file containing data

    Returns:
        data: :class:`numpy.ndarray` with data.
    """
    # Check on path
    if (not isinstance(path, Path)):
        path = Path(path)
    # Check on path existance
    if (not path.exists()):
        raise ValueError

    data = []
    with open(path, 'r') as f:
        for line in f.readlines():
            data.append(float(line))

    print(len(data))


def load_pcg(path):
    """Load PCG data from file.

    This function loads PCG data from a file containing
    a single column, with scientific notation for 
    data formatting

    Args:
        path (str): path to the file containing PCG data

    Returns:
        data:  :class:`numpy.ndarray` with PCG data.
    """
    return __load_single_column_data(path)


def load_ppg(path):
    """Load PPG data from file.

    This function loads PCG data from a file containing
    a single column, with scientific notation for 
    data formatting

    Args:
        path (str): path to the file containing PPG data

    Returns:
        data:  :class:`numpy.ndarray` array with PPG data.
    """
    return __load_single_column_data(path)


def extract_pcg_ppg_slots(pcg, ppg, sampling_frequency, slot_size, overlap):
    """

    """
    pass
