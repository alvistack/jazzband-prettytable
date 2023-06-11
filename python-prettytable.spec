# Copyright 2023 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-prettytable
Epoch: 100
Version: 3.7.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Display tabular data in a visually appealing ASCII table format
License: BSD-2-Clause
URL: https://github.com/jazzband/prettytable/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
PrettyTable is a Python library for representing tabular data in ASCII
tables, inspired by the tables emitted by the PostgreSQL shell, psql.
PrettyTable allows for selection of which columns are to be printed,
independent alignment of columns (left or right justified or centred)
and printing of "sub-tables" by specifying a row range.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-prettytable
Summary: Display tabular data in a visually appealing ASCII table format
Requires: python3
Requires: python3-importlib-metadata
Requires: python3-wcwidth
Provides: python3-PrettyTable = %{epoch}:%{version}-%{release}
Provides: python3-prettytable = %{epoch}:%{version}-%{release}
Provides: python3dist(prettytable) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-prettytable = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(prettytable) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-prettytable = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(prettytable) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-prettytable
PrettyTable is a Python library for representing tabular data in ASCII
tables, inspired by the tables emitted by the PostgreSQL shell, psql.
PrettyTable allows for selection of which columns are to be printed,
independent alignment of columns (left or right justified or centred)
and printing of "sub-tables" by specifying a row range.

%files -n python%{python3_version_nodots}-prettytable
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-PrettyTable
Summary: Display tabular data in a visually appealing ASCII table format
Requires: python3
Requires: python3-importlib-metadata
Requires: python3-wcwidth
Provides: python3-PrettyTable = %{epoch}:%{version}-%{release}
Provides: python3-prettytable = %{epoch}:%{version}-%{release}
Provides: python3dist(prettytable) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-prettytable = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(prettytable) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-prettytable = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(prettytable) = %{epoch}:%{version}-%{release}

%description -n python3-PrettyTable
PrettyTable is a Python library for representing tabular data in ASCII
tables, inspired by the tables emitted by the PostgreSQL shell, psql.
PrettyTable allows for selection of which columns are to be printed,
independent alignment of columns (left or right justified or centred)
and printing of "sub-tables" by specifying a row range.

%files -n python3-PrettyTable
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-prettytable
Summary: Display tabular data in a visually appealing ASCII table format
Requires: python3
Requires: python3-importlib-metadata
Requires: python3-wcwidth
Provides: python3-PrettyTable = %{epoch}:%{version}-%{release}
Provides: python3-prettytable = %{epoch}:%{version}-%{release}
Provides: python3dist(prettytable) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-prettytable = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(prettytable) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-prettytable = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(prettytable) = %{epoch}:%{version}-%{release}

%description -n python3-prettytable
PrettyTable is a Python library for representing tabular data in ASCII
tables, inspired by the tables emitted by the PostgreSQL shell, psql.
PrettyTable allows for selection of which columns are to be printed,
independent alignment of columns (left or right justified or centred)
and printing of "sub-tables" by specifying a row range.

%files -n python3-prettytable
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
