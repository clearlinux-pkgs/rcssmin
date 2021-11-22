#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rcssmin
Version  : 1.1.0
Release  : 33
URL      : https://files.pythonhosted.org/packages/1e/e1/1386510c336541857aa28f8a0bb1514f15f557eb6037ddd61d1dd09c14ec/rcssmin-1.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/1e/e1/1386510c336541857aa28f8a0bb1514f15f557eb6037ddd61d1dd09c14ec/rcssmin-1.1.0.tar.gz
Summary  : CSS Minifier
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: rcssmin-license = %{version}-%{release}
Requires: rcssmin-python = %{version}-%{release}
Requires: rcssmin-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# rCSSmin - A CSS Minifier For Python
TABLE OF CONTENTS
-----------------
1. Introduction
1. System Requirements
1. Installation
1. Documentation
1. Bugs
1. Author Information

%package license
Summary: license components for the rcssmin package.
Group: Default

%description license
license components for the rcssmin package.


%package python
Summary: python components for the rcssmin package.
Group: Default
Requires: rcssmin-python3 = %{version}-%{release}

%description python
python components for the rcssmin package.


%package python3
Summary: python3 components for the rcssmin package.
Group: Default
Requires: python3-core
Provides: pypi(rcssmin)

%description python3
python3 components for the rcssmin package.


%prep
%setup -q -n rcssmin-1.1.0
cd %{_builddir}/rcssmin-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1637602307
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rcssmin
cp %{_builddir}/rcssmin-1.1.0/LICENSE %{buildroot}/usr/share/package-licenses/rcssmin/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/rcssmin-1.1.0/bench/LICENSE.cssmin %{buildroot}/usr/share/package-licenses/rcssmin/2c0343517b99ae17764c408b6313ea09d921a856
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rcssmin/2c0343517b99ae17764c408b6313ea09d921a856
/usr/share/package-licenses/rcssmin/7df059597099bb7dcf25d2a9aedfaf4465f72d8d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
