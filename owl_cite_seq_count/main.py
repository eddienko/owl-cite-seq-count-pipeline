import os
from pathlib import Path
from typing import List

import dask
from cite_seq_count.__main__ import main as cite_main
from distributed import Client
from owl_dev import pipeline
from owl_dev.logging import logger


@pipeline()
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
    trim: int,
    output: Path,
    whitelist: Path = None,
    extra: List = None,
):
    extra = extra or []

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
        f"{trim}",
        "-o",
        f"{output}",
    ]

    if whitelist is not None:
        args += ["-wl", f"{whitelist}"]

    cpu_requests = os.getenv("CPU_REQUESTS")
    if cpu_requests is not None:
        args += ["--threads", f"{cpu_requests}"]

    args += [str(v) for v in extra]

    client = Client.current()
    with dask.annotate(executor="processes", retries=2):
        fut = client.submit(cite_main, args)
    try:
        client.gather(fut)
    except Exception as e:
        logger.error(e, exc_info=True)
        raise
