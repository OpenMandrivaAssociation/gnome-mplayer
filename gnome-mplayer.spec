Summary:	Simple GUI for MPlayer
Name:		gnome-mplayer
Version:	0.6.1
Release:	%mkrel 1
License:	GPLv2+
Group:		Video
URL:		http://dekorte.homeip.net/download/gnome-mplayer/
Source:		http://dekorte.homeip.net/download/gnome-mplayer/%name-%version.tar.gz
Requires:	mplayer
BuildRequires:	libgnome2-devel
BuildRequires:	gnomeui2-devel
BuildRequires:	dbus-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	desktop-file-utils
BuildRequires:	ImageMagick
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
GNOME MPlayer is a simple GUI for MPlayer. It is intended to be a
nice tight player and provide a simple and clean interface to
MPlayer. GNOME MPlayer has a rich API that is exposed via DBus.
Using DBus you can control a single or multiple instances of GNOME
MPlayer from a single command.

%prep
%setup -q
sed -i s,Icon=gnome-player.png,Icon=gnome-player, gnome-mplayer.desktop

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

desktop-file-install \
	--add-category="Audio;Video;GTK;Player" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*.desktop

mv %{buildroot}%{_docdir}/%{name} installed-docs
rm installed-docs/{INSTALL,COPYING}

# zero length docs
find installed-docs -size 0 | xargs rm

install -d -m755 %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps

convert %{name}.png -resize 16x16 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
convert %{name}.png -resize 32x32 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert %{name}.png -resize 48x48 %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png

%find_lang %{name}

%clean
rm -rf %{buildroot}

%post
%post_install_gconf_schemas %{name}
%{update_menus}
%{update_desktop_database}
%update_icon_cache hicolor

%preun
%preun_uninstall_gconf_schemas %{name}

%postun
%{clean_menus}
%{clean_desktop_database}
%clean_icon_cache hicolor

%files -f %{name}.lang
%defattr(-,root,root)
%doc installed-docs/*
%{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.png
