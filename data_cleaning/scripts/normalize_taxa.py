import re
import pandas as pd
import requests

PBDB_API = "https://paleobiodb.org/data1.2/"
PBDB_TAXA_ID = f"{PBDB_API}taxa/single.json?vocab=pbdb&id="
PBDB_TAXA_NAME = f"{PBDB_API}taxa/single.json?vocab=pbdb&name="


def taxon_name_parser(taxon_name):
    name_parts = {}
    modifiers = ["?", "aff.", "cf.", "f.", "morph", "s.s.", "s.l.", "var."]
    ranks = ["genus", "species", "subspecies"]

    if bool(re.search(r"\(.*?\)$", taxon_name)):
        descriptor = re.search(r"\(.*?\)$", taxon_name).group(0)
        name_parts["non-taxa descriptor"] = descriptor
        taxon_name = taxon_name.split(descriptor)[0].strip()

    parts = taxon_name.split(" ")

    current_rank_index = 0
    for index, part in enumerate(parts):
        if current_rank_index == 3:
            continue

        if part in modifiers:
            name_parts[ranks[current_rank_index] + " modifier"] = parts[index]
        else:
            name_parts[ranks[current_rank_index] + " name"] = parts[index]
            current_rank_index += 1

    if bool(re.search(r"\(.*?\)$", taxon_name)):
        descriptor = re.search(r"\(.*?\)$", taxon_name).group(0)
        name_parts["non-taxa descriptor"] = descriptor

    return name_parts


def fill_taxon(df, index, data, taxon_rank):
    # cast taxon_no to string to avoid pandas converting it to a float
    df.at[index, f"{taxon_rank}_taxon_id"] = str(data[0]["taxon_no"])
    df.at[index, f"{taxon_rank}_taxon_name"] = data[0]["taxon_name"]


def get_parent_taxa(df, parent_id, taxon_rank, round, index, data):
    if taxon_rank == "kingdom":
        return data
    elif parent_id == "0":
        return data
    elif round > 20:
        return data

    round = round + 1

    url_parent = PBDB_TAXA_ID + parent_id
    response = requests.get(url_parent)
    if response.status_code == 200:
        data = response.json()["records"]
        if len(data) == 1:
            taxon_rank = data[0]["taxon_rank"]
            parent_id = data[0]["parent_no"]
            if taxon_rank in ["family", "order", "class", "phylum", "kingdom"]:
                fill_taxon(df, index, data, taxon_rank)
            elif parent_id == "0":
                fill_taxon(df, index, data, taxon_rank)

            return get_parent_taxa(df, parent_id, taxon_rank, round, index, data)


def add_normalized_name_column(df, include_descriptor=True, include_modifier=True, col_name="normalized_name"):
    if include_modifier:
        fields = [
            "genus modifier",
            "genus name",
            "subgenera modifier",
            "subgenera name",
            "species modifier",
            "species name",
            "subspecies modifier",
            "subspecies name",
        ]
    else:
        fields = [
            "genus name",
            "subgenera name",
            "species name",
            "subspecies name",
        ]
    temp_df = df.copy()
    temp_df.fillna("", inplace=True)

    # concatenate taxa fields into a string
    df[col_name] = temp_df["Any taxon above genus"].str.cat(
        temp_df[fields], sep=" ", na_rep=""
    )

    if include_descriptor:
        des_col = "non-taxa descriptor"
        df.loc[
            (temp_df[des_col] != "") & (~temp_df[des_col].str.contains("\(")), col_name
        ] = (df[col_name] + " (" + temp_df[des_col] + ")")
        df.loc[
            (temp_df[des_col] != "") & (temp_df[des_col].str.contains("\(")), col_name
        ] = (df[col_name] + " " + temp_df[des_col])

    # get rid of extra spaces
    df[col_name] = df[col_name].str.strip()
    df[col_name] = df[col_name].replace(to_replace="  +", value=" ", regex=True)

    return df

