%include	/usr/lib/rpm/macros.perl
Summary:	Adds height= and width= to images referenced in specified HTML file
Name:		wwwis
Version:	2.44
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://wtwf.com/%{name}/wwwis
# Source0-md5:	469c5247cd30dd23466d5ecab8026a82
URL:		http://wtwf.com/wwwis/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sed >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WWWis is a Perl application which will read in an HTML file and insert
height=### width=### directives into the inlined images used in the
file. It also does a whole lot more to boot.

%prep
%setup -qcT
install %{SOURCE0} .
sed -i -e '1,/bin\/perl/d' wwwis
sed -i -e '1i#!/usr/bin/perl -w' wwwis

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install wwwis $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wwwis
