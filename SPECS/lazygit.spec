%define debug_package %{nil}

%global gh_user     jesseduffield
%global gh_commit   02bf6a5c177c145c46e5e62524458fc3375d01af
%global gh_short    %(c=%{gh_commit}; echo ${c:0:7})
%global gh_version  0.31.4

# see https://fedoraproject.org/wiki/PackagingDrafts/Go#Build_ID
%global _dwz_low_mem_die_limit 0

Name:           lazygit
Version:        0.42.0
Release:        1%{?dist}
Summary:        A simple terminal UI for git commands, written in Go with the gocui library
Group:          Applications/System
License:        MIT
URL:            https://github.com/%{gh_user}/%{name}
Source:         https://github.com/%{gh_user}/%{name}/archive/v%{gh_version}.tar.gz
BuildRequires:  git golang

%description
Are YOU tired of typing every git command directly into the terminal, but
you're too stubborn to use Sourcetree because you'll never forgive Atlassian
for making Jira? This is the app for you!

%prep
%setup -q -n %{name}-%{gh_version}

%build
export LDFLAGS="${LDFLAGS} -X main.commit=%{gh_short} -X main.date=$(date -u +%Y%m%d.%H%M%%S) -X main.version=%{version}"
go build -o %{_builddir}/bin/%{name}

