%define short_name selftest

Summary:	Narval selftest module
Summary(pl):	Modu³ testowy dla Narvala
Name:		Narval-%{short_name}
Version:	20011016
Release:	1
Source0:	ftp://ftp.logilab.org/pub/narval/applications/%{short_name}-%{version}.npm
License:	GPL
Group:		Applications
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	Narval
Url:		http://www.logilab.org/narval/app.html

%description
selftest is the test module for Narval.

It provides the actions and transformations necessary to run the
validation tests for the Narval kernel.

%description -l pl
selftest to modu³ testuj±cy dla Narvala.

Dostarcza dzia³añ i przekszta³ceñ koniecznych do wykonania testów
poprawno¶ci kernela Narvala.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_datadir}/narval/apps
install %{SOURCE0} $RPM_BUILD_ROOT/%{_datadir}/narval/apps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/narval/apps/*
