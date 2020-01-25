#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Rose
%define	pnam	URI
Summary:	Rose::URI - A URI class that allows easy and efficient manipulation of URI components.
#Summary(pl.UTF-8):	
Name:		perl-Rose-URI
Version:	1.00
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Rose/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ea5a41a557435b03ddbf6cf7ad03cb03
URL:		http://search.cpan.org/dist/Rose-URI/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Rose-Object >= 0.015
BuildRequires:	perl-URI
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rose::URI is an alternative to URI.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Rose/*.pm
%{_mandir}/man3/*