%install
install -Dm0755 %{_builddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%doc LICENSE *.md docs/*.md

%changelog
* Tue Jun 25 2024 Jamie Curnow <jc@jc21.com> 0.42.0-1
- v0.42.0

* Tue Nov 30 2021 Jamie Curnow <jc@jc21.com> 0.31.4-1
- v0.31.4

* Wed Nov 10 2021 Jamie Curnow <jc@jc21.com> 0.31.3-1
- v0.31.3

* Tue Aug 24 2021 Jamie Curnow <jc@jc21.com> 0.29.0-1
- v0.29.0

* Fri Apr 9 2021 Jamie Curnow <jc@jc21.com> 0.27.2-1
- v0.27.2

* Thu Apr 8 2021 Jamie Curnow <jc@jc21.com> 0.27.1-1
- v0.27.1

* Wed Apr 7 2021 Jamie Curnow <jc@jc21.com> 0.27.0-1
- v0.27.0

* Sun Mar 14 2021 Jamie Curnow <jc@jc21.com> 0.26.1-1
- v0.26.1

* Sat Dec 26 2020 Jamie Curnow <jc@jc21.com> 0.24.2-1
- v0.24.2

* Fri Nov 6 2020 Jamie Curnow <jc@jc21.com> 0.23.7-1
- v0.23.7

* Thu Oct 15 2020 Jamie Curnow <jc@jc21.com> 0.23.6-1
- v0.23.6

* Mon Oct 12 2020 Jamie Curnow <jc@jc21.com> 0.23.2-1
- v0.23.2

* Fri Sep 18 2020 Jamie Curnow <jc@jc21.com> 0.22.6-1
- v0.22.6

* Mon Sep 7 2020 Jamie Curnow <jc@jc21.com> 0.22.1-1
- v0.22.1

* Fri Jul 24 2020 Jamie Curnow <jc@jc21.com> 0.20.9-1
- v0.20.9

* Tue Jul 14 2020 Jamie Curnow <jc@jc21.com> 0.20.8-1
- v0.20.8

* Mon Jul 13 2020 Jamie Curnow <jc@jc21.com> 0.20.6-1
- v0.20.6

* Wed May 20 2020 Jamie Curnow <jc@jc21.com> 0.20.4-1
- v0.20.4

* Fri May 15 2020 Jamie Curnow <jc@jc21.com> 0.20.3-1
- v0.20.3

* Thu Apr 23 2020 Jamie Curnow <jc@jc21.com> 0.20.2-1
- v0.20.2

* Tue Apr 21 2020 Jamie Curnow <jc@jc21.com> 0.20.0-1
- v0.20.0

* Mon Mar 30 2020 Jamie Curnow <jc@jc21.com> 0.19.0-1
- v0.19.0

* Fri Mar 27 2020 Jamie Curnow <jc@jc21.com> 0.18.0-1
- v0.18.0

* Tue Mar 24 2020 Jamie Curnow <jc@jc21.com> 0.17.4-1
- v0.17.4

* Thu Mar 19 2020 Jamie Curnow <jc@jc21.com> 0.17.0-1
- v0.17.0

* Wed Mar 4 2020 Jamie Curnow <jc@jc21.com> 0.16.0-1
- v0.16.0

* Mon Mar 2 2020 Jamie Curnow <jc@jc21.com> 0.15.7-1
- v0.15.7

* Wed Feb 26 2020 Jamie Curnow <jc@jc21.com> 0.15.3-1
- v0.15.3

* Mon Feb 24 2020 Jamie Curnow <jc@jc21.com> 0.15.2-1
- v0.15.2

* Thu Feb 20 2020 Jamie Curnow <jc@jc21.com> 0.14.4-1
- v0.14.4

* Fri Feb 7 2020 Jamie Curnow <jc@jc21.com> 0.14.3-1
- v0.14.3

* Fri Feb 7 2020 Jamie Curnow <jc@jc21.com> 0.14.2-1
- v0.14.2

* Fri Jan 10 2020 Jamie Curnow <jc@jc21.com> 0.13.0-1
- v0.13.0

* Thu Jan 9 2020 Jamie Curnow <jc@jc21.com> 0.12.3-1
- v0.12.3

* Wed Nov 27 2019 Jamie Curnow <jc@jc21.com> 0.11.3-1
- v0.11.3

* Mon Nov 25 2019 Jamie Curnow <jc@jc21.com> 0.11.2-1
- v0.11.2

* Thu Nov 14 2019 Jamie Curnow <jc@jc21.com> 0.10.6-1
- v0.10.6

* Wed Nov 13 2019 Jamie Curnow <jc@jc21.com> 0.10.5-1
- v0.10.5

* Tue Nov 12 2019 Jamie Curnow <jc@jc21.com> 0.10.4-1
- v0.10.4

* Mon Nov 11 2019 Jamie Curnow <jc@jc21.com> 0.10.2-1
- v0.10.2

* Tue Nov 5 2019 Jamie Curnow <jc@jc21.com> 0.9.0-1
- v0.9.0

* Mon Sep 16 2019 Jamie Curnow <jc@jc21.com> 0.8.2-1
- v0.8.2

* Mon Jun 24 2019 Jamie Curnow <jc@jc21.com> 0.8.1-1
- v0.8.1

* Mon May 13 2019 Jamie Curnow <jc@jc21.com> 0.8.0-1
- v0.8.0

* Wed Mar 6 2019 Jamie Curnow <jc@jc21.com> 0.7.2-1
- v0.7.2

* Mon Mar 4 2019 Jamie Curnow <jc@jc21.com> 0.7.1-1
- v0.7.1

* Mon Jan 21 2019 Jamie Curnow <jc@jc21.com> 0.6.0-1
- v0.6.0

* Wed Oct 24 2018 Jamie Curnow <jc@jc21.com> 0.5.0-1
- v0.5.0

* Thu Oct 11 2018 Jamie Curnow <jc@jc21.com> 0.4.0-1
- v0.4.0

* Mon Sep 24 2018 Jamie Curnow <jc@jc21.com> 0.3.1-1
- v0.3.1

* Fri Sep 21 2018 Jamie Curnow <jc@jc21.com> 0.3.0-1
- v0.3.0

* Tue Sep 11 2018 Jamie Curnow <jc@jc21.com> 0.2.2-1
- v0.2.2

* Wed Aug 29 2018 Jamie Curnow <jc@jc21.com> 0.2.1-1
- v0.2.1

* Mon Aug 27 2018 Jamie Curnow <jc@jc21.com> 0.1.80-1
- v0.1.80

* Mon Aug 20 2018 Jamie Curnow <jc@jc21.com> 0.1.73-1
- v0.1.73

* Fri Aug 17 2018 Jamie Curnow <jc@jc21.com> 0.1.64-1
- v0.1.64

* Thu Aug 16 2018 Jamie Curnow <jc@jc21.com> 0.1.61-1
- v0.1.61

* Mon Aug 13 2018 Jamie Curnow <jc@jc21.com> 0.1.55-1
- v0.1.55

* Fri Aug 10 2018 Robert Fuehricht <robert.fuehricht@jku.at> 0.1.48-1
- Version bump
- Proper escape of date format string for spec
- Removed dep as deps are vendored
- Adds documentation to package
- Use suggestions from Fedora's Go packaging guide

* Fri Aug 10 2018 Jamie Curnow <jc@jc21.com> 0.1.48-1
- v0.1.48

* Thu Aug 9 2018 Jamie Curnow <jc@jc21.com> 0.1.43-1
- v0.1.43

* Thu Aug 9 2018 Jamie Curnow <jc@jc21.com> 0.1.29-1
- v0.1.29

* Thu Aug 9 2018 Jamie Curnow <jc@jc21.com> 0.1.25-1
- v0.1.25 with commit hash

* Wed Aug 8 2018 Jamie Curnow <jc@jc21.com> 0.1.11-1
- Initial Spec File


