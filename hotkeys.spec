Summary:	A program to use the special keys on internet/multimedia keyboards
Summary(pl):	Program do wykorzystania specjalnych klawiszy na internetowych/multimedialnych klawiaturach
Name:		hotkeys
Version:	0.5.4
Release:	0
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://ypwong.org/hotkeys/%{name}_%{version}.tar.gz
URL:		http://ypwong.org/hotkeys/
BuildRequires:	xosd-devel
BuildRequires:	libxml-devel
BuildRequires:	db2-devel >= 2.7.7
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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
%setup -q -n %{name}-%{version}

%build
aclocal
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

gzip -9nf AUTHORS BUGS TODO debian/changelog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz def/sample.xml debian/changelog.gz
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man*/*
