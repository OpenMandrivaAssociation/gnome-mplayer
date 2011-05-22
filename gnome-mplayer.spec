Summary:	Simple GUI for MPlayer
Name:		gnome-mplayer
Version:	1.0.3
Release:	%mkrel 1
License:	GPLv2+
Group:		Video
URL:		http://kdekorte.googlepages.com/gnomemplayer
Source:		http://gnome-mplayer.googlecode.com/files/%name-%version.tar.gz
Patch0:		gnome-mplayer-fix-str-fmt.patch
Requires:	mplayer
BuildRequires:	libgnome2-devel
BuildRequires:	gnomeui2-devel
BuildRequires:	dbus-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libmusicbrainz3-devel
BuildRequires:	libalsa-devel
BuildRequires:	curl-devel
BuildRequires:	libnotify-devel
BuildRequires:	libgpod-devel
BuildRequires:	nautilus-devel
BuildRequires:	libxscrnsaver-devel
BuildRequires:	libgpod-devel
BuildRequires:	pulseaudio-devel
# Used to determine power control methods at build-time
BuildRequires:	gnome-power-manager
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
GNOME MPlayer is a simple GUI for MPlayer. It is intended to be a
nice tight player and provide a simple and clean interface to
MPlayer. GNOME MPlayer has a rich API that is exposed via DBus.
Using DBus you can control a single or multiple instances of GNOME
MPlayer from a single command.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

desktop-file-install --vendor='' \
	--add-category="Audio;Video;GTK;Player;GNOME" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*.desktop

mv %{buildroot}%{_docdir}/%{name} installed-docs
rm installed-docs/{INSTALL,COPYING}

# zero length docs
find installed-docs -size 0 | xargs rm

rm -fr %buildroot%{_libdir}/nautilus/extensions-*/lib*.la

%find_lang %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc installed-docs/*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/gnome-control-center/default-apps/gnome-mplayer.xml
%dir %{_libdir}/nautilus
%dir %{_libdir}/nautilus/extensions-*
%{_libdir}/nautilus/extensions-*/lib*.so
%{_mandir}/man1/%{name}.1*

