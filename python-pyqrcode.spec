Name:		python-pyqrcode
Version:	1.2.1
Release:	2
Summary:	A QR code generator written purely in Python with SVG, EPS, PNG and
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://pypi.org/project/pyqrcode/
Source0:	PyQRCode-1.2.1.zip
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch
%description
A QR code generator written purely in Python with SVG, EPS, PNG and.

%files
%{py_sitedir}/*
