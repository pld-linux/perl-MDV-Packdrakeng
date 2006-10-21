#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	Packdrakeng
%define		pdir	MDV
Summary:	MDV::Packdrakeng - simple archive extractor/builder
Summary(pl):	MDV::Packdrakeng - prosta rozpakowywarka archiwów/builder
Name:		perl-MDV-Packdrakeng
Version:	1.01
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/R/RG/RGARCIA/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	08fa89a1908503a82abee649d7547f95
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with autodeps}
BuildRequires:	perl-Compress-Zlib
%endif
BuildRequires:	rpm-devel >= 4.2.3
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MDV::Packdrakeng is a simple indexed archive builder and extractor
using standard compression methods.

%description -l pl
MDV::Packdrakeng jest prostym builderem indeksowanych archiwów oraz
rozpakowywark± korzystaj±c± ze standardowych metod kompresji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%{perl_vendorlib}/MDV
