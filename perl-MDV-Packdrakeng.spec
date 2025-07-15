#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%define		pnam	Packdrakeng
%define		pdir	MDV
Summary:	MDV::Packdrakeng - simple archive extractor/builder
Summary(pl.UTF-8):	MDV::Packdrakeng - prosta rozpakowywarka archiwów/builder
Name:		perl-MDV-Packdrakeng
Version:	1.13
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/N/NA/NANARDON/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8dc16111304c486557ec94e26e8fa86c
Patch0:		%{name}-xz.patch
URL:		http://search.cpan.org/dist/MDV-Packdrakeng/
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

%description -l pl.UTF-8
MDV::Packdrakeng jest prostym builderem indeksowanych archiwów oraz
rozpakowywarką korzystającą ze standardowych metod kompresji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p1

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
