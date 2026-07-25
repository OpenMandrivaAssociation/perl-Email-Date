%define modname	Email-Date
%define modver 1.104

Summary:	Find and Format Date Headers
Name:		perl-%{modname}
Version:	%{modver}
Release:	10
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://github.com/rjbs/Email-Date
Source0:	https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-Date-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(Time::Piece)
BuildRequires:	perl(Capture::Tiny)
BuildRequires:	perl(Email::Abstract)
BuildRequires:	perl(Email::Date::Format)
BuildRequires:	perl(Date::Parse)
BuildRequires:	perl(Test::More)
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


