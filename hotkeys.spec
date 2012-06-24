Summary:	A program to use the special keys on internet/multimedia keyboards
Summary(pl):	Program do wykorzystania specjalnych klawiszy na internetowych/multimedialnych klawiaturach
Name:		hotkeys
Version:	0.5.4
Release:	0
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://ypwong.org/hotkeys/%{name}_%{version}.tar.gz
# Source0-md5:	50810778bf50c769a39cd44ba59fd14a
URL:		http://ypwong.org/hotkeys/
BuildRequires:	xosd-devel
BuildRequires:	libxml-devel
BuildRequires:	db2-devel >= 2.7.7
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
Demon HotKeys czeka na naci�ni�cia "specjalnych" klawiszy, kt�rych
normalnie nie u�y�by� z klawiatur internetowych/multimedialnych.
Przyciski wykonuj� swoje zamierzone zadanie, takie jak zwi�kszanie i
zmniejszanie g�o�no�ci, wyciszanie g�o�nika, uruchamianie program�w.
Obs�uguje OSD (On-screen display) do pokazywania g�o�no�ci,
uruchamianych program�w itp. Klawisze mog� by� konfigurowane przez
plik formacie XML.

%prep
%setup -q -n %{name}-%{version}

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS TODO debian/changelog def/sample.xml
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man*/*
