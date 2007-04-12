%define	module	IO-Multiplex
%define	name	perl-%{module}
%define	version	1.08
%define	release	%mkrel 2
%define	pdir	IO

Summary:	Manage IO on many file handles
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel >= 5.005
%endif
BuildRequires:	perl(IO::Socket)
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

%description
IO::Multiplex is designed to take the effort out of managing
multiple file handles.  It is essentially a really fancy front end to
the C<select> system call.  In addition to maintaining the C<select>
loop, it buffers all input and output to/from the file handles.  It
can also accept incoming connections on one or more listen sockets.


%prep
%setup -q -n %{module}-%{version}

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
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/%{pdir}
%{_mandir}/man*/*

