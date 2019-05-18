# coding=utf-8

import json
import decimal


class DecimalEncoder(json.JSONEncoder):

    def _iterencode(self, o, makers=None):
        if isinstance(o, decimal.Decimal):
            return (str(o) for o in [o])
        return super(DecimalEncoder, self)._iterencode(o, makers)