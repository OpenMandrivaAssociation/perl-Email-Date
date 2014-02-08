%define upstream_name    Email-Date
%define upstream_version 1.103

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Find and Format Date Headers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Email/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Time::Piece)
BuildRequires:	perl(Email::Abstract)
BuildRequires:	perl(Email::Date::Format)
BuildRequires:	perl(Date::Parse)
BuildRequires:	perl-devel

BuildArch:	noarch


%description
RFC 2822 defines the Date: header. It declares the header a required part of an
email message. The syntax for date headers is clearly laid out. Stil, even a
perfectly planned world has storms. The truth is, many programs get it wrong.
Very wrong. Or, they don't include a Date: header at all. This often forces you
to look elsewhere for the date, and hoping to find something.

For this reason, the tedious process of looking for a valid date has been
encapsulated in this software. Further, the process of creating RFC compliant
date strings is also found in this software.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Email
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.103.0-4mdv2012.0
+ Revision: 765194
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.103.0-2
+ Revision: 667125
- mass rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.103.0-1mdv2010.1
+ Revision: 403156
- rebuild using %%perl_convert_version

* Mon Aug 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.10.3-1mdv2009.0
+ Revision: 270912
- new version

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.10.2-3mdv2009.0
+ Revision: 223663
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.10.2-2mdv2008.1
+ Revision: 180393
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Jul 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.10.2-1mdv2008.0
+ Revision: 48062
- update to new version 1.102


* Sun Jan 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.10.1-1mdv2007.0
+ Revision: 111316
- fix build dependencies
- Import perl-Email-Date

* Sun Jan 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.10.1-1mdv2007.1
- first mdv release

