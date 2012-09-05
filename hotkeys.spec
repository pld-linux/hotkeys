Summary:	A program to use the special keys on internet/multimedia keyboards
Summary(pl.UTF-8):	Obsługa klawiszy specjalnych na internetowych/multimedialnych klawiaturach
Name:		hotkeys
Version:	0.5.7.1
Release:	6
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://ypwong.org/hotkeys/%{version}/%{name}_%{version}.tar.gz
# Source0-md5:	68e2aea6b4444f943b5f85ac00542a1c
Patch0:		%{name}-db41.patch
Patch1:		%{name}-libxml2.patch
Patch2:		%{name}-ac_am.patch
Patch3:		%{name}-home_etc.patch
URL:		http://ypwong.org/hotkeys/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db-devel >= 4.1
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libxml2-devel >= 2.2.8
BuildRequires:	pkgconfig >= 1:0.7
BuildRequires:	xosd-devel >= 0.7.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HotKeys daemon listens for the "special" hotkeys that you won't
normally use on your Internet/Multimedia keyboards. The buttons
perform their intended behaviors, such as volume up and down, mute the
speaker, or launch applications. It has On-screen display (OSD) to
show the volume, program that's being started, etc. It features an
XML-based keycode configuration file format, which makes it possible
to define the hotkeys to launch any programs you want.

%description -l pl.UTF-8
Demon HotKeys czeka na naciśnięcia "specjalnych" klawiszy, których
normalnie nie użyłbyś z klawiatur internetowych/multimedialnych.
Przyciski wykonują swoje zamierzone zadanie, takie jak zwiększanie i
zmniejszanie głośności, wyciszanie głośnika, uruchamianie programów.
Obsługuje OSD (On-screen display) do pokazywania głośności,
uruchamianych programów itp. Klawisze mogą być konfigurowane przez
plik formacie XML.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-xosd \
	--with-gtk \
	--with-x

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS TODO debian/changelog def/sample.xml
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/hotkeys.conf
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/*
