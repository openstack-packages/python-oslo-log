# Created by pyp2rpm-1.1.0b
%global pypi_name oslo.log

Name:           python-oslo-log
Version:        XXX
Release:        XXX{?dist}
Summary:        OpenStack Oslo Log library

License:        ASL 2.0
URL:            http://launchpad.net/oslo
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr

Requires:       python-babel
Requires:       python-six
Requires:       python-iso8601
Requires:       python-oslo-config
Requires:       python-oslo-context
Requires:       python-oslo-i18n
Requires:       python-oslo-utils
Requires:       python-oslo-serialization

%description
The OpenStack Oslo Log library.
* Source: http://git.openstack.org/cgit/openstack/oslo.log
* Bugs: http://bugs.launchpad.net/oslo


%package doc
Summary:    Documentation for the Oslo Log handling library
Group:      Documentation

BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx

%description doc
Documentation for the Oslo Log handling library.


%prep
%setup -q -n %{pypi_name}-%{upstream_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Let RPM handle the dependencies
rm -f requirements.txt


%build
%{__python2} setup.py build

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%files
%doc README.rst LICENSE
%{python2_sitelib}/oslo_log
%{python2_sitelib}/*.egg-info

%files doc
%doc html LICENSE

%changelog
* Tue Feb 17 2015 Derek Higgins <derekh@redhat.com> XXX
- Initial package.
