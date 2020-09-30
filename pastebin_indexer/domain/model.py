from dataclasses import dataclass, field

from arrow import Arrow
from dataclasses_json import dataclass_json, config
from marshmallow import fields

from pastebin_indexer.helpers.serialization import encoder, decoder


@dataclass_json
@dataclass(frozen=True)
class Paste:
    id: str # noqa
    username: str # noqa
    title: str # noqa
    date: Arrow = field( # noqa
        metadata=config(
            encoder=encoder,
            decoder=decoder,
            mm_field=fields.DateTime(format='iso')
        )
    )
    content: str  # noqa
