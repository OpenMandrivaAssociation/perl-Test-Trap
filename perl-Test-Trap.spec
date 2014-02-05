%define upstream_name    Test-Trap
%define upstream_version 0.2.3

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Trap exit codes, exceptions, output
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Test/Test-Trap-v%{upstream_version}.tar.gz

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


%changelog
* Wed Dec 30 2009 Jérôme Quelin <jquelin@mandriva.org> 0.2.1-1mdv2010.1
+ Revision: 483882
- update to v0.2.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.2.0-2mdv2010.0
+ Revision: 440698
- rebuild

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.0-1mdv2009.1
+ Revision: 292354
- update to new version 0.2.0

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.1.1-2mdv2009.0
+ Revision: 268755
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.1-1mdv2009.0
+ Revision: 194953
- update to new version 0.1.1

* Tue Jan 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.0-1mdv2008.1
+ Revision: 156642
- new version

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.0.21-1mdv2008.1
+ Revision: 140721
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Mar 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.0.21-1mdv2007.1
+ Revision: 146403
- spec cleanup

* Sun Mar 18 2007 Shlomi Fish 0.0.21-1mdv2007.1
- Initial release. Adapted the XML-Atom spec for this one.



