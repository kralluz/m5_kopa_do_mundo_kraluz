from exceptions import (
    NegativeTitlesError,
    InvalidYearCupError,
    ImpossibleTitlesError
)

def data_processing(selection_info_dict: dict):
    if selection_info_dict.get('titles') < 0:
        raise NegativeTitlesError
    if (
        selection_info_dict.get('year') < 1930
        ) or (
            selection_info_dict.get('year') % 4 != 0
            ):
        raise InvalidYearCupError
    if (
        selection_info_dict.get('titles') < 0
        ) or (
            selection_info_dict.get('titles') > ((
                2023 - selection_info_dict.get('first_cup')) / 4)
            ):
        raise ImpossibleTitlesError
