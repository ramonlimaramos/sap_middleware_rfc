
import simplejson, sys
from sap.sap_adapter import RFC


def flush():
    sys.stdout.flush()


def async_func_result(request_context=None, **args):

    try:

        print('[SAP Middleware Listener] received', args)
        flush()

    except Exception as e:
        print('[SAP Middleware Listener] ** error publishing **', e)
        flush()

def main():
    """
    Creates a listener service which expect an execution
    from SAP RFC ABAP (eg. se37) side to be invoked. 
    """
    RFC().notification_func('RFC_NAME', async_func_result)

if __name__ == '__main__':
    main()