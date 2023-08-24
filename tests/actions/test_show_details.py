from datetime import date
import pytest

from pro_filer.actions.main_actions import show_details  # NOQA

context = {"base_path": ""}


@pytest.mark.parametrize(
    "file_path, expected, expected_1, expected_2, expected_3, expected_4",
    [
        (
            "test_show_details.py",
            "File name: test_show_details.py",
            "File size in bytes: 0",
            "File type: file",
            "File extension: .py",
            f"Last modified date: {date.today()}",
        ),
        (
            "test_show_details",
            "File name: test_show_details",
            "File size in bytes: 0",
            "File type: file",
            "File extension: [no extension]",
            f"Last modified date: {date.today()}",
        ),
    ],
)
def test_show_all_details(
    file_path,
    expected,
    expected_1,
    expected_2,
    expected_3,
    expected_4,
    capsys,
    tmp_path,
):
    file_path = tmp_path / file_path
    file_path.touch()
    context["base_path"] = str(file_path)
    show_details(context)
    captured = capsys.readouterr()
    assert expected in captured.out
    assert expected_1 in captured.out
    assert expected_2 in captured.out
    assert expected_3 in captured.out
    assert expected_4 == captured.out.split("\n")[-2]


@pytest.mark.parametrize(
    "file_path, expected",
    [
        ("????", "File '????' does not exist"),
        ("????", "File '????' does not exist"),
    ],
)
def test_show_details_file_doesnt_exist(
    file_path,
    expected,
    capsys,
):
    context["base_path"] = file_path
    show_details(context)
    captured = capsys.readouterr()
    print(captured.out)
    assert expected in captured.out
