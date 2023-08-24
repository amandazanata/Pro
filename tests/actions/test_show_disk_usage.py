from pytest_dependency import pytest

from pro_filer.actions.main_actions import _get_printable_file_path  # NOQA
from pro_filer.actions.main_actions import show_disk_usage  # NOQA


@pytest.mark.parametrize(
    "file_1, file_2, file_3",
    [
        (
            "app.py",
            "app_test.py",
            "app_test2.py",
        ),
    ],
)
def test_show_disk_usage(file_1, file_2, file_3, capsys, tmp_path):
    tmp_path = tmp_path / "src"
    tmp_path.mkdir()
    edit1 = tmp_path / file_1
    edit2 = tmp_path / file_2
    edit3 = tmp_path / file_3
    edit1.touch()
    edit2.touch()
    edit3.touch()
    edit1.write_text("print('hello world')")
    edit2.write_text("print('hello')")
    edit3.write_text("print('hello')")
    context = {"all_files": [str(edit1), str(edit2), str(edit3)]}
    out1 = f"'{_get_printable_file_path(str(edit1))}':".ljust(69)
    out2 = f"'{_get_printable_file_path(str(edit2))}':".ljust(69)
    out3 = f"'{_get_printable_file_path(str(edit3))}':".ljust(69)
    show_disk_usage(context)
    captured = capsys.readouterr()
    assert (
        captured.out
        == f"{out1}  20 (41%)\n{out2}  14 (29%)\n{out3}  14 (29%)\n\
Total size: 48\n"
    )
