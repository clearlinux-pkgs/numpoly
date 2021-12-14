#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : numpoly
Version  : 1.2.3
Release  : 2
URL      : https://files.pythonhosted.org/packages/37/10/96ccf9b0ba76b552939cd9f2be478b8b03b1160f33cde0f840e9cadf0f9e/numpoly-1.2.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/37/10/96ccf9b0ba76b552939cd9f2be478b8b03b1160f33cde0f840e9cadf0f9e/numpoly-1.2.3.tar.gz
Summary  : Polynomials as a numpy datatype
Group    : Development/Tools
License  : BSD-2-Clause
Requires: numpoly-python = %{version}-%{release}
Requires: numpoly-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry)

%description
.. image:: https://github.com/jonathf/numpoly/raw/master/docs/.static/numpoly_logo.svg
:height: 200 px
:width: 200 px
:align: center

%package python
Summary: python components for the numpoly package.
Group: Default
Requires: numpoly-python3 = %{version}-%{release}

%description python
python components for the numpoly package.


%package python3
Summary: python3 components for the numpoly package.
Group: Default
Requires: python3-core
Provides: pypi(numpoly)
Requires: pypi(numpy)

%description python3
python3 components for the numpoly package.


%prep
%setup -q -n numpoly-1.2.3
cd %{_builddir}/numpoly-1.2.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1638316314
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
