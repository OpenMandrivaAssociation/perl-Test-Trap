%define upstream_name    Test-Trap
Name:		perl-%{upstream_name}
Version:	0.3.5
Release:	1

Summary:	Trap exit codes, exceptions, output

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-v%{version}.tar.gz

BuildRequires:	make
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
%setup -q -n Test-Trap-v0.3.5

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



