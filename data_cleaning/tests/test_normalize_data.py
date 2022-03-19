import pandas as pd
from pandas._testing import assert_frame_equal
import pytest
import numpy as np

from scripts.normalize_data import (
    normalize_columns,
    remove_whitespace_from_column_names,
    normalize_expedition_section_cols,
    remove_bracket_text,
    remove_whitespace_from_dataframe,
    ddm2dec,
    remove_empty_unnamed_columns
)


class TestNormalizeColumns:
    def test_replaces_columns_if_value_in_all_columns_matches_variants(self):
        all_cols = ["a", "B"]
        variants = {"A", "a", "aa"}
        new_col = "AAA"

        res = normalize_columns(variants, new_col, all_cols)

        assert res == ["AAA", "B"]

    def test_returns_all_columns_if_all_columns_does_not_match_variants(self):
        all_cols = ["a", "B"]
        variants = {"BB", "bb", "b"}
        new_col = "BBB"

        res = normalize_columns(variants, new_col, all_cols)

        assert res == ["a", "B"]


class RemoveSpacesFromColumns:
    def test_replaces_leading_and_trailing_spaces_from_columns(self):
        df = pd.DataFrame(columns=[' Aa', 'Bb12 ', '  Cc', 'Dd  ', '  Ed Ed  ', ' 12 ' ])

        res = remove_whitespace_from_column_names(df)

        assert res == ['Aa', 'Bb12', 'Cc', 'Dd', 'Ee Ee', '12']

    def test_returns_columns_if_no_leading_and_trailing_spaces(self):
        df = pd.DataFrame(columns=['Aa', 'Bb', 'Cc', 'Dd', 'Ed Ed'])

        res = remove_whitespace_from_column_names(df)

        assert res == ['Aa', 'Bb', 'Cc', 'Dd', 'Ee Ee' ]


class TestNormalizeExpeditionSectionCols:
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


class TestRemoveBracketText:
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


class TestRemoveWhitespaceFromDataframe:
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

        remove_whitespace_from_dataframe(df)

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

        remove_whitespace_from_dataframe(df)

        assert_frame_equal(df, expected)

    def test_handles_empty_strings(self):
        data = {'A': ['A', 'B  ', '  C', ' ']}
        df = pd.DataFrame(data)
        data2 = {'A': ['A', 'B', 'C', '']}
        expected = pd.DataFrame(data2)

        remove_whitespace_from_dataframe(df)

        assert_frame_equal(df, expected)

    def test_converts_nan_to_empty_strings(self):
        data = {'A': ['A', 'B  ', '  C', np.nan]}
        df = pd.DataFrame(data)
        data2 = {'A': ['A', 'B', 'C', '']}
        expected = pd.DataFrame(data2)

        remove_whitespace_from_dataframe(df)

        assert_frame_equal(df, expected)

class Testddm2dec:
    def test_returns_decimal_degree_fof_degree_decimal_minute(self):
        string = '25 51.498 N'
        assert ddm2dec(string) == 25.8583

    def test_works_with_decimal(self):
        string = '25 .498 N'
        assert ddm2dec(string) == 25.0083

    def test_works_with_integer(self):
        string = '25 20 N'
        assert ddm2dec(string) == 25.333333333333332

    def test_works_with_direction_first(self):
        string = 'N 25 51.498'
        assert ddm2dec(string) == 25.8583

    @pytest.mark.parametrize("string,result", [("25° 51.498'N", 25.8583), ("25°51.498'N", 25.8583)])
    def test_works_with_degree_minute_notation(self, string, result):
        assert ddm2dec(string) == result

    @pytest.mark.parametrize("string,result", [('25 51.498 e', 25.8583), ('25 51.498 w', -25.8583), ('25 51.498 S', -25.8583), ('25 51.498 n', 25.8583)])
    def test_adds_correct_sign_for_direction(self, string, result):
        assert ddm2dec(string) == result



class TestRemoveEmptyUnnamedColumns:
    def test_remove_unnamed_columns_with_no_content(self):
        data = {'A': [1, 2, 3], 'B': ['a', 'b', 'c'], 'Unnamed: 12': [None, None, None]}
        df = pd.DataFrame(data)
        data = {'A': [1, 2, 3], 'B': ['a', 'b', 'c']}
        expected = pd.DataFrame(data)

        remove_empty_unnamed_columns(df)

        assert_frame_equal(df, expected)

    def test_does_change_named_columns_without_content(self):
        data = {'A': [1, 2, 3], 'B': ['a', 'b', 'c'], 'C': [None, None, None]}
        df = pd.DataFrame(data)
        expected = pd.DataFrame(data)

        remove_empty_unnamed_columns(df)

        assert_frame_equal(df, expected)


    def test_does_change_unnamed_columns_with_content(self):
        data = {'A': [1, 2, 3], 'B': ['a', 'b', 'c'], 'Unnamed: 12': ['a', None, None]}
        df = pd.DataFrame(data)
        expected = pd.DataFrame(data)

        remove_empty_unnamed_columns(df)

        assert_frame_equal(df, expected)
