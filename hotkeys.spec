Summary: A program to use the special keys on internet/multimedia keyboards.
Name: hotkeys
Version: 0.5.2
Release: 1
Serial: 1
Copyright: GPL
Group: Applications/System
Source: http://ypwong.org/hotkeys/%{name}_%{version}.tar.gz
URL: http://ypwong.org/hotkeys/
BuildRoot: %{_tmppath}/%{name}-root
Requires: xosd, libxml
BuildRequires: xosd, db2-devel, libxml-devel

%description
The HotKeys daemon listens for the "special" hotkeys that you won't
normally use on your Internet/Multimedia keyboards. The buttons
perform their intended behaviors, such as volume up and down, mute the
speaker, or launch applications.  It has On-screen display (OSD) to
show the volume, program that's being started, etc.  It features an
XML-based keycode configuration file format, which makes it possible
to define the hotkeys to launch any programs you want.

%prep
%setup -q -n %{name}-%{version}

%build
%configure
make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS BUGS COPYING INSTALL TODO def/sample.xml debian/changelog
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man*/*

%changelog
* Thu Feb  8 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.5

* Sat Feb  3 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.4

* Sat Jan 20 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Initial spec file.
