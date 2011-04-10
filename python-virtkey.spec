Summary:	Python extension for emulating keypresses and getting layout information from the X server
Name:		python-virtkey
Version:	0.60.0
Release:	1
License:	LGPL v3
Group:		Development/Languages/Python
Source0:	http://launchpad.net/python-virtkey/0.60/0.60.0/+download/%{name}-%{version}.tar.gz
# Source0-md5:	f4f6776f379bc635a29eac83a14fdde5
URL:		http://launchpad.net/python-virtkey
BuildRequires:	gtk+2-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
python-virtkey is a python extension for emulating keypresses and
getting layout information from the X server.

%prep
%setup -q

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{py_sitedir}/virtkey.so
%if "%{py_ver}" > "2.4"
%{py_sitedir}/python_virtkey-*.egg-info
%endif
