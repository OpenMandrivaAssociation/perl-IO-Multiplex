%define	upstream_name	 IO-Multiplex
%define	upstream_version 1.13

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Manage IO on many file handles
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(IO::Socket)
BuildArch:	noarch

%description
IO::Multiplex is designed to take the effort out of managing
multiple file handles.  It is essentially a really fancy front end to
the C<select> system call.  In addition to maintaining the C<select>
loop, it buffers all input and output to/from the file handles.  It
can also accept incoming connections on one or more listen sockets.

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
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/IO
%{_mandir}/man*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.130.0-4mdv2012.0
+ Revision: 765370
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.130.0-3
+ Revision: 763872
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 1.130.0-2
+ Revision: 763082
- rebuild

* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.130.0-1
+ Revision: 654091
- update to new version 1.13

* Thu Feb 24 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.120.0-1
+ Revision: 639640
- update to new version 1.12

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.100.0-1mdv2010.1
+ Revision: 402557
- rebuild using %%perl_convert_version

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.10-1mdv2009.1
+ Revision: 292185
- update to new version 1.10

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.09-3mdv2009.0
+ Revision: 223796
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.09-2mdv2008.1
+ Revision: 180411
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 1.09-1mdv2008.0
+ Revision: 20228
- 1.09


* Sun Sep 03 2006 Scott Karns <scottk@mandriva.org> 1.08-2mdv2007.0
- Fix BuildRequires
- Fix file ownership

* Wed Jun 02 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.08-1mdk
- 1.08
- fix perms

* Thu Sep 04 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.07-1mdk
- needed by perl-Net-Server

