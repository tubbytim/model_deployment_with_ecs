
import re
from typing import Any, Union
import numpy as np
import pandas as pd

# float type for np.nan
def get_first_cabin(row: Any) -> Union[str, float]:
    try:
        return row.split()[0]
    except AttributeError:
        return np.nan


def get_title(passenger: str) -> str:
    """Extracts the title (Mr, Ms, etc) from the name variable."""
    line = passenger
    if re.search("Mrs", line):
        return "Mrs"
    elif re.search("Mr", line):
        return "Mr"
    elif re.search("Miss", line):
        return "Miss"
    elif re.search("Master", line):
        return "Master"
    else:
        return "Other"


def pre_pipeline_preparation(*, dataframe: pd.DataFrame) -> pd.DataFrame:
    # replace question marks with NaN values
    data = dataframe.replace("?", np.nan)

    # retain only the first cabin if more than
    # 1 are available per passenger
    data["cabin"] = data["cabin"].apply(get_first_cabin)

    data["title"] = data["name"].apply(get_title)

    # cast numerical variables as floats
    data["fare"] = data["fare"].astype("float")
    data["age"] = data["age"].astype("float")

    data.drop(labels=['name', 'ticket', 'boat', 'body'], axis=1, inplace=True, errors='ignore')

    return data