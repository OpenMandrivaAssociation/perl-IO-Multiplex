%define	upstream_name	 IO-Multiplex
%define	upstream_version 1.13

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Manage IO on many file handles
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:	perl-devel >= 5.005
%endif
BuildRequires:	perl(IO::Socket)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
IO::Multiplex is designed to take the effort out of managing
multiple file handles.  It is essentially a really fancy front end to
the C<select> system call.  In addition to maintaining the C<select>
loop, it buffers all input and output to/from the file handles.  It
can also accept incoming connections on one or more listen sockets.

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
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/IO
%{_mandir}/man*/*
