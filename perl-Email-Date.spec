%define modname	Email-Date
%define modver	1.103

Summary:	Find and Format Date Headers
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	8
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Email/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Time::Piece)
BuildRequires:	perl(Email::Abstract)
BuildRequires:	perl(Email::Date::Format)
BuildRequires:	perl(Date::Parse)
BuildRequires:	perl-devel

%description
RFC 2822 defines the Date:	header. It declares the header a required part of an
email message. The syntax for date headers is clearly laid out. Stil, even a
perfectly planned world has storms. The truth is, many programs get it wrong.
Very wrong. Or, they don't include a Date:	header at all. This often forces you
to look elsewhere for the date, and hoping to find something.

For this reason, the tedious process of looking for a valid date has been
encapsulated in this software. Further, the process of creating RFC compliant
date strings is also found in this software.

%prep
%setup -qn %{modname}-%{modver}

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
%{_mandir}/man3/*

