import sys
from pathlib import Path

from cite_seq_count.__main__ import main as cite_main
from distributed import Client
from owl_dev import pipeline
from owl_dev.logging import logger


@pipeline
def main(
    *,
    read1: Path,
    read2: Path,
    tags: Path,
    cell_barcode_first_base: int,
    cell_barcode_last_base: int,
    umi_first_base: int,
    umi_last_base: int,
    expected_cells: int,
    start_trim: int,
    output: Path,
):
    args = [
        "-R1",
        f"{read1}",
        "-R2",
        f"{read2}",
        "-t",
        f"{tags}",
        "-cbf",
        f"{cell_barcode_first_base}",
        "-cbl",
        f"{cell_barcode_last_base}",
        "-umif",
        f"{umi_first_base}",
        "-umil",
        f"{umi_last_base}",
        "-cells",
        f"{expected_cells}",
        "-trim",
        f"{start_trim}",
        "-o",
        f"{output}",
    ]

    client = Client.current()
    fut = client.submit(cite_main, args)
    client.gather(fut)
