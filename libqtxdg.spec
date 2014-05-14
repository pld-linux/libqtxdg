%define		qtver		4.8.5

Summary:	libqtxdg
Name:		libqtxdg
Version:	0.5.3
Release:	0.2
License:	GPLv2 and LGPL-2.1+
Group:		X11/Libraries
Source0:	http://lxqt.org/downloads/libqtxdg/0.5.3/%{name}-%{version}.tar.xz
# Source0-md5:	1a1058d61600907e15bca991a60a70d7
Patch0:		dirs.patch
Patch1:		deprecated.patch
URL:		http://www.lxqt.org/
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtXml-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.3
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
Requires:	QtCore-devel >= %{qtver}
Requires:	QtGui-devel >= %{qtver}
Requires:	QtXml-devel >= %{qtver}
Obsoletes:	razor-qt-devel

%description devel
This package contains header files and development documentation for
libqtxdg.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy
pisaniu własnych programów wykorzystujących libqtxdg.

%prep
%setup -q -c %{name}-%{version}
%patch0 -p1
%patch1 -p1

%build
install -d build
cd build
%cmake \
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
%attr(755,root,root) %{_libdir}/libqtxdg.so.*.*.*
%ghost %{_libdir}/libqtxdg.so.0
%dir %{_datadir}/libqtxdg
%lang(ar) %{_datadir}/libqtxdg/libqtxdg_ar.qm
%lang(cs_CZ) %{_datadir}/libqtxdg/libqtxdg_cs_CZ.qm
%lang(cs) %{_datadir}/libqtxdg/libqtxdg_cs.qm
%lang(da_DK) %{_datadir}/libqtxdg/libqtxdg_da_DK.qm
%lang(da) %{_datadir}/libqtxdg/libqtxdg_da.qm
%lang(de) %{_datadir}/libqtxdg/libqtxdg_de_DE.qm
%lang(el) %{_datadir}/libqtxdg/libqtxdg_el_GR.qm
%lang(eo) %{_datadir}/libqtxdg/libqtxdg_eo.qm
%lang(es) %{_datadir}/libqtxdg/libqtxdg_es.qm
%lang(es_VE) %{_datadir}/libqtxdg/libqtxdg_es_VE.qm
%lang(eu) %{_datadir}/libqtxdg/libqtxdg_eu.qm
%lang(fi) %{_datadir}/libqtxdg/libqtxdg_fi.qm
%lang(fr) %{_datadir}/libqtxdg/libqtxdg_fr_FR.qm
%lang(hu) %{_datadir}/libqtxdg/libqtxdg_hu.qm
%lang(id) %{_datadir}/libqtxdg/libqtxdg_id_ID.qm
%lang(it) %{_datadir}/libqtxdg/libqtxdg_it_IT.qm
%lang(ja) %{_datadir}/libqtxdg/libqtxdg_ja.qm
%lang(lt) %{_datadir}/libqtxdg/libqtxdg_lt.qm
%lang(nl) %{_datadir}/libqtxdg/libqtxdg_nl.qm
%lang(pl) %{_datadir}/libqtxdg/libqtxdg_pl_PL.qm
%lang(pt_BR) %{_datadir}/libqtxdg/libqtxdg_pt_BR.qm
%lang(pt) %{_datadir}/libqtxdg/libqtxdg_pt.qm
%lang(ro) %{_datadir}/libqtxdg/libqtxdg_ro_RO.qm
%lang(ru) %{_datadir}/libqtxdg/libqtxdg_ru.qm
%lang(ru_RU) %{_datadir}/libqtxdg/libqtxdg_ru_RU.qm
%lang(sk) %{_datadir}/libqtxdg/libqtxdg_sk_SK.qm
%lang(sl) %{_datadir}/libqtxdg/libqtxdg_sl.qm
%lang(sr) %{_datadir}/libqtxdg/libqtxdg_sr_RS.qm
%lang(th) %{_datadir}/libqtxdg/libqtxdg_th_TH.qm
%lang(tr) %{_datadir}/libqtxdg/libqtxdg_tr.qm
%lang(uk) %{_datadir}/libqtxdg/libqtxdg_uk.qm
%lang(zn_CN) %{_datadir}/libqtxdg/libqtxdg_zh_CN.qm
%lang(zn_TW) %{_datadir}/libqtxdg/libqtxdg_zh_TW.qm

%files devel
%defattr(644,root,root,755)
%{_includedir}/qtxdg
%attr(755,root,root) %{_libdir}/libqtxdg.so
%{_pkgconfigdir}/qtxdg.pc
%{_datadir}/cmake/qtxdg
