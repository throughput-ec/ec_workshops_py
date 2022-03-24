import re
import numpy as np
import pandas as pd

# HACK: (@)? are meaningless matches so each regex has 7 capture groups
# (1)-(U1)(A)
# (Exp)-(Site)(Hole)
sample_hole_regex = r"(^\d+)-(U\d+)([a-zA-Z])(@)?(@)?(@)?(@)?$"
# (1)-(U1)(A)-(1)
# (Exp)-(Site)(Hole)-(Core)
sample_core_regex = r"(^\d+)-(U\d+)([a-zA-Z])-(\d+)(@)?(@)?(@)?$"
# (1)-(U1)(A)-(1)(A)
# (Exp)-(Site)(Hole)-(Core)(Type)
sample_type_regex = r"(^\d+)-(U\d+)([a-zA-Z])-(\d+)([a-zA-Z])(@)?(@)?$"
# (1)-(U1)(A)-(1)(A)-(1)
# (1)-(U1)(A)-(1)(A)-(A)
# (Exp)-(Site)(Hole)-(Core)(Type)-(Section)
sample_sect_regex = r"(^\d+)-(U\d+)([a-zA-Z])-(\d+)([a-zA-Z])-(\w+)(@)?$"
# (1)-(U1)(A)-(1)(A)-(1)-(1)
# (1)-(U1)(A)-(1)(A)-(A)-(A)
# (Exp)-(Site)(Hole)-(Core)(Type)-(Section)-(AW)
sample_aw_regex = r"(^\d+)-(U\d+)([a-zA-Z])-(\d+)([a-zA-Z])-(\w+)-(\w+)"
# (1)-(U1)(A)-(1)-(1)-(1)
# (1)-(U1)(A)-(1)-(A)-(A)
# (Exp)-(Site)(Hole)-(Core)-(Section)-(AW)
sample_no_type_aw_regex = r"(^\d+)-(U\d+)([a-zA-Z])-(\d+)(@)?-(\w+)-(\w+)"
invalid_sample_regex = r"(-)?(-)?(-)?(-)?(-)?(-)?(-)?"


def normalize_expedition_section_cols(df):
    """Create Exp...Section columns using Sample or Label ID"""
    # NOTE: There was one file that did not have A/W column
    names = {"Exp", "Site", "Hole", "Core", "Type", "Section"}
    if names.issubset(df.columns):
        pass
    elif "Sample" in df.columns:
        df = df.join(create_sample_cols(df["Sample"]))
    elif "Label ID" in df.columns:
        df = df.join(create_sample_cols(df["Label ID"]))
    else:
        raise ValueError("File does not have the expected columns.")
    return df


def valid_sample_value(name):
    if isinstance(name, str):
        name = re.sub(r"-#\d*", "", name)

    if name is None:
        return True
    elif name is np.NaN:
        return True
    elif name == "No data this hole":
        return True
    elif re.search(sample_hole_regex, name):
        return True
    elif re.search(sample_core_regex, name):
        return True
    elif re.search(sample_type_regex, name):
        return True
    elif re.search(sample_sect_regex, name):
        return True
    elif re.search(sample_no_type_aw_regex, name):
        return True
    elif re.search(sample_aw_regex, name):
        return True
    else:
        # print("bad", name)
        return False


def extract_sample_parts(name):
    if isinstance(name, str):
        name = re.sub(r"-#\d*", "", name)

    if name is None or name == "No data this hole" or name is np.NaN:
        result = re.search(invalid_sample_regex, "")
    elif re.search(sample_hole_regex, name):
        result = re.search(sample_hole_regex, name)
    elif re.search(sample_core_regex, name):
        result = re.search(sample_core_regex, name)
    elif re.search(sample_type_regex, name):
        result = re.search(sample_type_regex, name)
    elif re.search(sample_sect_regex, name):
        result = re.search(sample_sect_regex, name)
    elif re.search(sample_no_type_aw_regex, name):
        result = re.search(sample_no_type_aw_regex, name)
    elif re.search(sample_aw_regex, name):
        result = re.search(sample_aw_regex, name)
    else:
        result = re.search(invalid_sample_regex, name)

    return result.groups()


def create_sample_cols(series):
    """Extract Exp...A/W info from a panda series"""
    df = pd.DataFrame(
        {
            "Exp": [],
            "Site": [],
            "Hole": [],
            "Core": [],
            "Type": [],
            "Section": [],
            "A/W": [],
        }
    )

    for item in series.to_list():
        parts = extract_sample_parts(item)
        parts_dict = {
            "Exp": parts[0],
            "Site": parts[1],
            "Hole": parts[2],
            "Core": parts[3],
            "Type": parts[4],
            "Section": parts[5],
            "A/W": parts[6],
        }
        temp = pd.DataFrame([parts_dict])
        df = pd.concat([df, temp], ignore_index=True)

    if not all([valid_sample_value(x) for x in series]):
        raise ValueError("Sample name uses wrong format.")

    return df


def remove_whitespace_from_column_names(df):
    """remove leading and trailing spaces from dataframe columns"""
    return [col.strip() for col in df.columns]


def remove_bracket_text(df):
    """remove trailing text inside brackets."""
    df.replace(r" *\[.*\] *$", "", regex=True, inplace=True)
    return df


def remove_whitespace(df):
    """remove leading and trailing spaces from dataframe rows"""
    for col in df.columns:
        # only process string columns
        if df[col].dtype == "object":
            if len(df[df[col].isna()]) > 0:
                df[col].fillna("", inplace=True)
            try:
                df[col] = df[col].map(str.strip)
            except TypeError:
                print('Must call fillna("") before using whitespace_remover.')


# https://gis.stackexchange.com/questions/398021/converting-degrees-decimal-minutes-to-decimal-degrees-in-python
def ddm2dec(dms_str):
    """Return decimal representation of degree decimal minutes"""
    if pd.isna(dms_str):
        return

    sign = -1 if re.search("[swSW]", dms_str) else 1

    matches = re.search(r"(\d+) (\d*).(\d*)", dms_str)
    if matches:
        numbers = matches.groups()
    else:
        matches = re.search(r"(\d+)° *(\d*).(\d*)\'", dms_str)
        numbers = matches.groups()

    degree = numbers[0]
    minute_decimal = numbers[1]
    decimal_val = numbers[2] if len(numbers) > 2 else "0"
    minute_decimal += "." + decimal_val

    return sign * (int(degree) + float(minute_decimal) / 60)


def remove_empty_unnamed_columns(df):
    for col in df.columns:
        if re.match(r"^Unnamed: \d+$", col):
            if len(df[col].dropna(how="all")) == 0:
                del df[col]


def print_df(df, num_rows=5):
    print(df.shape)
    return df.head(num_rows)


def normalize_columns(df, columns_mapping):
    """Replace variations of column name with a standard column name"""
    temp = {}
    for col in df.columns:
        if col in columns_mapping:
            value = columns_mapping[col]
            if value and value == value:
                temp[col] = value

    if len(temp) > 0:
        df.rename(columns=temp, inplace=True)
