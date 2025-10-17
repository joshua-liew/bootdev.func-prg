from enum import Enum


class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4


def get_csv_status(status, data):
    match (status):
        case (CSVExportStatus.PENDING):
            status_str = "Pending..."
            result = data_to_strings(data)
            return (status_str, result)
        case (CSVExportStatus.PROCESSING):
            status_str = "Processing..."
            result = data_to_single_string(data)
            return (status_str, result)
        case (CSVExportStatus.SUCCESS):
            status_str = "Success!"
            result = data
            return (status_str, result)
        case (CSVExportStatus.FAILURE):
            status_str = "Unknown error, retrying..."
            result = data_to_single_string(data_to_strings(data))
            return (status_str, result)
        case _:
            raise Exception("unknown export status")


def data_to_strings(data):
    return list(
        map(
            lambda inner_list: list(map(
                lambda x: str(x), inner_list
            )),
            data
        )
    )


def data_to_single_string(data):
    return "\n".join(
        list(
            map(lambda inner_list: ",".join(inner_list), data)
        )
    )
