from sap_adapter import RFC

inputs = {
    'REQUTEXT' = 'Hello SAP!'
}
result = RFC().invoke_func('STFC_CONNECTION', inputs)

print(result)