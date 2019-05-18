#!/usr/bin/env python

from pyrfc import TypeDescription, FunctionDescription

def get_standard_func():
    t_header = TypeDescription("ZHBREWSHEADER", nuc_length=90, uc_length=180)
    t_header.add_field(name=u'TYPE', field_type='RFCTYPE_CHAR',
        nuc_offset=0, uc_offset=0,
        nuc_length=30, uc_length=60)
    t_header.add_field(name=u'VALUE', field_type='RFCTYPE_CHAR',
        nuc_offset=0, uc_offset=0,
        nuc_length=60, uc_length=120)

    zhbr_ews_async = FunctionDescription("ZHBR_EWS_ASYNC")
    zhbr_ews_async.add_parameter(name=u'E_FAIL_MSG', parameter_type='RFCTYPE_CHAR',
        direction='RFC_EXPORT',
        nuc_length=1,
        uc_length=2)
    zhbr_ews_async.add_parameter(name=u'I_EWS_ID', parameter_type='RFCTYPE_CHAR',
        optional=True,
        direction='RFC_IMPORT',
        nuc_length=18,
        uc_length=24)
    zhbr_ews_async.add_parameter(name=u'I_STATUS', parameter_type='RFCTYPE_CHAR',
        optional=True,
        direction='RFC_IMPORT',
        nuc_length=1,
        uc_length=2)
    zhbr_ews_async.add_parameter(name=u'I_TIMESTAMP', parameter_type='RFCTYPE_BCD',
        optional=True,
        direction='RFC_IMPORT',
        nuc_length=8,
        uc_length=8)
    zhbr_ews_async.add_parameter(name=u'I_RISK_INFO', parameter_type='RFCTYPE_STRING',
        optional=True,
        direction='RFC_IMPORT',
        nuc_length=0,
        uc_length=0)
    zhbr_ews_async.add_parameter(name=u'T_HEADER', parameter_type='RFCTYPE_TABLE',
        optional=True,
        direction='RFC_TABLES',
        nuc_length=90,
        uc_length=180,
        type_description=t_header)
    zhbr_ews_async.add_parameter(name=u'T_TABLE', parameter_type='RFCTYPE_TABLE',
        optional=True,
        direction='RFC_TABLES',
        nuc_length=256,
        uc_length=512)
    return zhbr_ews_async