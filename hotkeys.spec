Summary:	A program to use the special keys on internet/multimedia keyboards.
Name:		hotkeys
Version:	0.5.4
Release:	0
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://ypwong.org/hotkeys/%{name}_%{version}.tar.gz
URL:		http://ypwong.org/hotkeys/
BuildRequires:	xosd-devel
BuildRequires:	libxml-devel
BuildRequires:	db2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HotKeys daemon listens for the "special" hotkeys that you won't
normally use on your Internet/Multimedia keyboards. The buttons
perform their intended behaviors, such as volume up and down, mute the
speaker, or launch applications. It has On-screen display (OSD) to
show the volume, program that's being started, etc. It features an
XML-based keycode configuration file format, which makes it possible
to define the hotkeys to launch any programs you want.

%prep
%setup -q -n %{name}-%{version}

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS COPYING INSTALL TODO def/sample.xml debian/changelog
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man*/*
