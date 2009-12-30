%define upstream_name    Test-Trap
%define upstream_version v0.2.1

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Trap exit codes, exceptions, output
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:      perl(Data::Dump)
BuildRequires:      perl(File::Temp)
BuildRequires:      perl(Test::Tester)
BuildRequires:      perl(version)

BuildArch:          noarch
BuildRoot:          %{_tmppath}/%{name}-%{version}-%{release}

%description
Primarily (but not exclusively) for use in test scripts: A block eval on
steroids, configurable and extensible, but by default trapping (Perl)
STDOUT, STDERR, warnings, exceptions, would-be exit codes, and return
values from boxed blocks of test code.

The values collected by the latest trap can then be queried or tested
through a special trap object.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
