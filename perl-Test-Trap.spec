%define module  Test-Trap
%define name    perl-%{module}
%define version 0.0.21
%define release %mkrel 1

Name:               %{name}
Version:            %{version}
Release:            %{release}
Summary:            Perl Module for Processing Atom Feeds
License:            GPL or Artistic
Group:              Development/Perl
Url:                http://search.cpan.org/dist/%{module}/
Source:             http://www.cpan.org/modules/by-module/Test/%{module}-v%{version}.tar.bz2
BuildRequires:      perl(Test::Tester)
BuildRequires:      perl(File::Temp)
BuildRequires:      perl(Data::Dump)
BuildRequires:      perl-version
BuildArch:          noarch

%description
Perl Module for processing Atoms feed and that provides access to the Atom
API.

%prep
%setup -q -n %{module}-v%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Test
%{_mandir}/*/*


