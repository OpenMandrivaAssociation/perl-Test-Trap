%define upstream_name    Test-Trap
%define upstream_version 0.2.4

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Trap exit codes, exceptions, output

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-v%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Data::Dump)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Test::Tester)
BuildRequires:	perl(version)

BuildArch:	noarch

%description
Primarily (but not exclusively) for use in test scripts: A block eval on
steroids, configurable and extensible, but by default trapping (Perl)
STDOUT, STDERR, warnings, exceptions, would-be exit codes, and return
values from boxed blocks of test code.

The values collected by the latest trap can then be queried or tested
through a special trap object.

%prep
%setup -q -n %{upstream_name}-v%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Test
%{_mandir}/*/*



