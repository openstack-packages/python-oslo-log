%{!?_licensedir:%global license %%doc}
%global pypi_name oslo.log

Name:           python-oslo-log
Version:        XXX
Release:        XXX
Summary:        OpenStack Oslo Log library

License:        ASL 2.0
URL:            http://launchpad.net/oslo
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr

Requires:       python-babel
Requires:       python-six >= 1.9.0
Requires:       python-iso8601
Requires:       python-oslo-config
Requires:       python-oslo-context
Requires:       python-oslo-i18n
Requires:       python-oslo-utils
Requires:       python-oslo-serialization
Requires:       python-debtcollector
Requires:       python-inotify

%description
OpenStack logging configuration library provides standardized configuration
for all openstack projects. It also provides custom formatters, handlers and
support for context specific logging (like resource id’s etc).

%package doc
Summary:    Documentation for the Oslo Log handling library

BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx
BuildRequires:  python-oslo-config
BuildRequires:  python-oslo-utils
BuildRequires:  python-oslo-context

%description doc
Documentation for the Oslo Log handling library.


%prep
%setup -q -n %{pypi_name}-%{upstream_version}
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
%doc README.rst ChangeLog AUTHORS
%license LICENSE
%{python2_sitelib}/oslo_log
%{python2_sitelib}/*.egg-info

%files doc
%doc html
%license LICENSE

%changelog
