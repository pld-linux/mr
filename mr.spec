Summary:	Command line tool for managing multiple repositories
Name:		mr
Version:	1.15
Release:	0.1
License:	GPL/GPL v2
Group:		Applications/Console
Source0:	ftp://ftp.debian.org/debian/pool/main/m/mr/%{name}_%{version}.tar.gz
# Source0-md5:	719ec056d7b9e2e5c9501d4f1ba19122
URL:		http://joeyh.name/code/mr/
Requires:	git-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The mr command can checkout, update, or perform other actions on a set
of repositories as if they were one combined respository. It supports
any combination of subversion, git, cvs, mercurial, bzr, darcs, cvs,
vcsh, fossil and veracity repositories.

%prep
%setup -q -n %{name}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -p mr $RPM_BUILD_ROOT%{_bindir}
cp -p mr.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
