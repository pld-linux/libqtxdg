%define		qtver		6.6.0

Summary:	QtXdg, a Qt6 implementation of XDG standards
Summary(pl.UTF-8):	QtXdg, implementacja standardów XDG w Qt6
Name:		libqtxdg
Version:	4.3.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Libraries
Source0:	https://github.com/lxqt/libqtxdg/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	dd6d86167ea86213d00dd82ec7ac88bb
URL:		http://www.lxqt.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6Svg-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	Qt6Xml-devel >= %{qtver}
BuildRequires:	cmake >= 3.18.0
BuildRequires:	glib2-devel >= 1:2.41.0
BuildRequires:	lxqt-build-tools >= 2.3.0
BuildRequires:	xterm
BuildRequires:	xz-devel
Obsoletes:	razor-qt
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QtXdg, a Qt6 implementation of XDG standards.

%description -l pl.UTF-8
QtXdg, implementacja standardów XDG w Qt6

%package devel
Summary:	libqtxdg - header files and development documentation
Summary(pl.UTF-8):	libqtxdg - pliki nagłówkowe i dokumentacja
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt6Core-devel >= %{qtver}
Requires:	Qt6DBus-devel >= %{qtver}
Requires:	Qt6Gui-devel >= %{qtver}
Requires:	Qt6Svg-devel >= %{qtver}
Requires:	Qt6Widgets-devel >= %{qtver}
Requires:	Qt6Xml-devel >= %{qtver}
Obsoletes:	razor-qt-devel

%description devel
This package contains header files and development documentation for
libqtxdg.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy
pisaniu własnych programów wykorzystujących libqtxdg.

%prep
%setup -q

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
    DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
/etc/xdg/lxqt-qtxdg.conf
/etc/xdg/qtxdg.conf
%{_libdir}/libQt6Xdg.so.4.*.*
%ghost %{_libdir}/libQt6Xdg.so.4
%{_libdir}/libQt6XdgIconLoader.so.4.*.*
%ghost %{_libdir}/libQt6XdgIconLoader.so.4
%{_libdir}/qt6/plugins/iconengines/libQt6XdgIconPlugin.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/qt6xdg
%{_includedir}/qt6xdgiconloader
%{_libdir}/libQt6Xdg.so
%{_libdir}/libQt6XdgIconLoader.so
%{_datadir}/cmake/qt6xdg
%{_datadir}/cmake/qt6xdgiconloader
%{_pkgconfigdir}/Qt6Xdg.pc
%{_pkgconfigdir}/Qt6XdgIconLoader.pc
