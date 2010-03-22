%define upstream_name    Git-Wrapper
%define upstream_version 0.008

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Wrap git(7) command-line interface
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Git/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: git
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::pushd)
BuildRequires: perl(Test::Deep)
BuildRequires: perl(Test::More)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

Requires: git

%description
Git::Wrapper provides an API for git(7) that uses Perl data structures for
argument passing, instead of CLI-style '--options' as the Git manpage does.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


