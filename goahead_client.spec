#
# spec file for package goahead_client
#
# -- Copyright omitted --

Name:           goahead_client
Version:        0.0.2
Release:        0
License:        Apache-2.0
Group:          System/Monitoring
Summary:        Client for Goahead, a simple service that allows or denies server / OS restarts
Url:            https://github.com/jlalvarez-arsys/goahead_client
Source0:         goahead-%{version}.tar.gz
Source1:         vendor.tar.gz
%if 0%{?suse_version}
BuildRequires:  (go or go1.19)
%else
BuildRequires:  (go or go1.19)
%endif

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Client for Goahead. A simple service that allows or denies server / OS restarts

%prep
%setup -q -n %{name}-%{version}
# unpack Source1 after changing directory
%setup -q -a 1

%build
go build -mod=vendor -o %{name}

%install
install -D -m 0755 %{name} "%{buildroot}/usr/bin/%{name}"

%files
%defattr(-,root,root,-)
%doc README.md LICENSE
%{_bindir}/*

%changelog
