from datetime import datetime
from exceptions import (
    NegativeTitlesError,
    InvalidYearCupError,
    ImpossibleTitlesError
)


def data_processing(selection_info_dict: dict):
    if selection_info_dict.get('titles') < 0:
        raise NegativeTitlesError("titles cannot be negative")

    first_cup_str = selection_info_dict.get('first_cup')
    if first_cup_str:
        first_cup_date = datetime.strptime(first_cup_str, "%Y-%m-%d").date()
        selection_info_dict['first_cup'] = first_cup_date
        first_cup_year = first_cup_date.year

        if first_cup_year < 1930 or (first_cup_year - 1930) % 4 != 0:
            raise InvalidYearCupError("there was no world cup this year")

    current_year = datetime.now().year
    max_titles_possible = (current_year - first_cup_year) // 4

    if selection_info_dict.get('titles') > max_titles_possible:
        raise ImpossibleTitlesError(
            "impossible to have more titles than disputed cups"
            )
