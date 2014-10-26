%define		qtver		5.3.1

Summary:	libqtxdg
Name:		libqtxdg
Version:	1.0.0
Release:	0.3
License:	GPLv2 and LGPL-2.1+
Group:		X11/Libraries
Source0:	http://lxqt.org/downloads/libqtxdg/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	394b6cedec6d580d387a73842343f53e
URL:		http://www.lxqt.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.3
BuildRequires:	libmagic-devel
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
%setup -q -n libqtxdg

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
%attr(755,root,root) %{_libdir}/libQt5Xdg.so.*.*.*
%ghost %{_libdir}/libQt5Xdg.so.1
%dir %{_datadir}/libqt5xdg
%lang(ar) %{_datadir}/libqt5xdg/libqtxdg_ar.qm
%lang(cs_CZ) %{_datadir}/libqt5xdg/libqtxdg_cs_CZ.qm
%lang(cs) %{_datadir}/libqt5xdg/libqtxdg_cs.qm
%lang(da_DK) %{_datadir}/libqt5xdg/libqtxdg_da_DK.qm
%lang(da) %{_datadir}/libqt5xdg/libqtxdg_da.qm
%lang(de) %{_datadir}/libqt5xdg/libqtxdg_de_DE.qm
%lang(el) %{_datadir}/libqt5xdg/libqtxdg_el_GR.qm
%lang(eo) %{_datadir}/libqt5xdg/libqtxdg_eo.qm
%lang(es) %{_datadir}/libqt5xdg/libqtxdg_es.qm
%lang(es_VE) %{_datadir}/libqt5xdg/libqtxdg_es_VE.qm
%lang(eu) %{_datadir}/libqt5xdg/libqtxdg_eu.qm
%lang(fi) %{_datadir}/libqt5xdg/libqtxdg_fi.qm
%lang(fr) %{_datadir}/libqt5xdg/libqtxdg_fr_FR.qm
%lang(hu) %{_datadir}/libqt5xdg/libqtxdg_hu.qm
%lang(id) %{_datadir}/libqt5xdg/libqtxdg_id_ID.qm
%lang(it) %{_datadir}/libqt5xdg/libqtxdg_it_IT.qm
%lang(ja) %{_datadir}/libqt5xdg/libqtxdg_ja.qm
%lang(lt) %{_datadir}/libqt5xdg/libqtxdg_lt.qm
%lang(nl) %{_datadir}/libqt5xdg/libqtxdg_nl.qm
%lang(pl) %{_datadir}/libqt5xdg/libqtxdg_pl_PL.qm
%lang(pt_BR) %{_datadir}/libqt5xdg/libqtxdg_pt_BR.qm
%lang(pt) %{_datadir}/libqt5xdg/libqtxdg_pt.qm
%lang(ro) %{_datadir}/libqt5xdg/libqtxdg_ro_RO.qm
%lang(ru) %{_datadir}/libqt5xdg/libqtxdg_ru.qm
%lang(ru_RU) %{_datadir}/libqt5xdg/libqtxdg_ru_RU.qm
%lang(sk) %{_datadir}/libqt5xdg/libqtxdg_sk_SK.qm
%lang(sl) %{_datadir}/libqt5xdg/libqtxdg_sl.qm
%lang(sr) %{_datadir}/libqt5xdg/libqtxdg_sr_RS.qm
%lang(th) %{_datadir}/libqt5xdg/libqtxdg_th_TH.qm
%lang(tr) %{_datadir}/libqt5xdg/libqtxdg_tr.qm
%lang(uk) %{_datadir}/libqt5xdg/libqtxdg_uk.qm
%lang(zn_CN) %{_datadir}/libqt5xdg/libqtxdg_zh_CN.qm
%lang(zn_TW) %{_datadir}/libqt5xdg/libqtxdg_zh_TW.qm

%files devel
%defattr(644,root,root,755)
%{_includedir}/qt5xdg
%attr(755,root,root) %{_libdir}/libQt5Xdg.so
%{_pkgconfigdir}/Qt5Xdg.pc
%{_datadir}/cmake/qt5xdg
