import pandas as pd
from pathlib import Path
import geopandas as gpd
from ipyleaflet import Map, CircleMarker
from IPython.display import  FileLink


paths = list(Path('..', 'processed_data', 'clean_data').rglob('*.csv'))
hole_path = Path('..', 'processed_data', 'Hole Summary_23_2_2021.csv')
taxa_search_path = Path('..', 'processed_data', 'normalized_taxa_list.csv')
nontaxa_list_path = Path('..', 'processed_data', 'normalized_nontaxa_list.csv')


def get_holes():
    cols = ["Exp", "Site", "Hole", "Latitude_decimal", "Longitude_decimal"]
    hole_df = pd.read_csv(hole_path, usecols=cols)

    return gpd.GeoDataFrame(
        hole_df,
        geometry=gpd.points_from_xy(hole_df['Longitude_decimal'], hole_df['Latitude_decimal']),
    )


def search_for_taxa_in_all_files(taxa):
    dfs = []

    for path in paths:
        df = search_for_taxa_in_dataframe(path, taxa)
        dfs.append(df)

    search_df = pd.concat(dfs).reset_index(drop=True)

    hole_gdf = get_holes()
    return search_df.merge(hole_gdf, on=['Exp', 'Site', 'Hole'])


def search_for_taxa_in_dataframe(path, taxa):
    nontaxa_list_df = pd.read_csv(nontaxa_list_path)

    df = pd.read_csv(path, dtype=str)
    taxa_cols = set(df.columns).intersection(taxa)
    if len(taxa_cols) > 0:
        nontaxa_cols = set(df.columns).intersection(set(nontaxa_list_df["field"]))
        return df[list(nontaxa_cols) + list(taxa_cols)]


def get_matching_taxa(search_terms):
    taxa_matches = set()

    for search_term in search_terms:
        taxa_matches.update(get_matches_for_field('basic_name', search_term))
        taxa_matches.update(get_matches_for_field('normalized_name', search_term))

    return taxa_matches


def get_matches_for_field(field, search_term):
    df = pd.read_csv(taxa_search_path)
    pattern = rf"\b{search_term}\b"
    return list(df[df[field].str.contains(pattern, regex=True)]["verbatim_name"])


def draw_map(df):
    m = Map(center=(0, 0), zoom=1)
    m.layout.height = "400px"

    for index, hole in df.iterrows():
        # name = f'Exp: {hole["Exp"]},<br> Site: {hole["Site"]},<br> Taxa: {hole["found_taxa"]}'
        marker = CircleMarker(
            location=(hole["Latitude_decimal"], hole["Longitude_decimal"]),
            weight=2,
            radius=7
        )
        # marker.popup = HTML(value=name)

        m.add_layer(marker)

    return m

def filter_samples_by_bounding_box(map, search_df, map_df):
    geom = gpd.points_from_xy(map_df['Longitude_decimal'], map_df['Latitude_decimal'])
    gdf_points = gpd.GeoDataFrame(geometry=geom, crs='epsg:4326')

    # gdf_points.cx[xmin:xmax, ymin:ymax]
    return search_df.merge(gdf_points.cx[map.east: map.west, map.north: map.south])


# https://github.com/jupyter-widgets/ipywidgets/issues/2471
class DownloadFileLink(FileLink):
    html_link_str = "<a href='{link}' download={file_name}>{link_text}</a>"

    def __init__(self, path, file_name=None, link_text=None, *args, **kwargs):
        super(DownloadFileLink, self).__init__(path, *args, **kwargs)

        self.file_name = file_name or os.path.split(path)[1]
        self.link_text = link_text or self.file_name

    def _format_path(self):
        from html import escape

        fp = "".join([self.url_prefix, escape(self.path)])
        return "".join(
            [
                self.result_html_prefix,
                self.html_link_str.format(
                    link=fp, file_name=self.file_name, link_text=self.link_text
                ),
                self.result_html_suffix,
            ]
        )


def display_search_results(search_terms):
    taxa_matches = get_matching_taxa(search_terms)

    search_df = search_for_taxa_in_all_files(taxa_matches)
    map_df = search_df.drop_duplicates(subset=['Exp', 'Site', 'Hole'])

    print(f'{len(search_df)} samples, {len(map_df)} holes')

    for taxon in taxa_matches:
        print(taxon)

    return draw_map(map_df)
