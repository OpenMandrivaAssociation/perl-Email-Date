%define module      Email-Date
%define name        perl-%{module}
%define version     1.10.2
%define up_version  1.102
%define release     %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Find and Format Date Headers
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Email/%{module}-%{up_version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(Email::Abstract)
BuildRequires:  perl(Date::Parse)
BuildArch:      noarch

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
%setup -q -n %{module}-%{up_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Email
%{_mandir}/*/*


