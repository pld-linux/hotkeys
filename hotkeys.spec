# TODO:
# - some cleanups
# - replace manual linking in configure with some nice way
# - really fix ac/am suite
Summary:	A program to use the special keys on internet/multimedia keyboards
Summary(pl):	Program do wykorzystania specjalnych klawiszy na internetowych/multimedialnych klawiaturach
Name:		hotkeys
Version:	0.5.7.1
Release:	0.9
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://ypwong.org/hotkeys/%{version}/%{name}_%{version}.tar.gz
# Source0-md5:	68e2aea6b4444f943b5f85ac00542a1c
URL:		http://ypwong.org/hotkeys/
BuildRequires:	xosd-devel
BuildRequires:	libxml2-devel >= 2.2.8
BuildRequires:	db4-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HotKeys daemon listens for the "special" hotkeys that you won't
normally use on your Internet/Multimedia keyboards. The buttons
perform their intended behaviors, such as volume up and down, mute the
speaker, or launch applications. It has On-screen display (OSD) to
show the volume, program that's being started, etc. It features an
XML-based keycode configuration file format, which makes it possible
to define the hotkeys to launch any programs you want.

%description -l pl
Demon HotKeys czeka na naci¶niêcia "specjalnych" klawiszy, których
normalnie nie u¿y³by¶ z klawiatur internetowych/multimedialnych.
Przyciski wykonuj± swoje zamierzone zadanie, takie jak zwiêkszanie i
zmniejszanie g³o¶no¶ci, wyciszanie g³o¶nika, uruchamianie programów.
Obs³uguje OSD (On-screen display) do pokazywania g³o¶no¶ci,
uruchamianych programów itp. Klawisze mog± byæ konfigurowane przez
plik formacie XML.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	CFLAGS="%{rpmcflags} -I/usr/include/libxml2/libxml -I/usr/include/libxml2" \
	LDFLAGS="-lxml2 -ldb4" \
	--with-db3-inc=/usr/include/db4 \
	--disable-db3test \
	--with-xml-exec-prefix=/usr 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
#%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS TODO debian/changelog def/sample.xml
%attr(644,root,root) %config(noreplace) /etc/hotkeys.conf
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man*/*
