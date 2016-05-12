Name:           vdpauinfo
Version:        1.0
Release:        1%{?dist}
Summary:        Tool to query the capabilities of a VDPAU implementation

License:        MIT
URL:            http://freedesktop.org/wiki/Software/VDPAU
Source0:        http://people.freedesktop.org/~aplattner/vdpau/vdpauinfo-%{version}.tar.gz

BuildRequires:  libvdpau-devel


%description
Tool to query the capabilities of a VDPAU implementation.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install


%files
%doc ChangeLog COPYING
%{_bindir}/vdpauinfo


%changelog
* Thu May 12 2016 Jajauma's Packages <jajauma@yandex.ru> - 1.0-1
- Public release
