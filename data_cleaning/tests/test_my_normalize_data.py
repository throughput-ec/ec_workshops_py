import pandas as pd
from pandas._testing import assert_frame_equal
import pytest
import numpy as np

from scripts.my_normalize_data import (
    normalize_expedition_section_cols,
    remove_bracket_text,
    remove_whitespace,
    normalize_columns
)


class XTestNormalizeColumns:
    def test_replace_column_name_with_value_from_columns_mapping(self):
        columns_mapping = {"aa": "A"}
        data = {"aa": [1]}
        df = pd.DataFrame(data)
        data = {"A": [1]}
        expected = pd.DataFrame(data)

        normalize_columns(df, columns_mapping)

        assert_frame_equal(df, expected)

    def test_replace_multiple_column_name_with_value_from_columns_mapping(self):
        columns_mapping = {"aa": "A", "b b": "B"}
        data = {"aa": [1], "b b": [2]}
        df = pd.DataFrame(data)
        data = {"A": [1], "B": [2]}
        expected = pd.DataFrame(data)

        normalize_columns(df, columns_mapping)

        assert_frame_equal(df, expected)

    def test_does_not_affect_columns_not_in_columns_mapping(self):
        columns_mapping = {"aa": "A", "b b": "B"}
        data = {"aa": [1], "b b": [2], "cc": [3]}
        df = pd.DataFrame(data)
        data = {"A": [1], "B": [2], "cc": [3]}
        expected = pd.DataFrame(data)

        normalize_columns(df, columns_mapping)

        assert_frame_equal(df, expected)

    def test_does_not_affect_columns_if_columns_mapping_has_no_value(self):
        columns_mapping = {"aa": None, "bb": "", "cc": np.nan}
        data = {"aa": [1], "b b": [2], "cc": [3]}
        df = pd.DataFrame(data)
        expected = pd.DataFrame(data)

        normalize_columns(df, columns_mapping)

        assert_frame_equal(df, expected)


class XTestRemoveBracketText:
    def test_removes_text_within_brackets_at_end_of_cell(self):
        df = pd.DataFrame(['aa [A]', 'bb [BB]', 'cc [C] ', 'dd  [dd]  '])
        expected = pd.DataFrame(['aa', 'bb', 'cc', 'dd'])

        remove_bracket_text(df)

        assert_frame_equal(df, expected)

    def test_does_not_remove_text_within_brackets_at_start_of_cell(self):
        df = pd.DataFrame(['[A] aa', '[BB] bb', '[C] cc ', '  [dd]  dd '])
        expected = df.copy()

        remove_bracket_text(df)

        assert_frame_equal(df, expected)

    def test_does_not_remove_text_within_brackets_in_middle_of_cell(self):
        df = pd.DataFrame(['aa [A] aa', 'bb [BB] bb', ' cc [C] cc ', ' dd  [dd]  dd '])
        expected = df.copy()

        remove_bracket_text(df)

        assert_frame_equal(df, expected)

    def test_removes_letters_numbers_punctuation_within_brackets(self):
        df = pd.DataFrame(['aa [A A]', 'bb [BB 123]', 'cc [123-456.] '])
        expected = pd.DataFrame(['aa', 'bb', 'cc'])

        remove_bracket_text(df)

        assert_frame_equal(df, expected)


class XTestRemoveWhitespaceFromDataframe:
    def test_remove_leading_and_trailing_spaces_from_dataframe(self):
        data = {
            'A': ['A', 'B ', '  C', 'D  ', '  Ed  ', ' 1 '],
            'B': ['Aa', 'Bb ', '  Cc', 'Dd  ', '  Ed Ed  ', ' 11 '],
        }
        df = pd.DataFrame(data)
        data2 = {
            'A': ['A', 'B', 'C', 'D', 'Ed', '1'],
            'B': ['Aa', 'Bb', 'Cc', 'Dd', 'Ed Ed', '11'],
        }
        expected = pd.DataFrame(data2)

        remove_whitespace(df)

        assert_frame_equal(df, expected)

    def test_ignores_numeric_columns(self):
        data = {
            'A': ['A', 'B  ', '  C'],
            'B': [1, 2, 3],
            'C': [1.1, 2.2, 3.3],
        }
        df = pd.DataFrame(data)
        data2 = {
            'A': ['A', 'B', 'C'],
            'B': [1, 2, 3],
            'C': [1.1, 2.2, 3.3],
        }
        expected = pd.DataFrame(data2)

        remove_whitespace(df)

        assert_frame_equal(df, expected)

    def test_handles_empty_strings(self):
        data = {'A': ['A', 'B  ', '  C', ' ']}
        df = pd.DataFrame(data)
        data2 = {'A': ['A', 'B', 'C', '']}
        expected = pd.DataFrame(data2)

        remove_whitespace(df)

        assert_frame_equal(df, expected)

    def test_converts_nan_to_empty_strings(self):
        data = {'A': ['A', 'B  ', '  C', np.nan]}
        df = pd.DataFrame(data)
        data2 = {'A': ['A', 'B', 'C', '']}
        expected = pd.DataFrame(data2)

        remove_whitespace(df)

        assert_frame_equal(df, expected)


