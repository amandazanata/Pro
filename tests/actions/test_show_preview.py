import pytest

from pro_filer.actions.main_actions import show_preview  # NOQA


@pytest.mark.parametrize(
    "context, expected, expected_1, expected_2",
    [
        (
            {
                "all_files": [],
                "all_dirs": [],
            },
            "Found 0 files and 0 directories",
            "",
            "",
        ),
        (
            {
                "all_files": ["1", "1", "1", "1", "1", "1"],
                "all_dirs": ["1", "1", "1", "1", "1", "1"],
            },
            "Found 6 files and 6 directories",
            "First 5 files: ['1', '1', '1', '1', '1']",
            "First 5 directories: ['1', '1', '1', '1', '1']",
        ),
        (
            {
                "all_files": ["1", "1", "1", "1", "1", "1"],
                "all_dirs": [],
            },
            "Found 6 files and 0 directories",
            "First 5 files: ['1', '1', '1', '1', '1']",
            "First 5 directories: []",
        ),
        (
            {
                "all_files": [],
                "all_dirs": ["1", "1", "1", "1", "1", "1"],
            },
            "Found 0 files and 6 directories",
            "First 5 files: []",
            "First 5 directories: ['1', '1', '1', '1', '1']",
        ),
    ],
)
def test_preview(context, expected, expected_1, expected_2, capsys):
    show_preview(context)
    out = capsys.readouterr()
    assert expected in out.out
    assert expected_1 in out.out
    assert expected_2 in out.out
