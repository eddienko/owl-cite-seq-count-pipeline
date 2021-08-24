from unittest import mock

from distributed.utils_test import client  # noqa: F401
from owl_cite_seq_count.main import main
from owl_cite_seq_count.schema import schema


def test_schema():
    config = {"datalen": 100, "output_dir": "/tmp"}
    schema(config)


@mock.patch("time.sleep", return_value=None)
def test_main(psleep):
    config = {"datalen": 10, "output_dir": "/tmp"}
    main.config = {}
    res = main(**config)
    assert res == 120
