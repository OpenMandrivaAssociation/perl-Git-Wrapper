%define upstream_name    Git-Wrapper
%define upstream_version 0.031
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Wrap git(7) command-line interface
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Git/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	git
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::pushd)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Most)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Sort::Versions)
BuildRequires:	perl(Env::Path)

BuildArch:	noarch

Requires: git

%description
Git::Wrapper provides an API for git(7) that uses Perl data structures for
argument passing, instead of CLI-style '--options' as the Git manpage does.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
git config --global user.email "John@smith.org"
git config --global user.name "John Smith"
%make test

%install
%makeinstall_std

%files
%doc Changes 
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.14.0-2mdv2011.0
+ Revision: 657071
- fix check
- rebuild for updated spec-helper

* Sun Nov 14 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.14.0-1mdv2011.0
+ Revision: 597581
- update to new version 0.014

* Fri Nov 12 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.13.0-1mdv2011.0
+ Revision: 596526
- update to new version 0.013

* Fri Jul 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.11.0-1mdv2011.0
+ Revision: 553960
- update to 0.011

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2011.0
+ Revision: 552312
- update to 0.010

* Mon Mar 22 2010 Jérôme Quelin <jquelin@mandriva.org> 0.8.0-1mdv2010.1
+ Revision: 526443
- update to 0.008

* Mon Nov 16 2009 Jérôme Quelin <jquelin@mandriva.org> 0.7.0-1mdv2010.1
+ Revision: 466506
- adding missing buildrequires:
- adding missing buildrequires + requires
- import perl-Git-Wrapper


* Mon Nov 16 2009 cpan2dist 0.007-1mdv
- initial mdv release, generated with cpan2dist




