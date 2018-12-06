# http://github.com/mreiferson/go-httpclient

%global goipath         github.com/mreiferson/go-httpclient
%global commit          c121dfe45d66997e43e25a6823fbe7466c8403fe


%gometa -i

Name:           golang-github-mreiferson-go-httpclient
Version:        0
Release:        0.12%{?dist}
Summary:        A Go HTTP client library
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description

can be used as a built in replacement for the standard librarys.

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml

%check
%gochecks -d .

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.11.gitc121dfe
- Upload glide files

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gitc121dfe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gitc121dfe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gitc121dfe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.gitc121dfe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.gitc121dfe
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.gitc121dfe
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gitc121dfe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Aug 07 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.3.gitc121dfe
- Update spec file to spec-2.0
  resolves: #1250495

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.gitc121dfe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Sep 19 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.1.gitc121dfe
- main package doesn't need arch specification, only devel package generated
- comment out test

* Thu Jul 17 2014 Colin Walters <walters@verbum.org> - 0-0.0gitc121dfe
- Initial package
