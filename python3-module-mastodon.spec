%define _unpackaged_files_terminate_build 1
%define pypi_name Mastodon.py

Name:           python3-module-mastodon
Version:        2.2.2
Release:        alt1
Summary:        Python wrapper for the Mastodon API
License:        MIT
Group:          Development/Python3
URL:            https://pypi.org/project/Mastodon.py
BuildArch:      noarch
Source:         mastodon_py-2.2.2.tar.gz

%global __arch_install_post %{nil}

Provides:       python3-module-%{pep503_name %pypi_name} = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-module-setuptools
BuildRequires:  python3-module-wheel

Requires:       python3-module-requests
Requires:       python3-module-dateutil
Requires:       python3-module-decorator
Requires:       python3-module-magic

%description
Mastodon.py is a Python wrapper for the Mastodon social networking API.
It provides a user-friendly interface for interacting with Mastodon servers.

%prep
%setup -q -n mastodon_py-2.2.2

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst
%python3_sitelibdir/mastodon/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Oct 06 2026 Anna Bespalova <anna_b03@mail.ru> 2.2.2-alt1
- Initial build for ALT Linux
