%define short_name selftest

Summary:	Narval selftest module
Summary(pl):	Modu³ testowy dla Narvala
Name:		Narval-%{short_name}
Version:	20011016
Release:	1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.logilab.org/pub/narval/applications/%{short_name}-%{version}.npm
# Source0-md5:	8eafb69ffc27f2bac9136f8f7475be43
URL:		http://www.logilab.org/narval/app.html
Requires:	Narval
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Selftest is the test module for Narval.
It provides the actions and transformations necessary to run the
validation tests for the Narval kernel.

%description -l pl
Selftest to modu³ testuj±cy dla Narvala.
Dostarcza dzia³añ i przekszta³ceñ koniecznych do wykonania testów
poprawno¶ci kernela Narvala.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -D %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/narval/apps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/narval/apps/*
