Summary:	idnkit - internationalized domain name toolkit
Summary(pl.UTF-8):	idnkit - zestaw narzędzi do umiędzynarodowionych nazw domen
Name:		idnkit
Version:	1.0
Release:	6
License:	BSD-like
Group:		Libraries
Source0:	http://www.nic.ad.jp/ja/idn/idnkit/download/sources/%{name}-%{version}-src.tar.gz
# Source0-md5:	e8863c21c5049af358bd59c384ff3e5d
URL:		http://www.nic.ad.jp/en/idn/index.html
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The 'idnkit' is an open source, BSD-like licensed software that
provides functionalities about Internationalized Domain Name
processing standardized at IETF. Major features that idnkit provides
are as follows:
 - libidnkit - Core library for IDN processing,
 - libidnkitlite - Light Weight library for IDN processing (UTF-8
   only),
 - idnconv - DNS zone / configuration file encoding converter
 - runidn / idn wrapper - Dynamic link resolver library for UNIX /
   Windows

%description -l pl.UTF-8
idnkit to wolnodostępne na licencji typu BSD oprogramowanie
zapewniające funkcjonalność związaną z obsługą umiędzynarodowionych
nazw domen (IDN - Internationalized Domain Name) standaryzowaną przez
IETF. Główne własności dostarczane przez idnkit są następujące:
 - libidnkit - główna biblioteka do przetwarzania IDN,
 - libidnkitlite - lekka biblioteka do przetwarzania IDN (tylko UTF-8),
 - idnconv - konwerter kodowania plików konfiguracyjnych i stref DNS
 - runidn / idn wrapper - dynamicznie konsolidowana biblioteka
   resolvera dla uniksów i Windows.

%package devel
Summary:	Header files for idnkit
Summary(pl.UTF-8):	Pliki nagłówkowe idnkit
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for idnkit.

%description devel -l pl.UTF-8
Pliki nagłówkowe idnkit.

%package static
Summary:	Static idnkit library
Summary(pl.UTF-8):	Statyczna biblioteka idnkit
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static idnkit library.

%description static -l pl.UTF-8
Statyczna biblioteka idnkit.

%prep
%setup -q -n %{name}-%{version}-src

%build
cp /usr/share/automake/config.sub  .
%configure2_13 \
	--enable-extra-ace \
	--enable-runidn

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README NEWS
%doc %lang(ja) README.ja
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/idn.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/idnalias.conf
%attr(755,root,root) %{_bindir}/idnconv
%attr(755,root,root) %{_bindir}/runidn
%attr(755,root,root) %{_libdir}/libidnkit.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libidnkit.so.1
%attr(755,root,root) %{_libdir}/libidnkitlite.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libidnkitlite.so.1
%attr(755,root,root) %{_libdir}/libidnkitres.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libidnkitres.so.1
# this one is used by runidn
%{_libdir}/libidnkitres.la
%dir %{_datadir}/idnkit
%{_datadir}/idnkit/*.map
%{_mandir}/man1/idnconv.1*
%{_mandir}/man1/runidn.1*
%{_mandir}/man5/idn.conf.5*
%{_mandir}/man5/idnalias.conf.5*
%{_mandir}/man5/idnrc.5*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libidnkit.so
%attr(755,root,root) %{_libdir}/libidnkitlite.so
%attr(755,root,root) %{_libdir}/libidnkitres.so
%{_libdir}/libidnkit.la
%{_libdir}/libidnkitlite.la
%dir %{_includedir}/idn
%{_includedir}/idn/*.h
%{_mandir}/man3/libidnkit.3*
%{_mandir}/man3/libidnkitlite.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libidnkit.a
%{_libdir}/libidnkitlite.a
%{_libdir}/libidnkitres.a
