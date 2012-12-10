Summary:	Simple GUI for MPlayer
Name:		gnome-mplayer
Version:	1.0.7
Release:	%mkrel 1
License:	GPLv2+
Group:		Video
URL:		http://kdekorte.googlepages.com/gnomemplayer
Source0:	http://gnome-mplayer.googlecode.com/files/%name-%version.tar.gz
Requires:	mplayer
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gmtk) >= 1.0.7
BuildRequires:	pkgconfig(dbus-1) >= 0.95
BuildRequires:	pkgconfig(dbus-glib-1) >= 0.70
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libgpod-1.0)
BuildRequires:	pkgconfig(libmusicbrainz3)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libnautilus-extension)
BuildRequires:	desktop-file-utils
# Used to determine volume control mode at build-time
BuildRequires:	pkgconfig(libpulse)
# Used to determine power control methods at build-time
BuildRequires:	gnome-power-manager

%description
GNOME MPlayer is a simple GUI for MPlayer. It is intended to be a
nice tight player and provide a simple and clean interface to
MPlayer. GNOME MPlayer has a rich API that is exposed via DBus.
Using DBus you can control a single or multiple instances of GNOME
MPlayer from a single command.

%prep
%setup -q

%build
%configure2_5x --enable-gtk3
%make

%install
%makeinstall_std

desktop-file-install --vendor='' \
	--add-category="Audio;Video;GTK;Player;GNOME" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*.desktop

# zero length docs
find %{buildroot}%{_docdir}/%{name}/ -size 0 | xargs rm -f

%find_lang %{name}

%files -f %{name}.lang
%doc %{_docdir}/%{name}/*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_datadir}/glib-2.0/schemas/apps.gecko-mediaplayer.preferences.gschema.xml
%{_datadir}/glib-2.0/schemas/apps.gnome-mplayer.preferences.*.xml
%{_datadir}/gnome-control-center/default-apps/gnome-mplayer.xml
%{_libdir}/nautilus/extensions*/*.so
%{_mandir}/man1/%{name}.1*
