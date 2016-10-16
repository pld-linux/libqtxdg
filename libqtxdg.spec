%define		qtver		5.3.1

Summary:	libqtxdg
Name:		libqtxdg
Version:	2.0.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Libraries
Source0:	http://downloads.lxqt.org/libqtxdg/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	a5683d77db13c6e86b6b578050c6f435
URL:		http://www.lxqt.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.3
BuildRequires:	libmagic-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	qt5-linguist >= %{qtver}
BuildRequires:	xz-devel
Obsoletes:	razor-qt
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libqtxdg.

%package devel
Summary:	libqtxdg - header files and development documentation
Summary(pl.UTF-8):	libqtxdg - pliki nagłówkowe i dokumentacja do kdelibs
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core-devel >= %{qtver}
Requires:	Qt5Gui-devel >= %{qtver}
Requires:	Qt5Xml-devel >= %{qtver}
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
install -d build
cd build
%cmake \
	-DUSE_QT5=ON \
	../

%{__make}

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
%attr(755,root,root) %{_libdir}/libQt5Xdg.so.2.*.*
%ghost %{_libdir}/libQt5Xdg.so.2
%attr(755,root,root) %{_libdir}/libQt5XdgIconLoader.so.2.*.*
%ghost %{_libdir}/libQt5XdgIconLoader.so.2

%files devel
%defattr(644,root,root,755)
%{_includedir}/qt5xdg
%{_includedir}/qt5xdgiconloader
%attr(755,root,root) %{_libdir}/libQt5Xdg.so
%attr(755,root,root) %{_libdir}/libQt5XdgIconLoader.so
%{_datadir}/cmake/qt5xdg
%{_datadir}/cmake/qt5xdgiconloader
%{_pkgconfigdir}/Qt5Xdg.pc
%{_pkgconfigdir}/Qt5XdgIconLoader.pc
