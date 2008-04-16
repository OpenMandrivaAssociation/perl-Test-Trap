%define module  Test-Trap
%define name    perl-%{module}
%define version 0.1.1
%define release %mkrel 1

Name:               %{name}
Version:            %{version}
Release:            %{release}
Summary:            Perl Module for Processing Atom Feeds
License:            GPL or Artistic
Group:              Development/Perl
Url:                http://search.cpan.org/dist/%{module}/
Source:             http://www.cpan.org/modules/by-module/Test/%{module}-%{version}.tar.gz
BuildRequires:      perl(Test::Tester)
BuildRequires:      perl(File::Temp)
BuildRequires:      perl(Data::Dump)
BuildRequires:      perl-version
BuildArch:          noarch
BuildRoot:          %{_tmppath}/%{name}-%{version}

%description
Perl Module for processing Atoms feed and that provides access to the Atom
API.

%prep
%setup -q -n %{module}-%{version}

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