class XTestNormalizeExpeditionSectionCols:
    def test_dataframe_does_not_change_if_expection_section_columns_exist(self):
        data = {
            "Col": [0, 1],
            "Exp": ["1", "10"],
            "Site": ["U1", "U2"],
            "Hole": ["h", "H"],
            "Core": ["2", "20"],
            "Type": ["t", "T"],
            "Section": ["3", "3"],
            "A/W": ["a", "A"],
        }
        df = pd.DataFrame(data)
        expected = pd.DataFrame(data)

        df = normalize_expedition_section_cols(df)

        assert_frame_equal(df, expected)

    def test_dataframe_does_not_change_if_expection_section_Sample_exist(self):
        data = {
            "Col": [0, 1],
            "Sample": ["1-U1h-2t-3-a", "10-U2H-20T-3-A"],
            "Exp": ["1", "10"],
            "Site": ["U1", "U2"],
            "Hole": ["h", "H"],
            "Core": ["2", "20"],
            "Type": ["t", "T"],
            "Section": ["3", "3"],
            "A/W": ["a", "A"],
        }
        df = pd.DataFrame(data)
        expected = pd.DataFrame(data)

        df = normalize_expedition_section_cols(df)

        assert_frame_equal(df, expected)

    def test_dataframe_does_not_change_if_expection_section_Label_exist(self):
        data = {
            "Col": [0, 1],
            "Label ID": ["1-U1h-2t-3-a", "10-U2H-20T-3-A"],
            "Exp": ["1", "10"],
            "Site": ["U1", "U2"],
            "Hole": ["h", "H"],
            "Core": ["2", "20"],
            "Type": ["t", "T"],
            "Section": ["3", "3"],
            "A/W": ["a", "A"],
        }
        df = pd.DataFrame(data)
        expected = pd.DataFrame(data)

        df = normalize_expedition_section_cols(df)

        assert_frame_equal(df, expected)

    def test_adds_missing_expection_section_using_Label(self):
        data = {
            "Col": [0, 1],
            "Label ID": ["1-U1h-2t-3-a", "10-U2H-20T-3-A"],
        }
        df = pd.DataFrame(data)

        data = {
            "Col": [0, 1],
            "Label ID": ["1-U1h-2t-3-a", "10-U2H-20T-3-A"],
            "Exp": ["1", "10"],
            "Site": ["U1", "U2"],
            "Hole": ["h", "H"],
            "Core": ["2", "20"],
            "Type": ["t", "T"],
            "Section": ["3", "3"],
            "A/W": ["a", "A"],
        }
        expected = pd.DataFrame(data)

        df = normalize_expedition_section_cols(df)

        assert_frame_equal(df, expected)

    def test_adds_missing_expection_section_using_Sample(self):
        data = {
            "Col": [0, 1],
            "Sample": ["1-U1h-2t-3-a", "10-U2H-20T-3-A"],
        }
        df = pd.DataFrame(data)

        data = {
            "Col": [0, 1],
            "Sample": ["1-U1h-2t-3-a", "10-U2H-20T-3-A"],
            "Exp": ["1", "10"],
            "Site": ["U1", "U2"],
            "Hole": ["h", "H"],
            "Core": ["2", "20"],
            "Type": ["t", "T"],
            "Section": ["3", "3"],
            "A/W": ["a", "A"],
        }
        expected = pd.DataFrame(data)

        df = normalize_expedition_section_cols(df)

        assert_frame_equal(df, expected)

    def test_handles_missing_aw_col(self):
        data = {
            "Col": [0, 1],
            "Sample": ["1-U1h-2t-3", "10-U2H-20T-3"],
            "Exp": ["1", "10"],
            "Site": ["U1", "U2"],
            "Hole": ["h", "H"],
            "Core": ["2", "20"],
            "Type": ["t", "T"],
            "Section": ["3", "3"],
        }
        df = pd.DataFrame(data)
        expected = pd.DataFrame(data)

        df = normalize_expedition_section_cols(df)

        assert_frame_equal(df, expected)

    def test_handles_no_data(self):
        data = {
            "Col": [0],
            "Sample": ["No data this hole"],
        }
        df = pd.DataFrame(data)

        data = {
            "Col": [0],
            "Sample": ["No data this hole"],
            "Exp": [None],
            "Site": [None],
            "Hole": [None],
            "Core": [None],
            "Type": [None],
            "Section": [None],
            "A/W": [None],
        }
        expected = pd.DataFrame(data)

        df = normalize_expedition_section_cols(df)

        assert_frame_equal(df, expected)

    def test_otherwise_raise_error(self):
        df = pd.DataFrame({"foo": [1]})

        message = "File does not have the expected columns."
        with pytest.raises(ValueError, match=message):
            normalize_expedition_section_cols(df)
