%define name	gnome-mplayer
%define version	0.5.3
%define rel	1

Summary:	Simple GUI for MPlayer
Name:		%name
Version:	%version
Release:	%mkrel %rel
License:	GPL
URL:		http://dekorte.homeip.net/download/gnome-mplayer/
Source:		http://dekorte.homeip.net/download/gnome-mplayer/%name-%version.tar.gz
Group:		Video
BuildRoot:	%_tmppath/%name-root
Requires:	mplayer
BuildRequires:	libgnome2-devel
BuildRequires:	gnomeui2-devel
BuildRequires:	dbus-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	desktop-file-utils
BuildRequires:	ImageMagick

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
rm -rf %buildroot
%makeinstall_std

desktop-file-install --vendor="" \
	--add-category="Audio;Video;GTK;Player" \
	--dir %buildroot%_datadir/applications \
	%buildroot%_datadir/applications/*.desktop

mv %buildroot%_docdir/%name installed-docs
rm installed-docs/{INSTALL,COPYING}

# zero length docs
find installed-docs -size 0 | xargs rm

install -d -m755 %buildroot%_miconsdir
install -d -m755 %buildroot%_iconsdir
install -d -m755 %buildroot%_liconsdir

convert %name.png -resize 16x16 %buildroot%_miconsdir/%name.png
convert %name.png -resize 32x32 %buildroot%_iconsdir/%name.png
convert %name.png -resize 48x48 %buildroot%_liconsdir/%name.png

%find_lang %name

%clean
rm -rf %buildroot

%post
%post_install_gconf_schemas %name
%update_menus
%update_desktop_database

%preun
%preun_uninstall_gconf_schemas %name

%postun
%clean_menus
%clean_desktop_database

%files -f %name.lang
%defattr(-,root,root)
%doc installed-docs/*
%_sysconfdir/gconf/schemas/*.schemas
%_bindir/%name
%_datadir/applications/%name.desktop
%_datadir/pixmaps/%name.png
%_miconsdir/%name.png
%_iconsdir/%name.png
%_liconsdir/%name.png
