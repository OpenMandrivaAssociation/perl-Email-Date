%define upstream_name    Email-Date
%define upstream_version 1.103

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Find and Format Date Headers
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Email/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(Email::Abstract)
BuildRequires:  perl(Email::Date::Format)
BuildRequires:  perl(Date::Parse)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

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
