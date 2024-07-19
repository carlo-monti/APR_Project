def filename_to_feature_list(filename, get_column_names = False):
    '''
    This function parses the filename and returns all the informations as a list.
    If get_column_names is True it will return the names of the columns.
    '''
    parsed_info = []
    column_names = []
    if filename.endswith(".mp3"):
        column_names =  ["Date_time",
                        "Intensity",
                        "Temperature",
                        "Humidity",
                        "Pressure",
                        "Wind_speed",
                        "Video",
                        "Duration",
                        "Surface",
                        ]
        parsed_info = filename[:-4].split("_")
        if len(parsed_info) == 10:
            # some files have 10 columns. It can be either:
            # - Because we are dealing with split audio (./audio/split/....)
            # - An error in the dataset (./audio)
            if parsed_info[9].find("segment") != -1:
                column_names.append("Segment")
            else:
                parsed_info.pop(7)
    if get_column_names:
        return column_names
    else:
        return parsed_info

