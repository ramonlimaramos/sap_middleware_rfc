# SAP RFC Middleware REST Service

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


This project is based on
Asynchronous, non-blocking [SAP NW RFC SDK Client](https://github.com/SAP/PyRFC) bindings for Python.

## Prerequisites

SAP NW RFC SDK C++ binaries must be downloaded (SAP partner or customer account required) and locally installed ([installation instructions](http://sap.github.io/PyRFC/install.html#sap-nw-rfc-library-installation)). More information on [SAP NW RFC SDK section on SAP Support Portal](https://support.sap.com/en/product/connectors/nwrfcsdk.html).

SAP NW RFC Library is fully backwards compatible, supporting all NetWeaver systems, from today S4, down to R/3 release 4.6C. Using the latest version is recommended.

### Windows

On Windows platforms the Microsoft Visual C++ 2005 Service Pack 1 Redistributable Package (KB973544), or [newer](https://www.microsoft.com/en-us/download/details.aspx?id=48145), must be installed, per [SAP Note 1375494 - SAP system does not start after applying SAP kernel patch](https://launchpad.support.sap.com/#/notes/1375494).

### macOS

* The macOS firewall stealth mode must be disabled ([Can't ping a machine - why?](https://discussions.apple.com/thread/2554739)):

```shell
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setstealthmode off
```

* Remote paths must be set in SAP NWRFC SDK for macOS: [node-rfc/#58](https://github.com/SAP/node-rfc/issues/58#issuecomment-446544151)

## Installation

After the SAP NW RFC SDK [installed](#prerequisites) on your system, you can pip install the _pyrfc_ package for your platform from the [dist](dist) folder:

```shell
wget https://github.com/SAP/PyRFC/blob/master/dist/pyrfc-1.9.94-cp37-cp37m-macosx_10_14_x86_64.whl

pip install pyrfc-1.9.94-cp37-cp37m-macosx_10_14_x86_64.whl

git clone https://github.com/ramonlimaramos/sap_middleware_rfc.git

cd sap_middleware_rfc
python -m virtualenv env
python -m pip install -r requirements.txt
```

Alternatively, or if the _pyrfc_ package for your platform not provided, [build the package from source](http://sap.github.io/PyRFC/build.html) on your system and pip install:

```shell
git clone https://github.com/SAP/PyRFC.git
cd PyRFC
python setup.py bdist_wheel
pip install dist/pyrfc-1.9.94-cp37-cp37m-macosx_10_14_x86_64.whl
# set ABAP system parameters in test/pyrfc.cfg
pytest -vv

git clone https://github.com/ramonlimaramos/sap_middleware_rfc.git

cd sap_middleware_rfc
python -m virtualenv env
python -m pip install -r requirements.txt
```
See also the the [pyrfc documentation](http://sap.github.io/PyRFC),
complementing _SAP NW RFC SDK_ [documentation](https://support.sap.com/nwrfcsdk).

## Getting started with sap_middleware_rfc

**Note:** The package must be [installed](#installation) before use.

In order to call remote enabled ABAP, first lets configure the connection properties of SAP.

```shell
cd sap_middleware_rfc/sap
nano sapnwrfc.cfg

[connection]
# sap system ip
ashost = 
# sap client id
client = 300
# sap router string, optional, format like /H/x.x.x.x/...
saprouter =
# sap system number
sysnr = 00
# sap username
#user = aeabap01
user = 
# sap password
#passwd = aeabap01
passwd = 


[gateway]
# gateway host name
gwhost = 
# gateway server name
ghserv = 
# name under which the python connector will register itself
program_id = PYRFC_APISERVER
# sap router string, optional
saprouter =
```

Once configured, lets accomplish a sync test of invoking:

```python
>>> from sap_adapter import RFC
```

```python
>>> inputs = {
    'REQUTEXT' = 'Hello SAP!'
}
>>> result = RFC().invoke_func('STFC_CONNECTION', inputs)
>>> print(result)
{u'ECHOTEXT': u'Hello SAP!',
 u'RESPTEXT': u'SAP R/3 Rel. 702   Sysid: ABC   Date: 20121001   Time: 134524   Logon_Data: 100/ME/E'}
```
Finally, the connection is closed automatically when the instance is deleted by the garbage collector.

## REST Client

You might want to use the server project builtin for invoke SAP/RFC results direct from REST service:

![](https://raw.githubusercontent.com/ramonlimaramos/sap_middleware_rfc/master/examples/img1_rest.png)

![](https://github.com/ramonlimaramos/sap_middleware_rfc/raw/master/examples/%20img2_rest.png)

The application will return a JSON as response.

For more information related to PyRFC see also the the [pyrfc documentation](http://sap.github.io/PyRFC),
complementing _SAP NW RFC SDK_ [documentation](https://support.sap.com/nwrfcsdk).


## Credits

Copyright (c) 2013 SAP SE or an SAP affiliate company. All rights reserved. This file is licensed under the Apache Software License, v. 2 except as noted otherwise in the [LICENSE](LICENSE) file.