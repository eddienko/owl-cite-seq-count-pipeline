from pathlib import Path

import voluptuous as vo

schema = vo.Schema(
    {
        vo.Required("read1"): vo.Coerce(Path),
        vo.Required("read2"): vo.Coerce(Path),
        vo.Required("tags"): vo.Coerce(Path),
        vo.Required("cell_barcode_first_base"): int,
        vo.Required("cell_barcode_last_base"): int,
        vo.Required("umi_first_base"): int,
        vo.Required("umi_last_base"): int,
        vo.Required("expected_cells"): int,
        vo.Required("output"): vo.Coerce(Path),
        vo.Optional("trim", default=0): int,
        vo.Optional("whitelist"): vo.Coerce(Path),
        vo.Optional("extra"): list,
    }
)
